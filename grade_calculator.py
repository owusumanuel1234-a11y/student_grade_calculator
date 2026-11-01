print("Welcome to Student Grade Calculator.")

#Input
while True:
    student_name = input("Enter name: ").strip()

    if student_name:
        break
    print("Name cann't be empty!")

while True:
    try:
        mathematics_score = float(input("Enter Mathematics score: "))
        science_score = float(input("Enter Science score: "))
        english_score = float(input("Enter english score: "))

        if mathematics_score < 0 or mathematics_score > 100:
            print("Math score is invalid !")
        elif science_score < 0 or science_score > 100:
            print("Science score is invalid !")
        elif english_score < 0 or english_score > 100:
            print("English score is invalid !")
        else:
            total_score = mathematics_score + science_score + english_score
            average_score = total_score / 3

#Output
            print("=== student information ===")
            print(f"Student name: {student_name}")
            print("----------------------")
            print(f"Mathematics score: {mathematics_score:.2f}")
            print(f"Science score: {science_score:.2f}")
            print(f"English score: {english_score:.2f}")
            print("----------------------")
            print(f"Total score: {total_score:.2f}")
            print(f"Average score: {average_score:.2f}")
            print("----------------------")
            if average_score >= 80:
                print("Grade: A")
                print("Status: Excellent")
            elif average_score >= 70:
                print("Grade: B")
                print("Status: Very Good")
            elif average_score >= 60:
                print("Grade: C")
                print("Status: Good")
            elif average_score >= 50:
                print("Grade: D")
                print("Status: Poor")
            else:
                print("Grade: F")
                print("Status: Fail")
            break
    except ValueError:
        print("Invalid number!")