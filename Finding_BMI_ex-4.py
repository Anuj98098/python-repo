#Here in this program we will calculate the BMI of the user. 
#In which we will ask the user for their weight and height
#formula for the calculation of BMI is:
# BMI=weight/height**2

weight=input("Please enter you weight: ")
height=input("Please enter your height: ")
#After taking input from the user you have to change the values in their calculative data type
#As input method always take string values which can not be calculative
BMI=float(weight)/int(height)**2
print(int(BMI))
