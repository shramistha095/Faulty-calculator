#creating a dictonary that will take a value from user and return the meaning from word
#dict={ " conqueror":" winner"," finicky":" whos not satisfied"," impeccable":"perfect"," pompous":"fashionable"}
#word=input(" enter the word")
#print(dict[word])
#creating a faulty calculator which will give 45*3 as 555, 56+9=77,56/6=4*
operand1=int(input("enter first operand"))
operand2=int(input("Enter second operand"))
print(" enter the operand")
operator=input()
if operand1==45 and operand2==4 and operator=="*":
    print(" multipication is 555")
elif  operand1==56 and operand2==9 and operator=="+":
    print(" addition is 77")
elif operand1==56 and operand2==6 and operator=="/":
    print(" division is 4")
elif operator=="+":
    print(operand1+operand2)
elif operator=="-":
    print(operand1-operand2)
elif operator=="*":
    print(operand1*operand2)
elif operator=="/":
    print(operand1/operand2)
else:
    print(" invalid input")



