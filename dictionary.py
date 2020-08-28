

eunice={"name":"Eunice","age":18,"country":"Kenya","county":"nairobi"}
alice={"name":"Alice","age":19,"country":"Kenya","county":"mombasa"}
agnes={"name":"Agnes","age":18,"country":"Kenya","county":"kisumu"}
violet={"name":"Violet","age":20,"country":"Kenya","county":"nairobi"}
lydiah={"name":"Lydiah","age":19,"country":"Kenya","county":"machakos"}
students=[eunice,alice,violet,lydiah]
print(students)
for student in students:
  name = student["name"]
  age = student["age"]
  county = student["county"]
  sentence = "{} is {} years and is from {} county".format(name,age,county)
  print(sentence) 
for student in students:
  age=student["age"]
  newAge=(age * 3)
  name=student["name"]
  sentence="{} age * 3 is {}".format(name,newAge)
  print(sentence)
for student in students:
  #name=student["name"]
  year=(2019-student["age"])
  age=student["age"]
  name=student["name"]
  sentence="{} was born in {}".format(name,year)
  print(sentence) 