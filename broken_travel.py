# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin?")) # Changed '==' to '=' for assignment and fixed input . to ( and added " instead of ' at the end

if year < 1900: #removed = for correct logic and added : for if statement
    print ("Woah, that's the past!") # Changed ' to "
elif year >= 1900 and year <= 2020: #Changed > to >= , < to <= to match question and changed && to and for correct logic operator
    print ("That's totally the present!")
else: #Changed elif to else because its the last one
    print ("Far out, that's the future!!")
