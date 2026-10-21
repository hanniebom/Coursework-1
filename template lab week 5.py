"""
RECORD CHECK  -  my version
===========================

Name  : Hania Sherif
Lane  : Cybersecurity and Digital Forensics
Date  : 21/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
class Record:
    def __init__(self, label, value, limit):
        """Initialize a record instance with a label, numeric value, and target limit."""
        self.label = label
        self.value = value
        self.limit = limit

records = [
    Record("R-001", 87.0, 100.0),
    Record("R-002", 120.0, 100.0)
    ]

for record in records:
    print()
    print("=" * 34)
    print(f" RECORD CHECK - {record.label}")
    print(f" Value: {record.value}")
    print(f" Limit: {record.limit}")
    print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
