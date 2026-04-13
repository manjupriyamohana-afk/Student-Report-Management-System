# student_report.py

file_path = "Student_Report.csv"

# Read file
try:
    with open(file_path, "r") as file:
        content = file.read()
        print("File Content:\n", content)
except FileNotFoundError:
    print("File not found! Creating new file...")

# Write (overwrite)
with open(file_path, "w") as file:
    file.write("Name,Roll No,Math,Science,English\n")
    file.write("Divya,104,88,76,91\n")

print("\nData written successfully!")

# Append data
with open(file_path, "a") as file:
    file.write("Fathima,106,93,87,96\n")
    file.write("Anu,101,85,90,78\n")

print("Data appended successfully!")

# Read all lines
with open(file_path, "r") as file:
    lines = file.readlines()
    print("\nAll Lines:")
    print(lines)

# Final read
with open(file_path, "r") as file:
    final_content = file.read()
    print("\nFinal Content:\n", final_content)
