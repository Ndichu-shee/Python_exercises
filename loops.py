print ("Hello, Dcoder!")
x=range(10)
print(x)
for y in x:
  print(y)
print("---")
a=range(2,10)
for x in a:
  print(x)
print("___")
x=range(10)
for y in x:
  if y%3==0:
      print(y)
print("___")
x=range(10)
for y in x:
  if y%3!=0:
      print(y)
print("___")
n=range(20)
for x in n:
  if x%5==0:
       print("{} is divisible by 5".format(x))
  else:
       print("{} is not divisible by 5".format(x))
print("___")
n=range(30)
for x in n:
  if x%5==0:
      print("{} is divisible by 5".format(x))
  elif x%7==0:
        print("{} is divisible by 7".format(x))
  else:
      print("{} is not divisible by 5 or 7".format(x))