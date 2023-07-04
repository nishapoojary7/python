
sentence=input("enter the sentence :")
wordList=sentence.split(" ")
print("this sentence has",len(wordList),"words")
digCnt=upCnt=loCnt=0

for ch in sentence:
 if '0'<=ch<='9':
     digCnt+=1
 elif 'A'<=ch<='Z':
     upCnt+=1
 elif 'a'<=ch<='z':
     loCnt+=1
print("this sentence has",digCnt,"digits",upCnt,"upper case letters",loCnt,"lower case letters")

