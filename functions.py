#keyword argument
def year_of_birth(name,age):
  year=2020-age
  print("Hello {} you were born in year {}".format(name,year))
year_of_birth("Aisha",20) #positional arg
year_of_birth(name="Auma",age=19) #keyword arg
year_of_birth(age=21,name="Rose")
print("----")
#Default argument
def my_country(country="uganda"):
  print("l am from {}".format(country))
my_country()
my_country(country="Kenya")
my_country(country="Rwanda")
print("---")

def greet(*names):
  for name in names:
    print("Hello {}".format(name))
greet("Joy","Joyce")
greet("Joy","Joyce","Wanjiru","Ndichu")
print("---")
def sum(*args):
  print("I will now find the sum of {}".format(args))
  total=0
  for x in args:
      total +=x
  print("The answer is {}".format(total))
  return
sum(67,29)
sum(12,78,53)
sum(57,84,63,57,37)
sum(1270,2220,5530,530)
print("----")
def greet(**kwargs):
   print(kwargs)
greet(name="Joy",age=20)
greet(name="Joyce",age=25,country="Uganda")
greet(name="Wanjiru",age=21,country="kenya",county="Nairobi")