# I want this program to ask the user
# the month they were born in "What month were you born in?" and then,
# I want this program to ask the user how old they are, 
# "How old are you?" and then,
# I want the program to say back "You were born in MONTH and are AGE years old"

#step 1 ask for birth month
print("What month were you on born?")
#step 2 input the user's birth month from the keyboard
Birth_month = input()

#step 3 ask for their age
print("How old are you?")
#step 4 recieve their age as the variable age
your_age = input()
#step 3 say back i am AGE years old as well using their age
print("You were born on " + Birth_month + " and are " + your_age + " years old")

# math we could do here is 
# addition, subtraction, multiplication, 
# division, modulo (divide & get remainder), 
# Exponentiation (powers)
# examples are: 
# - calculating age or birth year
# - converting between metric and imperial

Century =  100 - int(your_age)
print("You have " + str(Century) + " Year(s) Until you are 100 years old.")
