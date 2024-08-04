def calculate_compound_interest(principal, rate, time, compounds_per_year):
    # Convert annual rate from percentage to decimal
    rate_decimal = rate / 100
    
    # Calculate the accumulated amount
    amount = principal * (1 + rate_decimal / compounds_per_year) ** (compounds_per_year * time)
    
    # Calculate compound interest
    compound_interest = amount - principal
    
    return compound_interest, amount

# Example usage
principal = 1000  # Principal amount
rate = 5  # Annual interest rate in percentage
time = 10  # Time period in years
compounds_per_year = 4  # Quarterly compounding

compound_interest, amount = calculate_compound_interest(principal, rate, time, compounds_per_year)
print(f"Compound Interest: ${compound_interest:.2f}")
print(f"Total Amount: ${amount:.2f}")
