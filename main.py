import numpy as np

a = np.arange(1, 17).reshape(4, 4)
print(a)

print("\n")
x = input("Please choose a number :")
# if x == '1'or '2' or '3' or '4':
#     r_ow = np.delete(a, 0, 0)
#     n = 0
#     for i in range(1,5):
#         if i==int(x):
#             c_ol = np.delete(r_ow, n, 1)
#             print(c_ol)
#         n = n + 1



z=0
y=0
for i in range(1,5):
  if i==int(x):
    r_ow = np.delete(a, z, 0)
    c_ol = np.delete(r_ow, y, 1)
    print(c_ol)
  y=y+1

z=1
y=0
for i in range(5,9):
  if i==int(x):
    r_ow = np.delete(a, z, 0)
    c_ol = np.delete(r_ow, y, 1)
    print(c_ol)
  y=y+1
  
    
  


      





      
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
