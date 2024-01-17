#In this program we will find odd or even from the user input

a=int(input("Enter a number to find if it is odd or even: "))

#In our day to day life we say if a number is devided by 3 it is odd 
# and if a number is devided by 2 it is even

if a%2==0:
    print(f"{a} is a even number")
elif a%3==0:
    print(f"{a} is odd number")
else:
    print("not even nor odd ")