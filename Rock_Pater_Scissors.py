#This is super easy programer for Beginners to start 
#you git clone this and develop it from here...
#You can do User Validation, make it more dynamic and more 

import random

class Rock_Pater_Scissors:
    def __init__(self,user,computer=None) -> None:
        self.user = user
        self.computer = computer
        #Give Computer A Choice
        self.computer = random.choice(['r','p','s'])

    def logic(self):
        if self.user == self.computer:
            return 'It\'s a tie'
        
        def is_win(user,computer):
            if (user == 'r' and computer == 's') or (user =='s' and computer =='p')\
                or (user == 'p' and computer == 'r'):
                return True
            
        if is_win(self.user,self.computer):
            return "You Win, Congrats!!!"
        
        return 'You Lose Try Agin'


def main():
    user = str(input("Enter Ethir Rock(r) or Scissor(s) or Paper(p): "))
    test = Rock_Pater_Scissors(user)
    test = test.logic()
    print(test)



if __name__ == '__main__':
    main()


