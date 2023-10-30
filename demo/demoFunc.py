## function to add two numbers
def addNumbers(number1, number2):
    '''provide 2 numbers as parameters.
      function returns total'''
    return number1 + number2

## function to subtract two numbers
def subNumbers(number1, number2):
    '''provide 2 numbers as parameters.
      function subtracts second parameter from first parameters'''
    return number1 - number2


## function to glob files in a directory
import glob
def getFiles(path):
    '''provide directory and file pattern as parameters.
      function returns list of files matching pattern'''
    return glob.glob(path)