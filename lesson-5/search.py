search = input("Please enter a search word : ")
print(f"You entered : {search} ")

with open("rockyou.txt", "r", encoding="latin-1") as file:
    count = 0
    for line in file:
        newline = line.split()
        if search.lower() in newline:
            count = count + 1

print(f"The word {search} is repeated {count} once")
