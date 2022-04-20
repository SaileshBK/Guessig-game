import numpy as np
from colorama import Fore, Style

def New_Matrix(First_Matrix,x):
  length_row = len(First_Matrix)
  length_col = len(First_Matrix[0])

  if length_row == 4:
    Matrix_range = range(1,5)
  elif length_row == 3:
    Matrix_range = range(1,4)
  else:
    Matrix_range = range(1,3)
    
  
  for n in range(length_row):
    for m in range(length_col):
      if(First_Matrix[n][m] == int(x)):
        found_row =n+1
        found_col =m+1
  
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
       
  for i in Matrix_range:
    if i==found_col:
      r_ow = np.delete(First_Matrix, z, 0)
      New_Matrix = np.delete(r_ow, y, 1)
      
    y=y+1

  return New_Matrix


def intro(Main_matrix):

  choice = input("\nPlease choose a valid number from above : ")
  while (True):
    if choice.strip().isdigit() and (int(choice) in Main_matrix):
      First_matrix = New_Matrix(Main_matrix,choice)
      return First_matrix
    else:
      print("\nsorry not a valid option. Try again !\n")
      print(Main_matrix)
    choice = input("\nPlease choose a valid number from above : ")
        
  

def main():



  print("Hello , Lets play a Game.\n")
  
  print(Fore.GREEN +"--> First, remember number 34. <--")
  print(Style.RESET_ALL)
  
  print(Fore.BLUE +"Rules : \n 1) Below is a 4×4 Grid Prediction. pick a number.")
  print(" 2) However, your next number should not be in the same row and column of last number picked. ")
  print(" 3) Again, your next number should be in a different row and different column from the previous two numbers. \n ")
  print(Style.RESET_ALL)


  
  Main_matrix = np.arange(1, 17).reshape(4, 4)
  print(Main_matrix)
  
  First_step= intro(Main_matrix)
  print(First_step)
  
  Second_step = intro(First_step)
  print(Second_step)
  
  Third_step = intro(Second_step)
  print(Third_step)

  print(Fore.BLUE +"\nFinally, Add all your inputs, including the last remaining number in the matrix." )
  print("\nNow, compare that number to the number I told you to remember at the beginning of this game." )
  print("Thank You!")
  print(Style.RESET_ALL)


if __name__=="__main__":
  main()