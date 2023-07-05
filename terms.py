
str1=input("enter the string 1\n")
str2=input("enter the string 2\n")
if len(str2)<len(str1):
 short=len(str2)
 long=len(str1)
else:
    short=len(str1)
    long=len(str2)
matchCnt=0
for i in range(short):
    if str1[i]==str2[i]:
        matchCnt+=1
print("similarities between two said strings :")
print(matchCnt/long)
