wordlist= []
n= int(input())
wordlist= [input() for i in range(n)]
wordset= list(set(wordlist))
print(len(wordset))
for i in wordset:
    print(i, wordlist.count(i))
