#Assignment 3


class MarblesBoard():
    """MarbleBoard class represents a game that takes inputs of N marbles
    and allows two possible moves -- switch or rotate
    """
    
    def __init__(self,a):
        self.__a = list(a)
    
    """--str-- method to return a list of N marbles"""
    def __str__(self):
        return ' '.join(map(str, self.__a))

    def __repr__(self):
        return 'MarblesBoard(a=%s)' % (self.__a)
    
    """return the current list of N marbles"""
    def getList(self):
        return self.__a
    
    """switch the first two values in the list"""    
    def switch(self):
        self.__a[0],self.__a[1]=self.__a[1],self.__a[0]
    
    """rotate to move up the list"""    
    def rotate(self):
        self.__a.append(self.__a.pop(0))
    
    """check if the list is already sorted"""
    def is_solved(self):
        i=0
        for i in range(len(self.__a)-1):
            if self.__a[i] > self.__a[i+1]:
                return False
            i+=1
        return True

"""Solver class accepts a marble game as an input and solve the game in a finite step"""
class Solver():
    
    def __init__(self, marbles_board):
        self.marbles_board = marbles_board

    def __str__(self):
        return ' '.join(map(str, self.marbles_board))  
    
    def solve(self):
        """print the starting point of the game"""
        print(self.marbles_board)
        
        #variable step to keep track of step.
        step = 0

        #find the minimum number of the list.
        min_number=min(self.marbles_board.getList())
        
        #repeat the rules of the game until the list is sorted. 
        while (self.marbles_board.is_solved() is False):
            
            #if the first two elements in the list doesn't contain the minimum number, check if they should be switched.
            if (self.marbles_board.getList()[0]!=min_number and self.marbles_board.getList()[1]!=min_number):
                if (self.marbles_board.getList()[0] > self.marbles_board.getList()[1]):
                    self.marbles_board.switch()
                    print(self.marbles_board)
                    step+=1     
            
            #keep rotating the list
            self.marbles_board.rotate()
            step+=1
            print(self.marbles_board)
        
        # return the total steps
        return print("total steps: "+str(step))       
                                 
#request input from users with a comma as a separator
d = input("Enter Numbers: ").split(",")

#convert the input into a list of intergers.
input_marbles = [int(d[i]) for i in range(len(d))]

#initialize an instance of a MarblesBoard given the input
marbles = MarblesBoard(input_marbles)

#initialize a player of the game given a marble board initialized above.
player = Solver(marbles)

#player to solve the game
player.solve()


"""
**********************Answer to the Big O question**********************
The Big O running time for this program is O(n^2) time.
Compute this by initializing a board game with a large N numbers in a
completely reversed order

"""

x = list(range(10))
y=x[::-1]

"""
marbles_big_o = MarblesBoard(y)
player = Solver(marbles_big_o)
player.solve()
"""





