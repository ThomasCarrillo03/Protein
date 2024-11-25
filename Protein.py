# Get the weight and height of the user
height = float(input("Insert your height in meters: "))
weight = float(input("Insert your weight in kilograms: "))

# Calculate the BMI
bmi = weight / (height * height)

# Calculate the ideal protein
idealProteinMin = bmi * 1.2

print(f"Your BMI is: {bmi:.2f}")
print(f"That means that your ideal minimum quantity of protein is: {
      idealProteinMin:.2f} grams")
print("Remember that there are more factors to take into account.")
