weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
bmi = round(bmi, 2)
print("Your BMI is:", bmi)
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"
print("Category:", category)