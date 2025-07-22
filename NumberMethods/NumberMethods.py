#Number Methods In Python 
#https://app.eraser.io/workspace/GAxdlLIVgYAFpJf17bM1?origin=share

#Integors

a = 1 ;
b = 123456789 ;
c = -987654321 ;

print(type(a)) ;
print(type(b)) ;
print(type(c)) ;

#Floating Point Number

d = 1.1 ;
e = 1.0 ;
f = -35.457 ;

print(type(d)) ;
print(type(e)) ;
print(type(f)) ;

#Float can also be scientific numbers with an "e" to indicate the power of 10.

x = 23e45 ;
y = 12E4 ;
z = -87.7e237 ;

print(type(x)) ;
print(type(y)) ;
print(type(z)) ;

#Complex Number

m = 3 + 5j ;
n = -4j ;
o = 4j ;

print(type(m)) ;
print(type(n)) ;
print(type(o)) ;


#Coversion

num1  = 1 ; #int
num2 = 22.45 ; #float
num3 = 5j ; #complex

#Convert From int To float
num4 = float(num1);
print(num4) ;
print(type(num4)) ;

#Convert From float To integer
num5 = int(num2);
print(num5) ;
print(type(num5)) ;

#Convert From int To complex
num6 = complex(num1);
print(num6) ;
print(type(num6)) ;

#Import the random module, and display a random number from 1 to 9:

import random ;

print(random.randrange(1,10))