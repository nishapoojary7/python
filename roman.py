
def roman2Dec(romanStr):
    roman_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    #ANALYSE STING BACKWARDS
    romanBack=list(romanStr)[::-1]
    value=0
    # to keep track of order
    rightVal=roman_dict[romanBack[0]]
    for numeral in romanBack:
        leftVal=roman_dict[numeral]
    # check for subtraction
        if leftVal<rightVal:
            value-=leftVal
        else:
            value+=leftVal
        rightVal=leftVal
    return value
romanStr=input("enter the roman number : ")
print(roman2Dec(romanStr))
    
