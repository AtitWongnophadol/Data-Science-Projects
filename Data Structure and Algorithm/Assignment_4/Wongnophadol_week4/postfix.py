import operator #make use of operator module to perform arithmetic operations
import decimal #make use of decimal module to convert string to decimal

# class Empty to raise an exception code from the book "Data Structure and Algorithms in Python"
class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

# class ArrayStack code from chapter6.1 in the book "Data Structure and Algorithms in Python"
class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying stoarge."""
    
    def __init__(self):
        """Create an empty stack."""
        self._data=[]   # nonpublic list instance
        
    """--str-- method to return elements in Array"""
    def __str__(self):
        return ' '.join(map(str, self._data))
        
    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)
    
    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data)==0
    
    def push(self,e):
        """Add element e to the top of the stack."""
        self._data.append(e)    # new item stored at the end of list
        
    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        
        Raise Empty exception if the stack is empty.
        """
        
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    
    def pop(self):
        """Remove and return the element fomr the top of the stack (i.e., LIFO)
        
        Raise Empty exception if the stack is empty.
        """
        
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()     #remove last item from list
    
#function to perform calculation based on postfix notations

def postfix_calc(expr):

    operands = '+-*/' #allowable operands
    
    S = ArrayStack() #create a stack
    
    expr = expr.split(" ") #save string into a list, split by a space
    
    for c in range(len(expr)): #go over each element in the list
        
        if expr[c] not in operands:
        #If the element is number, add it to the stack
            S.push(expr[c])
            
        elif expr[c] in operands:
        #If the element is an operator, perform that operation given the latest two elements in the stack
        #Given stack is a LIFO, the last element in stack is popped as expression 2, followed by another pop for expression 1
            expr2 = decimal.Decimal(S.pop())
            expr1 = decimal.Decimal(S.pop())

            if expr[c]=='+':
                #if '+', then add expr2 to expr1, then push the result to the stack
                S.push(operator.add(expr1, expr2))
                
            elif expr[c]=='-':
                #if '-', then subtract expr2 from expr1, then push the result to the stack
                S.push(operator.sub(expr1, expr2))
                
            elif expr[c]=='*':
                #if '*', then multiply expr1 with expr1, then push the result to the stack
                S.push(operator.mul(expr1, expr2))
                
            elif expr[c]=='/':
                #if '/', then divide expr1 with expr2, then push the result to the stack
                S.push(operator.truediv(expr1, expr2))
    
    return S.pop() #pop the last element in the stack, which is the final outcome
 

# Specify output file path and filename
input_file_path = "/Users/plodium2000/Documents/All Documents/Profile/EM/Education/Berkeley/MIDS Program/Courses/Data Structure and Algorithm/1B_assignments_2016_11_10/Assignment_4/Wongnophadol_week4/input.txt"

# Specify output file path and filename
output_file_path = "/Users/plodium2000/Documents/All Documents/Profile/EM/Education/Berkeley/MIDS Program/Courses/Data Structure and Algorithm/1B_assignments_2016_11_10/Assignment_4/Wongnophadol_week4/output.txt"

# Read the input file and write out scrambled message of each line into the output file.
with open(input_file_path,'rt') as input_file, open(output_file_path,'wt') as output_file:
    for line in input_file:
        # Print statements to quickly test the accuracy of the program.
        print(line.rstrip())
        print(str(postfix_calc(line.rstrip()))+"\n")
        
        # Write out the scrambled messages to the output file.
        output_file.write(str(postfix_calc(line.rstrip()))+"\n")
    