#!/usr/bin/env python3

"""Module to calculate new loan balance after monthly payment."""

__author__ = 'Lydia Frame'
__date__ = '3/30/2025'

from decimal import Decimal, ROUND_HALF_UP

def main():
    """Calculate loan balance after payment and interest paid."""
    
    # Prompt user for inputs
    balance = float(input('Balance? '))
    annual_rate = float(input('APR? '))
    payment = float(input('Payment? '))

    # Convert annual rate to monthly rate
    monthly_rate = annual_rate / 100 / 12
    
    # Convert balance and payment to Decimals for accurate calculations
    dec_balance = Decimal(balance).quantize(Decimal('.01'), ROUND_HALF_UP)
    dec_payment = Decimal(payment).quantize(Decimal('.01'), ROUND_HALF_UP)
    
    # Calculate interest paid for the month
    interest_paid = dec_balance * Decimal(monthly_rate)
    
    # Calculate new balance after payment is applied
    new_balance = dec_balance - (dec_payment - interest_paid)
    
    # Output results formatted as currency with spaces for alignment
    print(f'Interest Paid:       ${interest_paid:,.2f}')
    print(f'New Balance:         ${new_balance:,.2f}')

if __name__ == '__main__':
    main()