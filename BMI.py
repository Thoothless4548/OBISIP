def calculate_bmi(weight, height):
    # Ensure valid inputs
    if weight <= 0 or height <= 0:
        raise ValueError("Weight and height must be positive values.")

    # BMI Calculation
    bmi = weight / (height ** 2)

    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    try:
        # Get user inputs
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        # Validate user inputs
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive values.")

        # Calculate BMI
        bmi = calculate_bmi(weight, height)

        # Classify BMI
        category = classify_bmi(bmi)

        # Display results
        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are classified as: {category}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
