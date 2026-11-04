"""
RECORD CHECK  -  my version
===========================

Name  : Hania Sherif
Lane  : Cybersecurity 
Date  : 04/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("records_sample.csv")

df["percent"] = (df["value"] / df["limit"]) * 100

df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else ("WARNING" if p >= 90 else "OK")
)

print("--- Full DataFrame ---")
print(df)

print("\n--- Rows with Warnings or Over Limits ---")
print(df[df["status"] != "OK"])

print("\n--- Counts per Status Group ---")
status_counts = df.groupby("status").size()
print(status_counts)

df.to_csv("processed_records.csv", index=False)

ax = status_counts.plot(kind="bar", title="Status Counts")
fig = ax.get_figure()
fig.savefig("status_chart.png", bbox_inches="tight")
plt.close(fig)

# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
