"""
# Ruchika Suneja
# module2_case_study.py
# This program determines whether a student qualifies
# for the Dean's List or the Honor Roll.
"""

while True:
    last_name = input("Enter student's last name: ")

    if last_name.upper() == "ZZZ":
        print("Program ended.")
        break

    first_name = input("Enter student's first name: ")
    try:
        gpa = float(input("Enter student's GPA: "))
    except ValueError:
        print("Invalid GPA. Please enter a numeric value.")
        continue

    if gpa >= 3.5:
        print(first_name, last_name, "has made the Dean's List.")
    elif gpa >= 3.25:
        print(first_name, last_name, "has made the Honor Roll.")
    else:
        print(first_name, last_name, "did not qualify.")
