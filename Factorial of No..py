## Factorial Of a Number

f=1
n=int(input('Enter an integer: '))
if n<0:
    print("Error! Factorial of a negative number doesn't exist.")
elif n==0:
    print('Factorial is: 1')
    
elif n>0:
    for i in range(1,n+1,1):
        f=f*i
print('Factorial is:',f)
