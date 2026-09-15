def grades(grade):
    if grade >= 94 and grade <= 100:
        return "A"
    elif grade >= 90 and grade <= 93.99:
        return "A-"
    elif grade >= 87 and grade <= 89.99:
        return "B+"
    elif grade >= 83 and grade <= 86.99:
        return "B"
    elif grade >= 80 and grade <= 82.99:
        return "B-"
    elif grade >= 77 and grade <= 79.99:
        return "C+"
    elif grade >= 73 and grade <= 76.99:
        return "C"
    elif grade >= 70 and grade <= 72.99:
        return "C-"
    elif grade >= 60 and grade <= 69.99:
        return "D"
    else:
        return "F"

float_grade = float(input("Please enter your grade: ")) 
print(grades(float_grade))