import random

f=open('file2.txt','r')
words=[]
compare_list1=[]
compare_list2=[]
i=0
j=0
missing_letters=[]
for i in f:
    words.append((i.split())[0])
# print(words)   
# print(len(words))
rand=random.randint(0,len(words))
choosen_word=words[rand]
print(choosen_word)
k=0
inp="abc"
while inp!=choosen_word:
    inp=str(input("Guess the word: "))

    for i in choosen_word:
        compare_list1.append(i)
    for j in inp:
        compare_list2.append(j)
    # print((compare_list1))
    # print((compare_list2))


    for i in range(len(inp)):
        if compare_list2[i]==compare_list1[i]:
            print(compare_list1[i],end='')
        else:
            print("_",end="")
            missing_letters.append(compare_list1[i])
    print()
    print("Missing letters: ",end="")
    for i in range(len(missing_letters)):
        print(missing_letters[i],end=",")
    print()
    if len(missing_letters)==0:
        print("Congratulations! You guessed the word correctly.. ")
    else:
        print("Opps! You missed, you have ",6-(k+1), "Chances left...")
    k+=1
    if k==6:
        break

    print(".............................")
    compare_list2.clear()
    missing_letters.clear()


