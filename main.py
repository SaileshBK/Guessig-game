import numpy as np


def found_row_col(First_Matrix,x):
  length_row = len(First_Matrix)
  length_col = len(First_Matrix[0])
  
  for n in range(length_row):
    for m in range(length_col):
      if(First_Matrix[n][m] == int(x)):
        found_row =n+1
        found_col =m+1
  
  if ((found_row ==1) and (found_col in range(1,5))):
      z=0
      y=0
      q= range(1,5)
  
  elif ((found_row ==2) and (found_col in range(1,5))):
      z=1
      y=0
      q= range(1,5)
  
  elif ((found_row ==3) and (found_col in range(1,5))):
      z=2
      y=0
      q= range(1,5)
  else:
    z=3
    y=0
    q=range(1,5)
       
  for i in q:
    if i==found_col:
      r_ow = np.delete(First_Matrix, z, 0)
      New_Matrix = np.delete(r_ow, y, 1)
      
    y=y+1

  return New_Matrix
  

def main():
  First_Matrix = np.arange(1, 17).reshape(4, 4)
  print(First_Matrix)
  print("\n")
  x = input("Please choose a number :")

  print(found_row_col(First_Matrix,x))

  x = input("Please choose a number :")
    
  length_row = len(c_ol)
  length_col = len(c_ol[0])
  
  for n in range(length_row):
    for m in range(length_col):
      if(c_ol[n][m] == int(x)):
        found_row =n+1
        found_col =m+1
  
  if ((found_row ==1) and (found_col in range(1,4))):
      z=0
      y=0
      q= range(1,4)
  
  elif ((found_row ==2) and (found_col in range(1,4))):
      z=1
      y=0
      q= range(1,4)
  else:
    z=2
    y=0
    q=range(1,4)
       
  for i in q:
    if i==found_col:
      r_ow = np.delete(c_ol, z, 0)
      c_ol = np.delete(r_ow, y, 1)
      print(c_ol)
    y=y+1
  
  
  x = input("Please choose another number :")
    
  length_row = len(c_ol)
  length_col = len(c_ol[0])
  
  for n in range(length_row):
    for m in range(length_col):
      if(c_ol[n][m] == int(x)):
        found_row =n+1
        found_col =m+1
  
  if ((found_row ==1) and (found_col in range(1,3))):
    z=0
    y=0
    q= range(1,3)
  else:
    z=1
    y=0
    q= range(1,3)
  
       
  for i in q:
    if i==found_col:
      r_ow = np.delete(c_ol, z, 0)
      c_ol = np.delete(r_ow, y, 1)
      print(c_ol)
    y=y+1


if __name__=="__main__":
  main()