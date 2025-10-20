import random
#Method 1
responses = random.randint(0, 9)

if responses == 0:
    print("It is certain.")
elif responses == 1:
    print("It is decidedly so.")    
elif responses == 2:
    print("Reply hazy, try again.")
elif responses == 3:
    print("Cannot predict now.")
elif responses == 4:
    print("Do not count on it.")
elif responses == 5:
    print("My sources say no.")
elif responses == 6:
    print("Outlook not so good.")  
elif responses == 7:
    print("Signs point to yes.")
elif responses == 8:
    print("Yes - definitely.")  
else:
    print("Out of my league.") 

#Method 2
responses = [
    "It is certain.",
    "It is decidedly so.",
    "Reply hazy, try again.",
    "Cannot predict now.",
    "Do not count on it.",
    "My sources say no.",
    "Outlook not so good.",
    "Signs point to yes.",
    "Yes - definitely.",
    "Out of my league."
]

print(random.choice(responses))
