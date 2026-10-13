"""
RECORD CHECK  -  my version
===========================

Name  : Hania Sherif
Lane  : Cybersecurity
Date  : 7/10/2026
Run it: python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
import math

def status_of(percent):
    """Return a status string based on the given percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def check(value, limit):
    """Calculate and return the difference and percentage as two values."""
    difference = value - limit
    
    if limit == 0:
        percent = float('inf') 
    else:
        percent = (value / limit) * 100
    return difference, percent

def print_report(label, value, limit, difference, percent, status):
    """Print the complete formatted report with borders."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Used      : {value:.2f}")
    print(f"  Total     : {limit:.2f}")
    print(f"  Diff      : {difference:.2f}")
    print(f"  Percent   : {percent:.2f}%")
    print(f"  Status    : {status}")
    print("=" * 34)

over_limit_count = 0

while True:
    
    label = input("Enter record label (or type 'quit' to stop): ")
    if label.lower() == "quit":
        break
        
    value = float(input("Enter value (number): "))
    limit = float(input("Enter limit (number): "))


    difference, percent = check(value, limit)
    status = status_of(percent)
  
    if status == "OVER LIMIT":
        over_limit_count += 1

    print_report(label, value, limit, difference, percent, status)


print(f"\nTotal records OVER LIMIT: {over_limit_count}")



# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
