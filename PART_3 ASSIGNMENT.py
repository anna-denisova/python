#Part 3 - Coding

#................................................................................................

# 1 - Write a program that stores the slope of a line (m = 3)
# and the yint of a line (b = 2) and displays the line in 
# slope intercept form.

m = 3 #slope
b = 2 #y-int

print(f"Slope intercept form for m = {m}, b = {b}: y = {m}x + {b}") #print slope-intercept form (y = mx+b)

#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#BONUS Q - try to convert to standard form using formulas 

#standard form - Ax + By + C  = 0
#ASSUMING m and b are whole numbers
#y = mx+b -> ax + by + c = 0
#way of doing this - keep mx+b while carrying over the y 

A = m #solve for coefficient in Ax
B = 1 #coefficient for y
C = b #solve for C

B = -1*B #Carry over B

#A cannot be negative so check: 
if(A < 0):
    #if a is negative, multiply equation by neg 1
    A *= -1
    B *= -1
    C *= -1

print(f"Standard form: {A}x", end = "") #end = makes sure that a newline isnt added
#check if number is negative OR if coefficient is 1 for formatting:

if(B<0): #for B
    if(B == -1):
      print("-y", end = "") #instead of "- 1y"
    else:
      print(B, end = "") #"-By"
else:
    if(B == 1):
      print(f"+y", end + "") # instead of "+ 1y"
    else:
      print(f"+{B}", end = "")
      
if(C<0): #for C, no need to check if C == 1 because there is no var after it
    print(C, end = "")
else:
    print(f"+{C}", end = "")

print("=0") # = 0 end of equation

#................................................................................................

# 2 - Write a program that has the bases of a trapezoid (a = 4 and b = 6) and the 
# height of a trapezoid (h=3) and calculates the area. 

#area of a trapezoid = ((b1+b2)/2)*h

a = 4 #base 
b = 6 #base
h = 3 #height
area = ((a+b)/2)*h; #area formula 

print(f"Area of a trapezoid with a = {a}, b = {b}, and h = {h}: {area}") #print area 

#................................................................................................

# 3 - Write a program that converts degrees Celsius (56 degrees) 
# to degrees Fahrenheit

#Formula : degrees celsius * (9/5) + 32 = degrees fahrenheit

c = 56 #celsius
f = c*(9/5)+32 #fahrenheit

print(f"{c} degrees celsius = {f} degrees fahrenheit") #print conversion

#................................................................................................

# 4 - Write a program that converts 3 days into an equivalent amount of 
# time in seconds

#1 day = 86400 seconds 

d = 3 #number of days
s = d*86400 #number of seconds in d days (60*60*24)

print(f"{d} days = {s} seconds") #print conversion

#................................................................................................
