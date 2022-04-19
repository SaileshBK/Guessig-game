import numpy as np

a = np.arange(1, 17).reshape(4, 4)
print(a)

print("\n")
x = input("Please choose a number :")

# z=0
# y=0
# for i in range(1,5):
#   if i==int(x):
#     r_ow = np.delete(a, z, 0)
#     c_ol = np.delete(r_ow, y, 1)
#     print(c_ol)
#   y=y+1

# z=1
# y=0
# for i in range(5,9):
#   if i==int(x):
#     r_ow = np.delete(a, z, 0)
#     c_ol = np.delete(r_ow, y, 1)
#     print(c_ol)
#   y=y+1

# z=2
# y=0
# for i in range(9,13):
#   if i==int(x):
#     r_ow = np.delete(a, z, 0)
#     c_ol = np.delete(r_ow, y, 1)
#     print(c_ol)
#   y=y+1

# z=3
# y=0
# for i in range(13,17):
#   if i==int(x):
#     r_ow = np.delete(a, z, 0)
#     c_ol = np.delete(r_ow, y, 1)
#     print(c_ol)
#   y=y+1

   
  
while True:
  
  if int(x) in range(1,5):
    z=0
    y=0
    q= range(1,5)
  elif int(x) in range(5,9):
    z=1
    y=0
    q=range(5,9)
  elif int(x) in range(9,13):
    z=2
    y=0
    q=range(9,13)
  else:
    z=3
    y=0
    q=range(13,17)
  
  for i in q:
    if i==int(x):
      r_ow = np.delete(a, z, 0)
      c_ol = np.delete(r_ow, y, 1)
      print(c_ol)
      print(len(c_ol))
    y=y+1

  if len(c_ol)==1:
    break
  x = input("Please choose a number :")
  a= c_ol
  









  

      
# elif int(x)==2:
#   a_del = np.delete(a, 0, 0)
#   b_del = np.delete(a_del,1,1)
#   print(b_del)

# elif int(x)==3:
#   a_del = np.delete(a, 0, 0)
#   b_del = np.delete(a_del,2,1)
#   print(b_del)

# elif int(x)==4:
#   a_del = np.delete(a, 0, 0)
#   b_del = np.delete(a_del,3,1)
#   print(b_del)

# elif int(x)==5:
#   a_del = np.delete(a, 1, 0)
#   b_del = np.delete(a_del,0,1)
#   print(b_del)

# elif int(x)==6:
#   a_del = np.delete(a, 1, 0)
#   b_del = np.delete(a_del,1,1)
#   print(b_del)

# elif int(x)==7:
#   a_del = np.delete(a, 1, 0)
#   b_del = np.delete(a_del,2,1)
#   print(b_del)

# elif int(x)==8:
#   a_del = np.delete(a, 1, 0)
#   b_del = np.delete(a_del,3,1)
#   print(b_del)
