import random

 

options = ["Rock", "Paper", "Scissors"]

 

user_choice = input("Choose Rock, Paper, or Scissors: ")

computer_choice = random.choice(options)

 

print("You chose: ", user_choice)

print("Computer chose: ", computer_choice)

 

if user_choice == "Rock" and computer_choice=="Rock":

    print("It's a tie!")

elif user_choice == "Paper" and computer_choice=="Paper":

    print("It's a tie!")

elif user_choice == "Scissors" and computer_choice=="Scissors":

    print("It's a tie!")

elif user_choice == "Rock" and computer_choice == "Scissors":

    print("You win!")

elif user_choice == "Paper" and computer_choice == "Rock":

    print("You win!")

elif user_choice == "Scissors" and computer_choice == "Paper":

    print("You win!")

elif user_choice == "Scissors" and computer_choice == "Rock":

    print("Computer wins!")

elif user_choice == "Rock" and computer_choice == "Paper":

    print("Computer wins!")

else:

    print("Computer wins!")

