from cs50 import get_int


def main():
    subjects()
    marks()

    # for 10 subjects, overall marks will be out of 100
    total_marks = sum(scores)
    percentage = (total_marks / 1000) * 100
    print(f"Percentage: {percentage:.2f}")

    gpa()
    credits()

    # to calculate total gpa in the first semester
    total_credits = 25
    credit_score = sum(credit)
    cgpa = credit_score / total_credits
    print(f"Total SGPA: {cgpa:.2f}")


def subjects():
    print()
    print("Total Subjects in First Semester:")
    print("1. Communication Skills")
    print("2. Applied Physics")
    print("3. Applied Chemistry")
    print("4. Electrical Science")
    print("5. Applied Mathematics")
    print("6. Manufacturing Process")
    print("7. Applied Physics Lab")
    print("8. Applied Chemistry Lab")
    print("9. Electrical Science Lab")
    print("10. Engineering Graphics Lab (EGL)")
    print()


scores = []


def marks():
    print("Marks scored out of 100 in each subject:")
    for i in range(1, 11):
        print(f"Score in Subject {i}:", end=" ")
        score = get_int("")
        scores.append(score)
    print()


sgpa = []

# To calculate gpa based on IP University criteria


def gpa():
    for i in range(10):
        if scores[i] < 40:
            temp = 0
            sgpa.append(temp)
        elif 40 <= scores[i] <= 44:
            temp = 4
            sgpa.append(temp)
        elif 45 <= scores[i] <= 49:
            temp = 5
            sgpa.append(temp)
        elif 50 <= scores[i] <= 54:
            temp = 6
            sgpa.append(temp)
        elif 55 <= scores[i] <= 64:
            temp = 7
            sgpa.append(temp)
        elif 65 <= scores[i] <= 74:
            temp = 8
            sgpa.append(temp)
        elif 75 <= scores[i] <= 89:
            temp = 9
            sgpa.append(temp)
        elif 90 <= scores[i] <= 100:
            temp = 10
            sgpa.append(temp)


credit = []


# Credit Score for each subject based on IP University
def credits():
    # subjects 1-4 have 3 credit points
    for i in range(4):
        temp = sgpa[i] * 3
        credit.append(temp)

    # subjects 5-6 have 4 credit points
    for i in range(4, 6):
        temp = sgpa[i] * 4
        credit.append(temp)

    # subjects 7-9 have one credit point
    for i in range(6, 9):
        temp = sgpa[i] * 1
        credit.append(temp)

    # EGL has two credit points
    for i in range(9, 10):
        temp = sgpa[i] * 2
        credit.append(temp)


main()
