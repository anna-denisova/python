#Bonus Question 

year = int(input("Enter the year: ")) #gets whatever user types 

#calculations
a = int(year%19)
b = int(year/100)
c = int(year%100)
d = int(b/4)
e = int(b%4)
f = int((8*b + 13)/25)
g = int((19*a+b-d-f+15)%30)
h = int((a+11*g)/319)
i = int(c/4)
j = int(c%4)
m = int((2*e+2*i-g-h-j+32)%7)
month = int((g-h+m+90)/25)
day = int((g-h+m+month+19)%32)

#output
print(f"Easter will be on:\n\tMonth(numbers):{month}\n\tDay:{day}")

#I'm surprised all these calculations actually give the correct date. 
#This is really cool 
