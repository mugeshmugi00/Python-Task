##userName="mugesh"
##enterUserName=input("Please Enter Your User Name:")
##passWord="2002"
##enterUserPassword=input("Please Enter Your User Pasword:")
##withdrawal=0
##balance=3000
##deposit=0
##Balance="1"
##Withdrawal="2"
##Deposit="3"    
##
##if(userName == enterUserName and passWord == enterUserPassword):
##    if(userName == enterUserName):
##        if(passWord == enterUserPassword):
##
##            print(1,"balance-")
##            print(2,"withdrawal-")
##            print(3,"deposit-")
##
##            userInput=input(":")
##            if(userInput>0 and userInput<4):
##
##                if(userInput == Balance):
##                    print(balance)
##    
##                if(userInput == Withdrawal):
##                    userWithdrawal=int(input("Enter Withdrawal Amount:"))
##                    if(userWithdrawal < balance):
##                        balanceAmount=balance-userWithdrawal
##                        print("Balance Amount:",balanceAmount)
##                    else:
##                        print("Insufficient Amount!")
##        
##                if(userInput == Deposit):
##                    userDeposit=int(input("Enter Deposit Amount:"))
##                    if(userDeposit > 0):
##                        depositAdd=balance+userDeposit
##                        print("Total Amount:",depositAdd)
##        else:
##            print("Please Enter Valid Password!")           
##    else:
##        print("Please Enter Valid User Name!")              
##else:
##    print("Both User Name and Password Incorrect!")                      
##    
##
##
##Take 10 integer inputs from user and
##store them in a list. Again ask user
##to give a number. Now, tell user whether
##that numberis present in list or not.

userInput=int(input("Enter the number:"))
list1=[]
for i in range(1,userInput+1,1):
    list1.append(i)
print(list1)
user=int(input("Enter the number:"))
if userInput in user:
    print("Present")
else:
    print("Not Present")





















