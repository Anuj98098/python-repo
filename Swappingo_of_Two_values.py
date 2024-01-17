# In this program there will have two values a and b
# We will take values of that variable by the users 
# Print them before swapping
# Then swap them using a third variable 
# And print them
a=input("Enter the value of a: ")
b=input("Enter the value of b: ")
print("The value of a is: ",a)
print("The value of b is: ",b)
# now after getting to know about the value of a and b we will swip the value
temp=a #temp variable is a temperory variable which is used to hold the value of a variable temperorally
a=b
b=temp
print("After swapping the value of a is: ",a)
print("After swapping the value of b is: ",b)
