name = input("What is your name? ")
age = int(input("What is your age? "))

wants_to_play = input("Do you want to play? (yes/no) ")
if wants_to_play == "yes".upper():
  print("Let's play!")
if wants_to_play == "no":
  print("Okay, bye!")


question1 = input("""Santa comes on the path,
The coat in the back. (write only in lower case) """)
if question1 == "bear":
  ans = input("""Floating boat
On the sands, travelers! (write only in lower case) """)
else:
  print("You lose...")

if ans == "camel":
  print("YAY! You win!")
else:
  print("You lose...")
