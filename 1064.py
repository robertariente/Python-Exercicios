a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())

x=0
y=0

if a>=0:
  x=x+1
  y=y+a

if b>=0:
  x=x+1
  y=y+b

if c>=0:
  x=x+1
  y=y+c

if d>=0:
  x=x+1
  y=y+d

if e>=0:
  x=x+1
  y=y+e

if f>=0:
  x=x+1
  y=y+f

media=y/x

print("%d valores positivos"%x)
print("%.1f"%media)