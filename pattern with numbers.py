#1
'''n=int(input())
for i in range(n):
    for j in range(i+1):
        print("1",end=' ')
    print()'''
#2
'''n=int(input())
p=1
for i in range(n):
    for j in range(i+1):
        print( p,end=' ')
    p+=1
    print()'''
#3
'''n=int(input())
p=5
for i in range(n):
    for j in range(i+1):
        print( p,end=' ')
    p-=1
    print()'''
#4
'''n=int(input())
p=0
for i in range(n):
    for j in range(i+1):
        print( p,end=' ')
    p+=2   
    print()'''
#5
'''n=int(input())
for i in range(n):
    for j in range(i+1):
        if(i%2==0):
            print("1",end=' ')
        else:
            print("2",end=' ')
    print()'''
#6
'''n=int(input())
p=1
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=' ')
    for j in range(i):
        print(p,end=' ')
    for j in range(i+1):
        print(p,end=' ')
    p+=1
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,n-1):
        print(p,end=' ')
    for j in range(i,n):
        print(p,end=' ')
    p+=1
    print()'''   
#7
'''n=int(input())
p=1
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=' ')
    for j in range(i):
        print(p,end=' ')
    for j in range(i+1):
        print(p,end=' ')
    p+=1
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,n-1):
         print(p,end=' ')
    for j in range(i,n):
        print(p,end=' ')
    p-=1
    print()'''   
#8
'''n=int(input())
for i in range(n):
    p=1
    for j in range(i+1):
        print(p,end=" ")
        p+=1
    print()'''
#9
'''n=int(input())
for i in range(n):
    p=1
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print(p,end=" ")
        p+=1
    print()'''
#10
'''n=int(input())
for i in range(n):
    p=1
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print(p,end=" ")
        p+=1
    for j in range(i+1):
        print(p,end=" ")
        p+=1
    print()'''
#11
'''n=int(input())
for i in range(n):
    p=5
    for j in range(i+1):
        print(p,end=" ")
        p-=1
    print()'''
#12
'''n=int(input())
k=5
for i in range(n):
    p=k
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print(p,end=" ")
        p-=1
    k-=1
    print()'''
#13
'''n=int(input())
for i in range(n):
    p=1
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print(p,end=" ")
        p+=1
    for j in range(i+1):
        print(p,end=" ")
        p-=1
    print()'''
#14floyd triangle
n=int(input())
p=1
for i in range(n):
    for j in range(i+1):
        print(p,end=' ')
        p+=1
    print()















    
