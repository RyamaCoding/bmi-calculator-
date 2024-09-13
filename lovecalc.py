print("Welcome to the love calculator")
name1 = input("What is your name? \n").lower()
name2 = input("What is your name? \n").lower()

# Count occurrences of t, r, u, e in both names
true_count = (
    name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e")
    + name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")
)

# Count occurrences of l, o, v, e in both names
love_count = (
    name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e")
    + name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")
)

love_score = int(str(true_count) + str(love_count)) 

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}%, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}%, you are a alright together.")
else:
    print(f"Your score is {love_score}%.")