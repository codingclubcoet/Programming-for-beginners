#program that takes cost price and selling price as input and displays whether the transaction is a Profit or a Loss or Neither
c=int(input())
s=int(input())
if(c<s):
  print("Profit",end='')
elif(c==s):
  print("Neither",end='')
else:
  print("Loss",end='')
