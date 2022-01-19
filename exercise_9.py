def run():
    amount_invested = float(input("Enter the money borrowed or invested: "))
    anual_interest = float(input("Enter the annual rate of interest: "))
    num_years = float(input("Enter the length of time you borrow or invest (in years): "))

    interest_earned = round(amount_invested * (anual_interest/100 + 1) ** num_years, 2)

    print(f'The interest earned after {num_years} years is {interest_earned}')



if __name__ == '__main__':
    run()