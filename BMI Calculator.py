weight = int(input("What is your weight? "))
height = int(input("What is your height? "))

body_mass_index = weight / height ** 2

if body_mass_index < 18.5:
    print(f"Your BMI is {body_mass_index}, you are underweight ")
elif body_mass_index < 25 :
    print(f"Your BMI is {body_mass_index}, you are normal weight ")
elif body_mass_index < 30:
    print(f"Your BMI is {body_mass_index}, you are slightly overweight ")
elif body_mass_index < 35:
    print(f"Your BMI is {body_mass_index}, you are obese")
else:
    print(f"Your BMI is {body_mass_index}, you are clinicaly obese")