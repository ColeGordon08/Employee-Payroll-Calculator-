import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV
df = pd.read_csv("Employees.csv")
df.columns = df.columns.str.strip()
print("COLUMNS:", repr(df.columns.tolist()))
# Calculate regular hours
df["regular_hours"] = df["hours_worked"].clip(upper=40)

# Calculate overtime hours
df["overtime_hours"] = (df["hours_worked"] - 40).clip(lower=0)

# Calculate regular pay
df["regular_pay"] = df["regular_hours"] * df["hourly_rate"]

# Calculate overtime pay
df["overtime_pay"] = df["overtime_hours"] * df["hourly_rate"] * 1.5

# Calculate gross pay
df["gross_pay"] = df["regular_pay"] + df["overtime_pay"]

# Create the chart
plt.figure(figsize=(10, 6))

plt.bar(df["Name"], df["gross_pay"])

plt.title("Employee Gross Pay")
plt.xlabel("Employee")
plt.ylabel("Gross Pay ($)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()
