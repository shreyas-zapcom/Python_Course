try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception as e:
    print("An unexpected error occurred:", e)
else:
    print("Division was successful.")
finally:
    print("Program execution completed.")
