import numpy as np


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
  

def main():
  Main_matrix = np.arange(1, 17).reshape(4, 4)
  print(Main_matrix)
  print("\n")
  
  for i in range(3):
    x = input("Please choose a number :")
    First_matrix = New_Matrix(Main_matrix,x)
    print(First_matrix)
    Main_matrix = First_matrix
    


if __name__=="__main__":
  main()