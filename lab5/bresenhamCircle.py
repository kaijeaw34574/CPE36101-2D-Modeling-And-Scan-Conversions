# Lab 5: Bresenham's Circle Algorithm

def BresenhemCircle(x, y ,r):
    xc = 0
    yc = r
    h = 1 - r
    dU = 0
    dD = 0
    p1, p2, p3, p4, p5, p6, p7, p8 = [],[],[],[],[],[],[],[]
    result = []
    temp = []
    temp2 = []
    temp2.append((h, xc, yc))

    while (xc <= yc):
        p1.append((xc + x, yc + y))   # (x,y) P1
        p2.append((yc + x, xc + y))   # (y,x) P2
        p7.append((yc + x, -xc + y))  # (y,-x) P7
        p8.append((xc + x, -yc + y))  # (x,-y) P8 
        p5.append((-xc + x, -yc + y)) # (-x,-y) P5
        p6.append((-yc + x, -xc + y)) # (-y,-x) P6
        p3.append((-yc + x, xc + y))  # (-y,x) P3
        p4.append((-xc + x, yc + y))  # (-x,y) P4 
        if h < 0:
            dU = (2 * xc) + 3
            h = h + dU
        else:
            dD = (2 * (xc - yc)) + 5
            h = h + dD
            yc -= 1
        xc += 1
        temp2.append((h, xc, yc))
    
    p2.reverse()
    p4.reverse()
    p6.reverse()
    p8.reverse()
    result.extend(p1)
    result.extend(p2)
    result.extend(p7)
    result.extend(p8)
    result.extend(p5)
    result.extend(p6)
    result.extend(p3)
    result.extend(p4)

    for i in result:
        if i not in temp:
            temp.append(i)
    return temp, temp2, p1, p2, p3, p4, p5, p6, p7, p8

# Main function print list of all points
# for draw a circle by used Bresenham's Circle Algorithm
x, y, r = input('').split()
x, y, r = int(x), int(y), int(r)
s, v, p1, p2, p3, p4, p5, p6, p7, p8 = BresenhemCircle(x, y, r)
for i in s:
    print(i)