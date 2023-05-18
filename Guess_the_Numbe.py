#This is super easy programer for Beginners to start 
#you git clone this and project and start building and developing on it...

import random

class Guess_the_Numbe:
    def __init__(self, user_input) -> None:
        self.user_input = user_input
    def show_num(self):
        return self.user_input
    def logic(self):
        random_num = random.randint(1,self.user_input)
        guess = 0
        while guess != random_num:
            guess = int(input(f"Guess a number bewteen 1 to {self.user_input}: "))
            if guess > random_num:
                print('Sorry, Too High.')
            elif guess < random_num:
                print('Sorry Too Low.')
        print(f"Congrats You get the right Number ({random_num})")
    def computer_ans(self):
        #Build This One
        ... 

def main():
    #Get user_input
    USER_START = int(input("Enter a number to start: "))
    test = Guess_the_Numbe(USER_START)
    #Start The Logic 
    logic = test.logic()


if __name__ == '__main__':
    main()

#Inspeard by  12 Beginner Python Projects - Coding Course 
# Link for the video (https://www.youtube.com/watch?v=8ext9G7xspg&ab_channel=freeCodeCamp.org)