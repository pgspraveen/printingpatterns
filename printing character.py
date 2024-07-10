#1
'''n=int(input())
p=65
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=' ')
    p+=1
    print()'''
#2
'''n=int(input())
p=69
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=' ')
    p-=1
    print()'''
#3
'''s="CODER"
n=len(s)
p=0
for i in range(n):
    for j in range(i+1):
        print(s[p],end=' ')
    p+=1
    print()'''
#4
'''s="CODER"
n=len(s)
p=n-1
for i in range(n):
    for j in range(i+1):
        print(s[p],end=' ')
    p-=1
    print()'''
#5
'''s="CODER"
n=len(s)
for i in range(n):
    p=0
    for j in range(i+1):
        print(s[p],end=' ')
        p+=1
    print()'''
#6
'''s="CODER"
n=len(s)
for i in range(n):
    p=n-1
    for j in range(i+1):
        print(s[p],end=' ')
        p-=1
    print()'''
#7
s="CODER"
n=len(s)
k=n-1
for i in range(n):   
    p=k
    for j in range(i):
        print(" ",end=' ')
    for j in range(i,n):
        print(s[p],end=' ')
        p-=1
    k-=1
    print()













