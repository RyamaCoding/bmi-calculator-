height = float(input("Enter your heigh in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / (height ** 2)
if(bmi < 18.5):
    print(f"Your BMI is {bmi:.2f}, you are underweight")
elif(bmi >= 18.5 and bmi < 25):
    print(f"Your BMI is {bmi:.2f}, you are normal weight")
elif(bmi >= 25 and bmi < 30):
    print(f"Your BMI is {bmi:.2f}, you are overweight")
elif(bmi >= 30 and bmi < 35):
    print(f"Your BMI is {bmi:2f}, you are obese")
else:
    print(f"Your BMI is {bmi:.2f}, you are clinically obese")