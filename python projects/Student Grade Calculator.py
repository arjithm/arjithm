# Function to calculate grade based on average score
def calculate_grade(average_score):
    if 90 <= average_score <= 100:
        return 'A'
    elif 80 <= average_score < 90:
        return 'B'
    elif 70 <= average_score < 80:
        return 'C'
    elif 60 <= average_score < 70:
        return 'D'
    else:
        return 'F'


# Main function to get student's name, scores, and calculate average and grade
def student_grade_calculator():
    name = input("Enter the student's name: ")
    scores = []

    num_subjects = int(input("Enter the number of subjects: "))
    for i in range(num_subjects):
        score = float(input(f"Enter score for subject {i + 1}: "))
        scores.append(score)

    average_score = sum(scores) / num_subjects
    grade = calculate_grade(average_score)

    print(f"\nStudent Name: {name}")
    print(f"Average Score: {average_score:.2f}")
    print(f"Grade: {grade}")


student_grade_calculator()
