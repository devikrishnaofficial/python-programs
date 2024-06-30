"""1 An electric power distribution company charges domestic customers as
follows: Consumption unit Rate of charge:
1.1. 0-200 Rs. 0.50 per unit
1.2. 201-400 Rs. 0.65 per unit in excess of 200
1.3. 401-600 Rs 0.80 per unit excess of 400
1.4. 601 and above Rs 1.00per unit excess of 600
1.5. If the bill exceeds Rs. 400, then a surcharge of 15% will be charged,
and the minimum bill should be Rs. 100/-
Create a Python program based on the scenario mentioned above."""

def calculate_bill(units):
    if units <= 0:
        return "Units cannot be zero or negative."
    
    elif units <= 200:
        charge = units * 0.50
        
    elif units <= 400:
        charge = 200 * 0.50 + (units - 200) * 0.65
        
    elif units <= 600:
        charge = 200 * 0.50 + 200 * 0.65 + (units - 400) * 0.80
        
    else:
        charge = 200 * 0.50 + 200 * 0.65 + 200 * 0.80 + (units - 600) * 1.00

    if charge > 400:
        surcharge = charge * 0.15
        total_bill = charge + surcharge
    else:
        total_bill = charge

    if total_bill < 100:
        total_bill = 100
    
    return total_bill
units_consumed = float(input("Enter the number of units consumed: "))
bill_amount = calculate_bill(units_consumed)
print(f"Electricity bill: Rs. {bill_amount:.2f}") 
