#Part 1
# I want this program to ask the user
# their favorite month "What's your favorite month?" and then,
# I want the program to say back "I like FAV_MONTH too" where FAV_MONTH is their favorite month
#Part 2
# I want this program to ask the user for a value
# that says how old they are, "How old are you?" and then,
# I want the program to say back "I am AGE years old as well" where
# AGE is how old they are

#Part 1
#step 1 ask for favorite month
print("What is your favorite month?")
#step 2 input the user's favorite month from the keyboard
fav_month = input()
#step 3 say i like back with their favorite month
print("I like " + fav_month + " too")

#Part 2
#step 1 as for their age
print("How old are you?")
#step 2 recieve their age as variable age
age = input()
#step 3 say back i am AGE years old as well using their age
print("I am " + str(age) + " years old as well")