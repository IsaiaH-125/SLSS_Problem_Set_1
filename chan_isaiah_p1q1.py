# Quiz creation activity

# Quiz has 5 questions the user will answer
# It will keep track of score and give a final result

import time

print('An Idiots quiz!\n')

points = 0

question_one = int(input(f"What is the correct answer for 1+1?\n"))
if question_one == 2:
    print("\nYou got the easiest question correct!!")
    print("+1 point wow.\n")
    points += 1
else:
    print("that was wrong.")
    print("You didn't gain any points")

question_two = input('Where is Canada located\n' 'a) NA\n''b) France\n''c) Asia\n''d) America\n')
if question_two.lower() == "a":
    print('Well done.')
    print('+1 points wow.\n')
    points += 1
else:
    print("really?? that’s just sad.")
    print("You missed out on the greatest reward, points.\n")

question_three = input("cereal then milk or milk then cereal\n""A\n""or\n""B\n")
if question_three.lower() == "a":
    print("You picked the correct choice")
    print("You got 3 extra points for the better answer!\n")
    points += 3
else:
    print("Tsk.. Tsk..")
    print("You got -3 points\n")
    points -= 3

question_four = input("solve for y: 2 + 4y = 18\n")
if question_four == "4":
    print("A good answer")
    print("+1 point!\n")
    points += 1
else:
    print("ok.")
    print("-2 points...\n")
    points -= 2

question_five = int(input(f"Solve for x: 3x - 18 = 6\n"))
if question_five == 8:
    print("Good job!")
    print("+2 points!\n")
    points += 2
else:
    time.sleep(1.0)
    print("....")
    time.sleep(1.0)
    print("really...")
    print("-8 points. Not the right answer.\n")
    points -= 8

time.sleep(2.0)
points = points
print("This is the end of the quiz!")
print(f"{points}/8 points have been acquired!\n")
if points == 8:
    print("Good job you aced the easiest quiz ever!")
elif points in range(6, 7):
    print("You did good, kinda..")
elif points in range(4, 5):
    print("sad.")
else:
    print(".......")
