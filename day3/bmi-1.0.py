height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height**2)
new = "Your BMI is " + str(bmi) + ", "

if bmi <= 18.5:
    print(new + "you are underweight.")
elif bmi <= 25:
    print(new + "you have a normal weight")
elif bmi <= 30:
    print(new + "you are overweight")
elif bmi <= 35:
    print(new + "you are obese")
else:
    print(new + "you are clinically obese.")