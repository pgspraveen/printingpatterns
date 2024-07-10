#1
'''n=5
for i in  range(n):
    for j in range(n):
        if(j==0 or j==n-1):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()'''
#2
'''n=5
for i in  range(n):
    for j in range(n):
        if(i==n//2 or j==n//2):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()'''
#3
'''n=5
for i in  range(n):
    for j in range(n):
        if(i==j or i+j==n-1):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()'''

#4
'''n=5
for i in  range(n):
    for j in range(n):
        if(j==0 or i==0 or j==n-1 or i==n-1):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()'''
#5
'''n=5
for i in  range(n):
    for j in range(i+1):
        if(j==0 or i==n-1 or j==i):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()'''
#6
'''n=5
for i in  range(n):
    for j in range(i,n):
        if(j==i or i==0 or i==n-1 or j==n-1):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()'''
#7
'''n=5
for i in  range(n):
    for j in range(i,n):
        print(" ",end=' ')
    for j in range(i):
        if(i==n-1 or j==0):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    for j in range(i+1):
        if(i==n-1 or j==i):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()'''
#8
n=5
for i in  range(n-1):
    for j in range(i,n):
        print(" ",end=' ')
    for j in range(i):
        if(j==0):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    for j in range(i+1):
        if(j==i):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
for i in  range(n):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,n-1):
        if(j==i):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    for j in range(i,n):
        if(j==n-1):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()




