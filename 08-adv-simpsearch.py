names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

search = input("Enter the name to search: ")

search_lower = search.lower()
found = False

for name in names:
    if name.lower() == search_lower:
        found = True
        break

if found:
    print(search.capitalize(), "found!")
else:
    print(search.capitalize(), "not found.")