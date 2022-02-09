
print("_______________________________________________")
print ("\033[1m" + "Day 1\n"+ "\033[0m") #Bolds string

#.......................................................

print("\u0332".join("Question 1 ")) #Underlines string

#An Syntax Error Full Program
# This is my program (Fixed)
y = 2
z = 1
x = y * 3
w = y 

print("The result is")
print(x)
print(w)

print("\n") 

#.......................................................

print("\u0332".join("Question 2 ")) #Underlines string

var_1, var_2 = 4, "Math Rules"
print("Var 1:", var_1, "\nVar 2:", var_2)

print("\n") 

#.......................................................

print("\u0332".join("Question 3 ")) #Underlines string

x, y = 5, 6
print(f"{x} + {y} = {x+y}")

print("\n") 

#.......................................................

print("\n_______________________________________________")
print ("\033[1m" + "Day 2\n"+ "\033[0m") #Bolds string

#.......................................................

print("\u0332".join("Question 1 ")) #Underlines string

height, base, area = 5.6, 10.5, 0
area = 0.5*base+height
print(f"Area: {area}")

print("\n") 

#.......................................................

print("\u0332".join("Question 2 ")) #Underlines string

l1, l2, l3 = 3, 5, 6
print(f"Perimeter: {l1+l2+l3}")

print("\n") 

#.......................................................

print("\u0332".join("Question 3 ")) #Underlines string

d, r, t = 0, 86, 8
print(f"Distance (in km): {r*t}")

print("\n") 

#.......................................................

print("\n_______________________________________________")
print ("\033[1m" + "Day 3\n"+ "\033[0m") #Bolds string

#.......................................................

print("\u0332".join("Question 1 ")) #Underlines string

a, b, c, d = 3, 7, 2, 9
print(f"Average of {a, b, c, d}:\n->{(a+b+c+d)/2}")

print("\n") 

#.......................................................

print("\u0332".join("Question 2 ")) #Underlines string

r = 5
#circumfrence = 2*pi*r
#area = pi*r*squared
print(f"Circumfrence of circle with radius {r} : {2*3.14*r}")
print(f"Area of circle with radius {r} : {3.14*r*r}")

print("\n") 

#.......................................................

print("\n_______________________________________________")
print ("\033[1m" + "Day 5\n"+ "\033[0m") #Bolds string

#.......................................................

print("\u0332".join("Question 1 ")) #Underlines string

x = 15
if(15%5 == 0):
    print(x,"is divisible by 5")
if(15%5 != 0):
    print(x, "is not divisible by 5")


print("\n") 

#.......................................................

print("\u0332".join("Question 2 ")) #Underlines string

a = 5 #random numbers between 1-100
b = 90

print(f"Values of a and b: \na:{a}\nb:{b}")
if a > 50 and b > 50:
    print("Both a and b are larger than 50")
elif a>50 and b<50:
    print("Only a is larger than 50. B is less than 50")
elif a<50 and b>50:
    print("Only b is larger than 50. A is less than 50")
elif a<50 and b<50:
    print("a and b are both smaller than 50")


print("\n") 

#.......................................................


