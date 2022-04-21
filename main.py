"""This is a python 4*4 grid prediction. First you have to pick a number. Now you can not pick any numbers on the same row and column of the last number you picked. For example, if you pick 1 , you next pick should not be 2,3,4,5,9,13. The process repeats """

#The magic number is 34.


import numpy as np
from colorama import Fore, Style
# importing numpy and colorama library to use matrix and text color.

#This New_Matrix takes the initial Matrix with user input and return the new matrix after deleting the correct row and column of old matrix.
def New_Matrix(First_Matrix,x):
  length_row = len(First_Matrix) # row length of our matrix
  length_col = len(First_Matrix[0]) # column length of our matrix

  if length_row == 4:  # This if statements provides us a correct range to use in the process of deleting rows and columns.
    Matrix_range = range(1,5)
  elif length_row == 3:
    Matrix_range = range(1,4)
  else:
    Matrix_range = range(1,3)
    
  
  for n in range(length_row): # for loop to find the position of row and column to delete.
    for m in range(length_col):
      if(First_Matrix[n][m] == int(x)):
        found_row =n+1
        found_col =m+1
  #From here we compare the found row and column and initialize the necessary obj and axis to delete.
  if ((found_row ==1) and (found_col in Matrix_range)):
      z=0
      y=0
  
  elif ((found_row ==2) and (found_col in Matrix_range)):
      z=1
      y=0
  
  elif ((found_row ==3) and (found_col in Matrix_range)):
      z=2
      y=0
  else:
    z=3
    y=0
  #np.delete() takes three parameters. Input array,Row or column number and Axis to delete( Axis = 0-delete row, 1-delete column).
  for i in Matrix_range:
    if i==found_col:
      r_ow = np.delete(First_Matrix, z, 0)
      New_Matrix = np.delete(r_ow, y, 1)
      
    y=y+1

  return New_Matrix


def intro(Main_matrix):  # this function asked for the valid input and keep asking if the user input is invalid.

  choice = input("\nPlease choose a valid number from above : ")
  while (True):
    if choice.strip().isdigit() and (int(choice) in Main_matrix): # checks if the user input is digit or not and falls within the matrix rage.
      First_matrix = New_Matrix(Main_matrix,choice)
      return First_matrix
    else:
      print("\nsorry not a valid option. Try again !\n")
      print(Main_matrix)
    choice = input("\nPlease choose a valid number from above : ")
        
  
# our main
def main():
  
  print("Hello , Lets play a Game.\n")
  print(Fore.GREEN +"--> Magic Number 34. <--") # here we made the text color to green using colorama.
  print(Style.RESET_ALL) # reseting the text color to default.
  print(Fore.BLUE +"Rules : \n 1) Below is a 4×4 Grid Prediction. pick a number.") # here we made the text color to blue using colorama.
  print(" 2) However, your next number should not be in the same row and column of last number picked. ")
  print(" 3) Again, your next number should be in a different row and different column from the previous two numbers. \n ")
  print(Style.RESET_ALL)


  
  Main_matrix = np.arange(1, 17).reshape(4, 4) # initial 4*4 matrix
  print(Main_matrix)
  
  First_step= intro(Main_matrix) # first step
  print(First_step)
  
  Second_step = intro(First_step) #secod step
  print(Second_step)
  
  Third_step = intro(Second_step) #third step

  print("Remaining number in matrix is :",Third_step)

  print(Fore.BLUE +"\nFinally, Add all your inputs, including the last remaining number in the matrix." )
  print("\nNow, compare that sum to the Magic Number." )
  print("Thank You!")
  print(Style.RESET_ALL)


if __name__=="__main__":
  main()