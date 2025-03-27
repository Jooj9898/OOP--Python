#Author: Justin McGarr, C23421344

#Program Description: The program simulates a player betting on a game of Cho-Han, which involves rolling two dice and
#guessing if the answer will be "Cho" (even) or "Odd" and gaining or losing money on their bets. It heavily relies on the use
#of classes, class inheritance and functions within classes.

#Date: 3/12/2024

import random

##creating the class GameParticipant
class GameParticipant(object):
    #constructor to assign all its attributes
    def __init__(self,player_no=1,balance= 0):
        self.player_no = player_no
        self.balance = balance

    #constructor for updating the attributes
    def __str__(self):
        GameParticipant_info = f"Name: {self._player_no}\n"
        GameParticipant_info += f"Balance: {self.balance}\n"

        return GameParticipant_info

#creating the player class, which inherits attributes from the GameParticipant such as balance etc
class Player(GameParticipant):
    #adding the username attribute
    def __init__(self,player_no,balance,username):
        #calling game participant to give the player the same attributes as game participant
        GameParticipant.__init__(self,player_no,balance)
        self.username = username

    #defining the function to bet
    def bets(self,guess,money,dice):
        #the guess and money are both parameters we will add when calling
        self.guess = guess
        self.money = money
        #while loop is to ensure that the user cant bet more money than they have
        while money <= self.balance:
            #dice.roll_dice() returns cho or han depending on its outcome, this checks to see if the guess user has entered
            #is the same as the return of "cho" or "han" aka if they won
            if guess == dice.roll_dice():
                #printing the outcome and updating the balance as well as printing the new balance
                print("The player has won!")
                updated_balance = self.balance + (self.money *2)
                print(f"Updated balance: {updated_balance}")
                return updated_balance
            #opposite to check if the user has lost
            else:
                #printing the outcome and updating the balance as well as printing the new balance
                print("The player lost :(")
                updated_balance = self.balance - money
                print(f"Updated balance: {updated_balance}")
                return updated_balance
        #these are outside the while clause, so they print if whatever the user entered doesnt meet our standards, tells them their balance isnt high enough
        print("You dont have enough money to bet this much!")
        print(f"Your balance is: {self.balance}\n")

#creating the class DiceCup to hold the two die
class DiceCup(object):
    #defining functino to assign the attributes to the instance of the class
    def __init__(self,dice1=0,dice2=0,sum_dice = 0):
        self.dice1 = dice1
        self.dice2 = dice2
        self.sum_dice = sum_dice
    #defining our function to roll the dice, which is passed into bets
    def roll_dice(self):
        #each dice represents the roll, so we assign a random number between 1-6 to the dice/roll
        self.dice1 = random.randint(1,6)
        self.dice2 = random.randint(1,6)
        #sum of the dice is both rolls added together
        self.sum_dice = (self.dice1 + self.dice2)
        #if the sum is even, return cho
        if self.sum_dice % 2 == 0:
            return "cho"
        #if the sum is odd, return han
        else:
            return "han"
#creating a player instance "Susie"
Player1 = Player(1,50,"Susie")
#creating a dice instance, which we can also use to pass to bets
dice = DiceCup()

#this print ensures that the user knows how much they have and to enter an amount more than that
print(f"Your balance is: {Player1.balance}, you must bet an amount less than or equal to your balance!")

#we call the bets function and make the parameters user inputs, so the user can dynamically choose their answer and how much they are betting
#so now, we play the game with player1 'Susie!'
Player1.bets(input("Please enter the guess if its cho or han:"),int(input("Please enter how much money you want to bet:")),dice)






