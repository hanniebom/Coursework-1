"""
RECORD CHECK  -  my version
===========================

Name  : Hania Sherif
Lane  : Cybersecurity and Digital Forensics
Date  : 14/10/2026

Run it: python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
def check_record(value, limit):
    """Calculate and return the difference, percentage, and status string."""
    difference = value - limit
    if limit == 0:
        percent = float('inf')
    else:
        percent = (value / limit) * 100
        
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    return difference, percent, status

def print_report(label, value, limit, difference, percent, status):
    """Print the complete formatted report with borders."""
    print()
    print("=" * 34)
    print(f"RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"Used       : {value:.2f}")
    print(f"Total      : {limit:.2f}")
    print(f"Diff       : {difference:.2f}")
    print(f"Percent    : {percent:.2f}%")
    print(f"Status     : {status}")
    print("=" * 34)

def load_records(path):
    """Read a comma-separated file and return a list of dictionaries."""
    loaded_list = []
    with open(path, "r") as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            record_dict = {
                "label": label, 
                "value": float(value), 
                "limit": float(limit)
            }
            loaded_list.append(record_dict)
            
    return loaded_list

records = load_records("records_sample.txt")

for record in records:
    diff, pct, stat = check_record(record["value"], record["limit"])
    print_report(record["label"], record["value"], record["limit"], diff, pct, stat)
