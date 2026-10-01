"""
RECORD CHECK  -  my version
===========================

Name  : Hania Sherif 
Lane  : Cyber
Date  : 30//09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ================================================================= INPUT
label = input("Enter the name: ")
value = float(input("Enter the used amount: "))
limit = float(input("Enter the total limit: "))

# =============================================================== PROCESS
# 2. Work out the difference and the percentage.
difference = value - limit
percent = (value / limit) * 100

if percent >= 100:
    status = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"

# ================================================================ OUTPUT
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"  Used       : {value:>15.2f}")
print(f"  Total      : {limit:>15.2f}")
print(f"  Difference : {difference:>15.2f}")
print(f"  Percentage : {percent:>14.2f}%")
print(f"  Status     : {status:>15}")

print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
