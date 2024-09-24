import math

# These functions are to be used for investments and understanding interest gain.
def calcFutureVal():

  while True:
    try:
      # Call for user action to input the variables for the function.
      presentVal = float(input("What is the initial investment? "))
      interestRate = float(input("What is the interest rate? "))
      period = float(input("How long do you want to invest in years? "))
      break
    except ValueError:
      # if user didn't enter right info give error message
      print("That is not a valid input")
      continue

  # Calculating the rate multipler.
  rateMultiplier = (interestRate/ 100) + 1

  # Calculating future value with the formula FV = PV(1 + r)^t
  futureVal = presentVal * pow(rateMultiplier, period)

  # Rounding answer for readability.
  roundedAnswer = round(futureVal, 2)

  answer = f"With the initial investment of {presentVal}, with the interest rate of {interestRate}%, after {period} years your investment would be: ${roundedAnswer}"
  print(answer)



def calcPresentVal():
  while True:
    try:
      # Call for user action to input the variables for the function.
      futureVal = float(input("What is the current investment? "))
      interestRate = float(input("What is the interest rate? "))
      period = float(input("How long do you want to invest in years? "))
      break
    except ValueError:
      # if user didn't enter right info give error message
      print("That is not a valid input")
      continue

  # Calculate the rate multiplier
  rateMultiplier = (interestRate / 100) + 1

  # Calculating the present value with the formula PV = FV / (1 + r)^t
  presentVal = futureVal / pow(rateMultiplier, period)

  # Cleaning up the answer for readability.
  roundedAnswer = round(presentVal, 2)

  answer = f"With the current investment of {futureVal}, with the interest rate of {interestRate}%, after accruing interest for {period} years your initial investment would have been: ${roundedAnswer}"
  print(answer)



# Calculates the interest rate after given the current investment amount, initial investment amount, and the time spent accruing interest.
def calcRate():
  # Call for user action to input the variables for the function.
  while True:
    try:
      futureVal = float(input("What is the current investment amount? "))
      presentVal = float(input("What is the initial investment? "))
      period = float(input("How long has this investment sat? "))
      if presentVal <= 0 or period <= 0:
        print("The initial investment and time period must be greater than zero.")
        continue
    except ValueError:
      print("That is not a valid input.")
      continue

    # Calculate the quotient value.
    quotientVal = futureVal / presentVal

    # Calculate the compound interest rate with formula.
    investmentRate = (pow(quotientVal, (1/period)) - 1) * 100

    # Round the answer for readability.
    investmentRate = round(investmentRate, 2)


    answer = f"After {period} years, your current investment is at {futureVal}, and your initial investment was {presentVal}, doing some calculations we can determine that your investment rate was {investmentRate}"
    print(answer)


# Calculates the time that an investment has lived based on the current value, the interest rate and the value initially submitted.
def calcTime():
  while True:
    try:
      futureVal = float(input("What is the current investment amount? "))
      presentVal = float(input("What was the initial investment? "))
      intRate = float(input("What is the investment rate? "))
      if presentVal <= 0 or intRate <= 0:
          print("The initial investment and rate must be greater than zero.")
          continue
      break
    except ValueError:
      print("That is not a valid input. Please enter numbers only.")

  # Calculating rate multiplier for math, leaving the rate the same for printing purposes
  rateMultiplier = (float(intRate) / 100) + 1

  # Calculating the quotient value
  quotientVal = futureVal / presentVal

  # Calculating the time by solving for t in the equation (1+r)^t = FV/PV
  resultTime = (math.log(quotientVal) / math.log(rateMultiplier))

  # Rounding the result for readability.
  resultTime = round(resultTime, 2)

  answer = f"Based on the current investment of ${futureVal} and an initial investment of ${presentVal}, the investment has accrued over approximately {resultTime} years."
  print(answer)

def main():
    while True:
        print("\nInvestment Calculator Menu:")
        print("1. Calculate Future Value")
        print("2. Calculate Present Value")
        print("3. Calculate Interest Rate")
        print("4. Calculate Investment Time")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            calcFutureVal()
        elif choice == '2':
            calcPresentVal()
        elif choice == '3':
            calcRate()
        elif choice == '4':
            calcTime()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 5.")

# Start the program
if __name__ == "__main__":
    main()