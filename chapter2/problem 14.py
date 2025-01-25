def get_grade(marks):
    if marks == -1:
        return "NA"
    elif marks <= 39:
        return "F"
    elif marks <= 44:
        return "P"
    elif marks <= 49:
        return "C"
    elif marks <= 54:
        return "B"
    elif marks <= 59:
        return "B+"
    elif marks <= 69:
        return "A"
    elif marks <= 79:
        return "A+"
    elif marks <= 100:
        return "O"

def main():
    s1 = int(input("Enter marks for Subject 1: "))
    s2 = int(input("Enter marks for Subject 2: "))
    s3 = int(input("Enter marks for Subject 3: "))

    total = s1 + s2 + s3
    average = total / 3

    print("Subject 1 Grade:", get_grade(s1))
    print("Subject 2 Grade:", get_grade(s2))
    print("Subject 3 Grade:", get_grade(s3))

    if s1 <= 39 or s2 <= 39 or s3 <= 39:
        print("Result: Fail")
    else:
        print("Result: Pass")

    print("Total Marks:", total)
    print("Average Marks:", average)

main()
