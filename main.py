import numpy as np
a = np.arange(1,17).reshape(4, 4)
print(a)

print("\n")
x= input("Please choose a number :")
if int(x)==1:
  a_del = np.delete(a, 0, 0)
  b_del = np.delete(a_del,0,1)
  print(b_del)
  
  x= input("Please choose a number :")
  if int(x)==6:
    a_del = np.delete(b_del, 0, 0)
    b_del = np.delete(a_del,0,1)
    print(b_del)

    x= input("Please choose a number :")
    if int(x)==11:
      a_del = np.delete(b_del, 0, 0)
      b_del = np.delete(a_del,0,1)
      print(b_del)

    
    

  

