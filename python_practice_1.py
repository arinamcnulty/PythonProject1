print("Oryna Zudilova, 4-rd group, software engineering")
print("PRACTICE")
print("<<Numbers>>")
a=55
b=45
c=a+b
print(c)
print("<<Comparing true or false>>")
x=True
y=False
print(x==y)
print(x and y)
print(x or y)
print(not x)
print("<<Age bool>>")
age=19
print(age>=18)
print("<<Text>>")
text="python"
print(text.upper())
print(text.lower())
print(text.replace("python", "python2"))
print("<<List>>")
numbers=[1,2,3,4,5]
numbers.append(6) #add last element
print(numbers)
numbers.pop()   #delete last element
print(numbers)
numbers.insert(0,6) #replace first number on 6
print(numbers)
numbers.remove(3)  #remove element 3
print(numbers)
print("<<Tuple>>")
zahlen=(1,2,3,4,5,6) #can`t change this
print(zahlen)
print("<<Set>>")
myset={6,7,6,5,4,3,4,5,6,}
print(myset)  #sorte and delete double elements
a={1,2,3,4,5}
b={5,6,7,8,9}
print(a&b)
print(a|b)
print("<<Dict>>")
person={
    "name":"Arina",
    "age":19,
    "city":"Kyiv"
}
print(person["name"],person["city"],person["age"])
person["job"]="Developer" #add new information
print(person)
person["age"]=20 #change age
print(person)
if "name" in person:
    print("Person has a name"+" "+person["name"])
if "city" in person:
    print("Person has a city"+" "+person["city"])
del person["city"] #delete person`s city
print(person)
print("New information about the person")
for key,value in person.items(): # write all information about person
    print(key,":",value)













