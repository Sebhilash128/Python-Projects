Gryffindor=0
Ravenclaw=0
Hufflepuff=0
Slytherin=0

print("Welcome to the Sorting Hat Quiz!")
print("Answer the following questions to find out which Hogwarts house you belong to.")

# Question 1
Answer=int(input("1. Do you like dawn or dusk? 1.[dawn] 2.[dusk]"))
if Answer==1:
    Gryffindor+=1
    Ravenclaw+=1
else:
    Hufflepuff+=1
    Slytherin+=1

# Question 2
Answer=int(input("2. When I'm dead, I want people to remember me as: 1.[The Good] 2.[The Great] 3.[The Wise] 4.[The Bold]"))
if Answer==1:
    Hufflepuff+=2
elif Answer==2:
    Slytherin+=2
elif Answer==3:
    Ravenclaw+=2
else:
    Gryffindor+=2

# Question 3
Answer=int(input("3. Which kind of instrument most pleases your ear? 1.[The violin] 2.[The trumpet] 3.[The piano] 4.[The drum]"))
if Answer==1:
    Slytherin+=4
elif Answer==2:
    Hufflepuff+=4
elif Answer==3:
    Ravenclaw+=4
else:
    Gryffindor+=4

# Determine the house with the highest score

print(f"Gryffindor: {Gryffindor}, Ravenclaw: {Ravenclaw}, Hufflepuff: {Hufflepuff}, Slytherin: {Slytherin}")

max_score = max(Gryffindor, Ravenclaw, Hufflepuff, Slytherin)
if max_score == Gryffindor:
    print("You belong in Gryffindor!")
elif max_score == Ravenclaw:
    print("You belong in Ravenclaw!")
elif max_score == Hufflepuff:
    print("You belong in Hufflepuff!")
else:
    print("You belong in Slytherin!")



