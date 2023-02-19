import re
import random
from collections import defaultdict

def compute(filename):
    try:
        # Open the file in read mode and convert the text to lowercase
        with open(filename, 'r') as f:
            text = f.read().lower()

        # Find all the words in the text using regex
        data = re.findall(r'\b\w+\b', text)

        # Calculate the number of unique words and the total number of words
        uniq = len(set(data))
        total = len(data)
        
        # Count the frequency of each word in the text
        count = defaultdict(int)
        for word in data:
            count[word] += 1
        
        # Sort the words by frequency and get the top 5 words
        top_5_words = sorted(count.items(), key=lambda x: x[1], reverse=True)[:5]

        # Split the text into sentences and remove any empty sentences
        sens = re.split(r'[.!?]+', text)
        sens = [group.strip() for group in sens if group.strip()]
        
        # Calculate the number of sentences in the text
        tot_sens = len(sens)
        
        # Calculate the number of sentences that are too short or too long
        slsens = 0
        for group in sens:
            if len(group.split()) < 5 or len(group.split()) > 35:
                slsens += 1
        
        # Count the number of consecutive punctuation marks
        consecutive_punctuations = sum(1 for i in range(1, len(text)) if text[i] in '.,;:' and text[i-1] in '.,;:')

        # Calculate the features
        f1 = uniq / total
        f2 = sum(count for _, count in top_5_words) / total
        f3 = slsens / tot_sens
        f4 = consecutive_punctuations / total
        f5 = 1 if total > 750 else 0

        # Calculate the net score
        net_score = 4 + f1 * 6 + f2 * 6 - f3 - f4 - f5
        return net_score, top_5_words, data
    except Exception as e:
        print(f"An error occurred while processing the file {filename}: {e}")
        return None, None, None

def write_scores(scores):
    try:
        # Open the scores file in write mode
        with open('scores.txt', 'w') as f:
            # Write the scores for each file
            for filename, score in scores.items():
                if score[0] is None:
                    f.write(f"No score available for file {filename}\n")
                else:
                    f.write(filename + '\n')
                    f.write('score: ' + str(score[0]) + '\n')
                    f.write('most used word: ' + ', '.join(word for word, _ in score[1]) + '\n')
                    f.write('random words: ' + ', '.join(random.sample(score[2], 5)) + '\n')

        # List of filenames to process
    except Exception as e:
        print(f"An error occurred while processing the file {filename}: {e}")
        return None, None, None

    
filenames = ['file1.txt','file2.txt']

# Calculate the scores for each file
scores = {filename: compute(filename) for filename in filenames}

# Write the scores to a file
write_scores(scores)
