# Lab 1: 2D Transformation 

from decimal import *

# public var (window coordinates)
xmin = 10
xmax = 260
ymin = 10
ymax = 160

#########################
#4bit
def firstbit(y,ymax):
  #test y > ymax
  first = 0
  if y > ymax:
    first = 1
  return first
def secondbit(y,ymin):
  #test y < ymin
  second = 0
  if y < ymin:
    second = 1
  return second
def thirdbit(x,xmax):
  #test x > xmax
  third = 0
  if x > xmax:
    third = 1
  return third
def fourthbit(x,xmin):
  #test x < xmin
  fourth = 0
  if x < xmin:
    fourth = 1
  return fourth
#########################

def lab2(x1,y1,x2,y2): # def function to make it easy to test
  # y = mx + p
  # x = (y - p)/m   
  m = (y2 - y1)/(x2 - x1)
  p = y2 - (m * x2)
  #4 bit 
  while True: # loop until visible or invisible (prevent clipping candidate without visible line segment in the window)
    first1 = firstbit(y1,ymax)
    second1 = secondbit(y1,ymin)
    third1 = thirdbit(x1,xmax)
    fourth1 = fourthbit(x1,xmin)
    print(first1,second1,third1,fourth1)
    bit1 = [first1,second1,third1,fourth1] # 4 bits from 1st point

    first2 = firstbit(y2,ymax)
    second2 = secondbit(y2,ymin)
    third2 = thirdbit(x2,xmax)
    fourth2 = fourthbit(x2,xmin)
    print(first2,second2,third2,fourth2)
    bit2 = [first2,second2,third2,fourth2] # 4 bits from 2nd point

  #########################
  # check clipping catagory 
  # status = 0      : visible
  # 0 < status < 10 : clipping candidate
  # status >= 10    : Invisible

    status = 0
    for n in range(0,4):
      if bit1[n] == 0 and bit2[n] == 0:
        status = status + 0 
      elif bit1[n] == 0 or bit2[n] == 0:
        status = status + 1 
      elif bit1[n] == 1 and bit2[n] == 1:
        status = status + 10 
  #########################
    if status >= 10:
      print("Invisible")
      break
    elif status == 0:
      print("Visible")
      print("("+'%.3f'% x1 +", "+'%.3f'% y1 +")") #print x1,y1 (in 3 digits after decimal) 
      print("("+'%.3f'% x2 +", "+'%.3f'% y2 +")") #print x1,y1 (in 3 digits after decimal) 
      break

    elif status > 0 and status < 10:
      print("Clipping Candidate")
      if bit1[0] == 1 or bit2[0] == 1: # y > ymax
        if bit1[0] == 1:
          x1 = x1 + ((ymax-y1)/m)
          y1 = ymax
          print("("+'%.3f'% x1 +", "+'%.3f'% y1 +")") #print x1,y1 (in 3 digits after decimal) 
          print("("+'%.3f'% x2 +", "+'%.3f'% y2 +")") #print x1,y1 (in 3 digits after decimal) 
        else:
          x2 = x2 + ((ymax-y2)/m)
          y2 = ymax
          print("("+'%.3f'% x1 +", "+'%.3f'% y1 +")") #print x1,y1 (in 3 digits after decimal) 
          print("("+'%.3f'% x2 +", "+'%.3f'% y2 +")") #print x1,y1 (in 3 digits after decimal) 
      elif bit1[1] == 1 or bit2[1] == 1: # y < ymin  
        if bit1[1] == 1:
          x1 = x1 + ((ymin-y1)/m)
          y1 = ymin
          print("("+'%.3f'% x1 +", "+'%.3f'% y1 +")") #print x1,y1 (in 3 digits after decimal) 
          print("("+'%.3f'% x2 +", "+'%.3f'% y2 +")") #print x1,y1 (in 3 digits after decimal) 
        else:
          x2 = x2 + ((ymin-y2)/m)     
          y2 = ymin
          print("("+'%.3f'% x1 +", "+'%.3f'% y1 +")") #print x1,y1 (in 3 digits after decimal) 
          print("("+'%.3f'% x2 +", "+'%.3f'% y2 +")") #print x1,y1 (in 3 digits after decimal) 
      elif bit1[2] == 1 or bit2[2] == 1: # x > xmax
        if bit1[2] == 1:
          y1 = y1 + (m*(xmax-x1))
          x1 = xmax
          print("("+'%.3f'% x1 +", "+'%.3f'% y1 +")") #print x1,y1 (in 3 digits after decimal) 
          print("("+'%.3f'% x2 +", "+'%.3f'% y2 +")") #print x1,y1 (in 3 digits after decimal) 
        else:
          y2 = y2 + (m*(xmax-x2)) 
          x2 = xmax 
          print("("+'%.3f'% x1 +", "+'%.3f'% y1 +")") #print x1,y1 (in 3 digits after decimal) 
          print("("+'%.3f'% x2 +", "+'%.3f'% y2 +")") #print x1,y1 (in 3 digits after decimal) 
      elif bit1[3] == 1 or bit2[3] == 1: # x < xmin    
        if bit1[3] == 1:
          y1 = y1 + (m*(xmin-x1))
          x1 = xmin 
          print("("+'%.3f'% x1 +", "+'%.3f'% y1 +")") #print x1,y1 (in 3 digits after decimal) 
          print("("+'%.3f'% x2 +", "+'%.3f'% y2 +")") #print x1,y1 (in 3 digits after decimal) 
        else:
          y2 = y2 + (m*(xmin-x2))
          x2 = xmin       
          print("("+'%.3f'% x1 +", "+'%.3f'% y1 +")") #print x1,y1 (in 3 digits after decimal) 
          print("("+'%.3f'% x2 +", "+'%.3f'% y2 +")") #print x1,y1 (in 3 digits after decimal) 

inp = str(input())
sp = inp.split()
x1 = int(sp[0])
y1 = int(sp[1])
x2 = int(sp[2])
y2 = int(sp[3])
lab2(x1,y1,x2,y2)