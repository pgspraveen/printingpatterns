'''n=int(input())
for i in range(n):
    for j in range(n):
        print("*",end=' ')
    print('',end='\n')'''
#increasing triangle pattern
'''n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end=' ')
    print('',end='\n')'''
#decreasing triangle pattern
'''n=int(input())
for i in range(n):
    for j in range(i,n):
        print("*",end=' ')
    print('',end='\n')'''
#rightsidedtriangle
'''n=int(input())
for i in range(n):
    for j in range(i,n):
        print(" ",end=' ')
    for j in range(i+1):
        print("*",end=' ')
    print('',end='\n')'''
#another
'''n=int(input())
for i in range(n):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,n):
        print("*",end=' ')
    print('',end='\n')'''
#hill pattern
'''n=int(input())
for i in range(n):
    for j in range(i,n):
        print(" ",end=' ')
    for j in range(i):
        print("*",end=' ')
    for j in range(i+1):
        print("*",end=' ')
    print('',end='\n')'''
#anotherhillclimb(reverse hill)
'''n=int(input())
for i in range(n):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,n-1):
        print("*",end=' ')
    for j in range(i,n):
        print("*",end=' ')
    print('',end='\n')'''  
#diamond pattern
'''n=int(input())
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=' ')
    for j in range(i):
        print("*",end=' ')
    for j in range(i+1):
        print("*",end=' ')
    print('',end='\n')
for i in range(n):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,n-1):
        print("*",end=' ')
    for j in range(i,n):
        print("*",end=' ')
    print('',end='\n')'''
l=int(input())
b=int(input())
print("*"*b)
for i in range(1,l-1):
    print("*"+""*((b*2)-3)+"*")
print("*"*b)









