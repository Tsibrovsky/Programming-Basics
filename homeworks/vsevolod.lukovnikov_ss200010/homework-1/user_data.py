name = input("What is your name?")
surname = input("What is your surname?")
age = input("How old are you?")
profession = input("What is your profession?")
data = " My name is %s %s. I'm %s years old and I'm %s" % (name,surname, age, profession)
print(data)
file = open("data.txt", "wt")
file.write(data)
