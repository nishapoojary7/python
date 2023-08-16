
class PaliStr:
    def __init__(self):
       self.isPali = False
    def chkPalindrome(self,myStr):
        if myStr == myStr[::-1]:
            self.isPali = True
        else:
            self.isPali= False
        return self.isPali
class PaliInt(PaliStr):
    def __init__(self):
      self.isPali= False
    def chkPalindrome(self,val):
        temp = val
        rev = 0
        while temp != 0:
            dig = temp % 10
            rev = (rev * 10)+dig
            temp=temp//10
        if val==rev:
            self.isPali= True
        else:
            self.isPali = False
        return self.isPali
st = input("enter the string")
stObj = PaliStr()
if stObj.chkPalindrome(st):
    print("given string is palindrome")
else:
    print("given string is not a palindrome")
val = int(input("enter a integer"))
intObj = PaliInt()
if intObj.chkPalindrome(val):
    print("given integer is palindrome")
else:
    print("given integer is not a palindrome")
