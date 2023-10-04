#In this exercise, you will need to add numbers and strings to the correct lists using the "append" list method. You must add the numbers 1,2, and 3 to the "numbers" list, and the words 'hello' and 'world' to the strings variable.
#You will also have to fill in the variable second_name with the second name in the names list

numbers=[]
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings=[]

names=["John","Eric","Mona"]
second_name=names[1]

strings.append("Hello")
strings.append("World")

print(numbers)
print(strings)

print("Second name in names list is %s" %second_name)