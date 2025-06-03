import csv

# Sample data
data = [
    ["Name", "Age", "Country"],
    ["Alice", 30, "USA"],
    ["Bob", 25, "UK"],
    ["Charlie", 35, "Canada"]
]

# Writing to CSV file
with open("sample_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file 'sample_data.csv' created successfully.")