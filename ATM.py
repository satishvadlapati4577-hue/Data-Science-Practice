import random
print("welcome to SBI ATM")
print("please enter your debit card")
print("choose the required options")
options = ''' 1: Quick cash, 2:transfer,3:balance inq, 4:registration,5:pin generation , 6:mini statement,7:exit'''
balance=20000
transcation=[]
def quick_cash():
    global balance
    cash= input("enter the amount")
    if cash.isnumeric():
        cash=int(cash)
        if cash<=balance:
            print("please collect your cash")
            transcation.append(cash)
            balance-=cash
        else:
            print("print amount exceeds the current balance")
    else:
     print("enter the numerics")
def transfer():
   acc=input("enter the account number")
   print("account number should be contains 10 digits")
   if len(acc)==10:
      amount=input("enter the amount")
      print(f"amount is successfully transfered to{acc}")
   else:
      print(f"enter the correct account number")
def balanceinq():
   print(f"available amount is {balance} ")
def registration():
   name=print(input(f"enter the full name"))
   aadhar=int(input("enter the aadhar no"))
   accountno = 0
   while True:
      choice=input("enter 1 for current account type or enter  2 for savings accoount type")
      if choice == "1":
         accountno=random.randint(4000000000,6000000000)
         print(accountno)
         break
      elif choice=="2":
         accountno=random.randint(400000000,2000000000)
         print(accountno)
      break
def pingeneration():
      pin=random.randint(2000,8099)
      print(pin)
def ministatement():
   if len(transcation)>0:
      for i in transcation:
         print(i)
   else:
      print("no transcation")
def exit():
   print(f"thank you & visit again")

print(options)
while True:
   choice=int(input("enter the options"))
   if choice== 1:
      quick_cash()
   elif choice == 2:
      transfer()
   elif choice == 3:
      balanceinq()
   elif choice == 4:
      registration()
   elif choice== 5:
      pingeneration()
   elif choice == 6:
      ministatement()     
   elif choice == 7:
      exit() 
      break
   else:
     print("invalid option")     
                              
                     
 