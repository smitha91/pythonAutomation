age = int(input("How old are you?\n"))
decade = age//10 # divide and get whole number
years = age % 10 # get the remainder
print("You are " + str(decade) + " decades and " + str(years) + " years old")