n = int(input("Enter the number : "))

# Half Pyramid
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print() # or print("") same

# Inverted Half Pyramid
print("\n")
for i in range(n):
    for j in range(i,n):
        print("*",end="")
    print()

# Full Pyramid
print("\n")

for i in range(n):
    for j in range(-n,-i):
        print(" ",end="")
    for k in range(i+1):
        print("*",end=" ")
    print()

# Inverted Full Pyramid
print("\n")

for i in range(n):
    for j in range(i):
        print(" ",end="")
    for k in range(i,n):
        print("*",end=" ")
    print()

# after 180 degree rotation (right angle)
print("\n")

k = 2 * n - 2
for i in range(n):
    for j in range(k):
        print(end=" ")
    k = k - 2
    for m in range(i+1):
        print("*", end=" ")
    print("\r")
    
# Pattern of Num
print("\n")

num = 1
for i in range(n):
    for j in range(i+1):
        print(num,end=" ")
        num = num + 1
    print()    # print("New")

# Inverted Num 
print("\n")

num = 1
for i in range(n):
    for j in range(n,i,-1):
        print(num,end=" ")
        num = num + 1
    print()

# Pattern of Num in different style 1 12 123
print("\n")

num = 1
for i in range(n):
    for j in range(i+1):
        print(num,end=" ")
        num = num + 1
    num = 1
    print()
    
# Inverted Num 123 12 1
print("\n")

for i in range(n):
    num = 1
    for j in range(n,i,-1):
        print(num,end=" ")
        num = num + 1
    print()

# Inverted Half Pyramid Num

min = 10
for i in range(n):
    count = 0
    for j in range(min):
        print(end=" ")
    min = min - 2
    for k in range(i+1):
        count = count + 1
    num = count
    for m in range(i+1):
        print(num,end=" ")
        num = num - 1
    print()

# Inverted Half Pyramid Num
print("\n")

for i in range(n):
    min = 10
    count = 0
    # for j in range(min):
        # print(end="")
    min = min - 2
    for k in range(i+1):
        count = count + 1
    num = count
    for m in range(i+1):
        print(num,end=" ")
        num = num - 1
    print()
    
# Simple Pyramid pattern
print("\n")

list = []
for i in range(1,n+1):
    list.append("* " * i)
print("\n".join(list))

# simple pattern 12345 12345 12345
print("\n")

for i in range(1,n):
    for j in range(1,n):
        print(j,end="")
    print()

# simple pattern 1111 2222 3333 4444
print("\n")

for i in range(1,n):
    for j in range(1,n):
        print(i,end="")
    print()
    
# simple pattern **** **** ****
print("\n")

for i in range(1,n):
    for j in range(1,n):
        print("*",end="")
    print()

# simple pattern 1010 1010 1010
print("\n")

for i in range(1,n):
    for j in range(1,n):
        print(j%2,end="")
    print()

# simple pattern abcd abcd abcd
print("\n")

for i in range(ord('a'), ord('e')+1):
    for j in range(ord('a'), ord('e')+1):
        print(chr(j), end="")
    print()
    
# simple pattern aaaa bbbb cccc
print("\n")

for i in range(ord('a'), ord('e')+1):
    for j in range(ord('a'), ord('e')+1):
        print(chr(i),end="")
    print()

# simple pattern dddd cccc bbbb aaaa
print("\n")

for i in range(ord('e'), ord('a')-1,-1):
    for j in range(ord('e'), ord('a')-1,-1):
        print(chr(i), end="")
    print()

# simple pattern dcba dcba dcba dcba
print("\n")

for i in range(ord('e'), ord('a')-1,-1):
    for j in range(ord('e'), ord('a')-1,-1):
        print(chr(j), end="")
    print()

# simple pattern 1111 0000 1111 0000
print("\n")

for i in range(1,n):
    for j in range(1,n):
        print(i%2, end="")
    print()

# simple pattern 4321 4321 4321 4321
print("\n")

for i in range(n,0,-1):
    for j in range(n,0,-1):
        print(j, end="")
    print()
    
# simple pattern 4444 3333 2222 1111
print("\n")

for i in range(n,0,-1):
    for j in range(n,0,-1):
        print(i, end="")
    print()
    
# Hollow Square Pattern
print("\n")

for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

# Hollow triangle pattern
print("\n")

for i in range(1,n+1):
    for j in range(i):
        if j==0 or j==i-1:
            print("*",end="")
        else:
            if i != n:
                print(" ",end="")
            else:
                print("*",end="")
    print()

# Hollow Pyramid Pattern
print("\n")

for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(2 * (i+1)):
        if k==0 or k==2*i:
            print("*", end="")
        else:
            if i==n-1:
                print("*", end="")
            else:
                print(" ",end="")
    print()
    
# Diamond Start Pattern
print("\n")

for i in range(n):
    for j in range(-n,-i):
        print(" ",end="")
    for k in range(i+1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for k in range(i,n):
        print("*",end=" ")
    print()
    