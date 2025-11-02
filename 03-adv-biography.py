name = input("Enter your name: ")
hometown = input("Enter your hometown: ")
age = input("Enter your age: ")

if age.isdigit():
    age = int(age)
else:
    print("Please enter a number for age next time.")
    age = 20

bio = {
    "name": name,
    "hometown": hometown,
    "age": age
}

print("Name:", bio["name"])
print("Hometown:", bio["hometown"])
print("Age:", bio["age"])