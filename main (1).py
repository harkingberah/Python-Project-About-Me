score = 0
answer = input("Which planet is known as 'The Red Planet'? Mars or Mercury? ")
if answer == 'Mars':
    print("Correct!")
    score += 1
else:
    print("Sorry, the answer is Mars.")
    
answer = input("What is the largest planet in our Solar system? Saturn or Jupiter? ")
if answer == "Jupiter":
    print("Correct!")
    score += 1
else:
    print("Sorry, the answer is Jupiter.")
    
answer = input("What planet spins on its side? Pluto or Uranus ")
if answer == "Uranus":
    print("Correct!")
    score += 1
else:
    print("Sorry, the answer is Uranus.")
    
answer = input("What planet is closest to the Sun? Mercury or Neptune ")
if answer == "Mercury":
    print("Correct!")
    score += 1
else:
    print("Sorry, the answer is Mercury.")

answer = input("On what planet do we live? Mars or Earth ")
if answer == "Earth":
    print("Correct!")
    score += 1
else:
    print("Sorry, the answer is Earth.")
    
print("You Scored:", score)