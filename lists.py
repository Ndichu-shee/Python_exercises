a=["boy","girl","women","men"]
b=["school","country "]
c=a+b
print(c)
a=["boy","girl","women","men"]
b=["school","country"]
c=a+b
print(c*3)
print("----")

#append-appends a new item to the bottom of the list.
names = ['yonce','shak','riri']
names.append('cardi')
print(names)
print("----")
#extend-appends a new list to the current list.
names.extend(['dolly','nicki','migos'])
print(names)
print("----")
#remove-removes a given item from the list.
names.remove('cardi')
print(names)
print("----")
#sort-sort items in an ascending manner.
names.sort()
print(names)
print("----")
#reverse-reverses the order of items in the list
names.reverse()
print(names)
print("----")
#pop-removes the last item from a given list
names.pop()
print(names)


nums = [5,6,7,8,9,10]
for n in nums:
     print(n*4)
print("____")
     
numbers = [5,6,7,8,9] #operation on each element
for n in numbers:
  print(n + 5)
for n in numbers:
  print(n * 5)
for n in numbers:
  print(n * n)
for n in numbers:
  print(n / 5)
for n in numbers:
  print(n % 5)
print("___")
num = [5,10,15,50,25,30]
squares = []
for b in num:
  square = b * b
  squares.append(square)
print(squares)
print("---")
num = [5,10,15,20,25,30]
squares = [b * b for b in num]
print (squares)