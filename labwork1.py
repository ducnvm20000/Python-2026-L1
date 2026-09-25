#ex1
radius = float( input("Enter circle radius? "))
circle_area = 3.14 * radius**2
print("Circle area = ", circle_area)

#ex2
celcius = float( input("Enter the temperature in Celcius? "))
fahrenheit = celcius*1.8 + 32
print( celcius, '(C) =', fahrenheit, '(F)')

#ex3
n = int(input("Enter a number? "))
if (n <= 1): 
    print( n, "is not prime")
else:
    prime = True
    for i in range (2, n):
        if n%i==0:
            prime = False
            break
    if prime:
        print(n, "is prime")
    else:    
        print (n, "is not prime")


#ex4
n = int(input("Enter number: "))
s = 0 #sum all divisors 
for i in range (1, n):
    if n % i ==0:
     s += i

if s == n:
   print( "Yes perfect")
else:
   print("No perfect")

#ex5
fav = ["red", "blue", "yellow", "green"]
color = input("Your color? ")
if color in fav:
    print("yo same!")
    print (f"position at {fav.index(color)}")
else:
    print("nonono")

#ex6
range1 = [str(i) for i in range (0, 7)]
print(",".join(range1))
range2 = [str(i) for i in range (1, 11, 3)]
print(",".join(range2))
range3 = [str(i) for i in range (5, 0, -1)]
print(",".join(range3))
range4 = [str(i) for i in range (6, -3, -2)]
print(",".join(range4))

#ex7
s = input("Enter string: ")
s1 = s.replace("$","")   
print(s1)

#ex8
def extract_even(l):
    return [i for i in l if i%2==0]
print(extract_even([1,4,5,-1,10]))

#ex9
def factorial(n):
    value = 1
    for i in range (1, n+1):
            value = value * i
    return value
print (factorial(5))

#ex10
def divs(n):
    out = []
    for i in range (1, n+1):
        if n % i == 0:
            out += [i]
    return out
    
print (divs(120))

#ex11
import math
xa = int(input("xa "))
xb = int(input("xb ")) 
ya = int(input("ya "))
yb = int(input("yb "))
dist = math.sqrt((xa - ya)**2 + (xb-yb)**2)
print (dist)

#ex12
col = int(input("cols: "))
row = int(input("rows: "))
for i in range (row):
    for j in range (col):
        if i == 0 or i== row - 1 or j ==0 or j == col - 1:
            print ("* ", end="")
        else:
            print ("  ", end="")
    print()        
    
