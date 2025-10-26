# Exercise 24: Solution

## Solution 1: Complete Implementation
```python
students = {}


def get_letter_grade(average):
    """Convert numeric grade to letter grade."""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'


def get_gpa(average):
    """Convert numeric grade to GPA (4.0 scale)."""
    if average >= 90:
        return 4.0
    elif average >= 80:
        return 3.0
    elif average >= 70:
        return 2.0
    elif average >= 60:
        return 1.0
    else:
        return 0.0


def calculate_average(grades_list):
    """Calculate average from a list of grades."""
    if not grades_list:
        return 0
    return sum(grades_list) / len(grades_list)


def display_menu():
    """Display the main menu."""
    print("\n===== GRADE BOOK SYSTEM =====\n")
    print("1. Add student")
    print("2. Add grade")
    print("3. View student report")
    print("4. View all students")
    print("5. Class statistics")
    print("6. Top performers")
    print("7. Quit")


def add_student():
    """Add a new student to the grade book."""
    name = input("\nStudent name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return

    student_id = input("Student ID: ").strip()
    if not student_id:
        print("Student ID cannot be empty!")
        return

    if student_id in students:
        print(f"Student ID {student_id} already exists!")
        return

    students[student_id] = {
        "name": name,
        "grades": {}
    }

    print(f"Student {name} added successfully!")


def add_grade():
    """Add a grade for a student in a subject."""
    student_id = input("\nStudent ID: ").strip()

    if student_id not in students:
        print(f"Student ID {student_id} not found!")
        return

    subject = input("Subject: ").strip()
    if not subject:
        print("Subject cannot be empty!")
        return

    try:
        grade = float(input("Grade (0-100): "))
        if grade < 0 or grade > 100:
            print("Grade must be between 0 and 100!")
            return

        # Add grade to student's subject
        if subject not in students[student_id]["grades"]:
            students[student_id]["grades"][subject] = []

        students[student_id]["grades"][subject].append(grade)
        print(f"Grade {grade} added for {subject}!")

    except ValueError:
        print("Invalid grade! Please enter a number.")


def view_student_report():
    """Display detailed report for a student."""
    student_id = input("\nStudent ID: ").strip()

    if student_id not in students:
        print(f"Student ID {student_id} not found!")
        return

    student = students[student_id]
    print(f"\n===== REPORT CARD =====")
    print(f"Student: {student['name']} ({student_id})")
    print("-" * 40)

    if not student["grades"]:
        print("No grades recorded yet.")
        return

    print(f"{'Subject':<15} | {'Grade':<6} | Letter")
    print("-" * 40)

    all_grades = []
    for subject, grades in student["grades"].items():
        avg = calculate_average(grades)
        letter = get_letter_grade(avg)
        all_grades.extend(grades)
        print(f"{subject:<15} | {avg:<6.1f} | {letter}")

    print("-" * 40)
    overall_avg = calculate_average(all_grades)
    overall_letter = get_letter_grade(overall_avg)
    overall_gpa = get_gpa(overall_avg)

    print(f"{'Average:':<15} | {overall_avg:<6.1f} | {overall_letter}")
    print(f"{'GPA:':<15} | {overall_gpa:<6.2f} |")
    print("-" * 40)


def view_all_students():
    """Display summary of all students."""
    if not students:
        print("\nNo students in grade book!")
        return

    print(f"\n{'ID':<10} | {'Name':<20} | {'Subjects':<10} | {'Average':<8} | Grade")
    print("-" * 70)

    for student_id, student in students.items():
        name = student["name"]
        num_subjects = len(student["grades"])

        # Calculate overall average
        all_grades = []
        for grades_list in student["grades"].values():
            all_grades.extend(grades_list)

        if all_grades:
            avg = calculate_average(all_grades)
            letter = get_letter_grade(avg)
            print(f"{student_id:<10} | {name:<20} | {num_subjects:<10} | {avg:<8.1f} | {letter}")
        else:
            print(f"{student_id:<10} | {name:<20} | {num_subjects:<10} | {'N/A':<8} | N/A")


def class_statistics():
    """Display statistics for the entire class."""
    if not students:
        print("\nNo students in grade book!")
        return

    print("\n===== CLASS STATISTICS =====")
    print(f"Total Students: {len(students)}\n")

    # Collect all subjects
    all_subjects = set()
    for student in students.values():
        all_subjects.update(student["grades"].keys())

    if not all_subjects:
        print("No grades recorded yet!")
        return

    # Statistics for each subject
    for subject in sorted(all_subjects):
        subject_grades = []
        student_names = []

        for student_id, student in students.items():
            if subject in student["grades"]:
                avg = calculate_average(student["grades"][subject])
                subject_grades.append(avg)
                student_names.append(student["name"])

        if subject_grades:
            avg = calculate_average(subject_grades)
            highest = max(subject_grades)
            lowest = min(subject_grades)
            highest_student = student_names[subject_grades.index(highest)]
            lowest_student = student_names[subject_grades.index(lowest)]

            print(f"{subject}:")
            print(f"  Average: {avg:.1f}")
            print(f"  Highest: {highest:.1f} ({highest_student})")
            print(f"  Lowest: {lowest:.1f} ({lowest_student})")
            print()

    # Overall class average
    all_grades = []
    for student in students.values():
        for grades_list in student["grades"].values():
            all_grades.extend(grades_list)

    if all_grades:
        overall_avg = calculate_average(all_grades)
        print(f"Overall Class Average: {overall_avg:.1f}")


def top_performers():
    """Display top performing students."""
    if not students:
        print("\nNo students in grade book!")
        return

    # Calculate average for each student
    student_averages = []
    for student_id, student in students.items():
        all_grades = []
        for grades_list in student["grades"].values():
            all_grades.extend(grades_list)

        if all_grades:
            avg = calculate_average(all_grades)
            student_averages.append((student["name"], student_id, avg))

    if not student_averages:
        print("\nNo grades recorded yet!")
        return

    # Sort by average (highest first)
    student_averages.sort(key=lambda x: x[2], reverse=True)

    print("\n===== TOP PERFORMERS =====\n")
    print(f"{'Rank':<6} | {'Name':<20} | {'ID':<10} | {'Average':<8} | Grade")
    print("-" * 70)

    for rank, (name, student_id, avg) in enumerate(student_averages[:10], 1):
        letter = get_letter_grade(avg)
        print(f"{rank:<6} | {name:<20} | {student_id:<10} | {avg:<8.1f} | {letter}")


# Main program loop
print("Welcome to Grade Book System!")

while True:
    display_menu()

    choice = input("\nChoose option: ").strip()

    if choice == '1':
        add_student()
    elif choice == '2':
        add_grade()
    elif choice == '3':
        view_student_report()
    elif choice == '4':
        view_all_students()
    elif choice == '5':
        class_statistics()
    elif choice == '6':
        top_performers()
    elif choice == '7':
        print("\nGoodbye!")
        break
    else:
        print("Invalid option! Please choose 1-7.")
```

## Solution 2: Enhanced with Weighted Grades
```python
students = {}


def get_letter_grade(average):
    """Convert numeric grade to letter grade."""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'


def get_gpa(average):
    """Convert numeric grade to GPA (4.0 scale)."""
    letter = get_letter_grade(average)
    gpa_map = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
    return gpa_map[letter]


def calculate_average(grades_list):
    """Calculate average from a list of grades."""
    if not grades_list:
        return 0
    return sum(grades_list) / len(grades_list)


def calculate_weighted_average(grades_dict):
    """
    Calculate weighted average.
    grades_dict format: {"tests": [90, 85], "homework": [95, 88], "quizzes": [92]}
    Weights: tests=50%, homework=30%, quizzes=20%
    """
    weights = {"tests": 0.5, "homework": 0.3, "quizzes": 0.2}
    total_weighted = 0
    total_weight = 0

    for category, weight in weights.items():
        if category in grades_dict and grades_dict[category]:
            avg = calculate_average(grades_dict[category])
            total_weighted += avg * weight
            total_weight += weight

    if total_weight > 0:
        return total_weighted / total_weight
    return 0


def add_student():
    """Add a new student to the grade book."""
    name = input("\nStudent name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return

    student_id = input("Student ID: ").strip()
    if not student_id:
        print("Student ID cannot be empty!")
        return

    if student_id in students:
        print(f"Student ID {student_id} already exists!")
        return

    students[student_id] = {
        "name": name,
        "grades": {}
    }

    print(f"Student {name} added successfully!")


def add_grade():
    """Add a grade for a student in a subject."""
    student_id = input("\nStudent ID: ").strip()

    if student_id not in students:
        print(f"Student ID {student_id} not found!")
        return

    subject = input("Subject (Math, English, Science, etc.): ").strip()
    if not subject:
        print("Subject cannot be empty!")
        return

    print("\nGrade categories:")
    print("1. Test")
    print("2. Homework")
    print("3. Quiz")

    category_choice = input("Choose category (1-3): ").strip()
    category_map = {"1": "tests", "2": "homework", "3": "quizzes"}

    if category_choice not in category_map:
        print("Invalid category!")
        return

    category = category_map[category_choice]

    try:
        grade = float(input("Grade (0-100): "))
        if grade < 0 or grade > 100:
            print("Grade must be between 0 and 100!")
            return

        # Initialize subject if needed
        if subject not in students[student_id]["grades"]:
            students[student_id]["grades"][subject] = {
                "tests": [],
                "homework": [],
                "quizzes": []
            }

        students[student_id]["grades"][subject][category].append(grade)
        print(f"Grade {grade} added for {subject} ({category})!")

    except ValueError:
        print("Invalid grade! Please enter a number.")


def view_student_report():
    """Display detailed report for a student."""
    student_id = input("\nStudent ID: ").strip()

    if student_id not in students:
        print(f"Student ID {student_id} not found!")
        return

    student = students[student_id]
    print(f"\n===== REPORT CARD =====")
    print(f"Student: {student['name']} ({student_id})")
    print("-" * 60)

    if not student["grades"]:
        print("No grades recorded yet.")
        return

    print(f"{'Subject':<15} | {'Tests':<7} | {'HW':<7} | {'Quiz':<7} | {'Final':<7} | Letter")
    print("-" * 60)

    subject_averages = []
    for subject, categories in student["grades"].items():
        test_avg = calculate_average(categories.get("tests", []))
        hw_avg = calculate_average(categories.get("homework", []))
        quiz_avg = calculate_average(categories.get("quizzes", []))

        # Weighted average: 50% tests, 30% homework, 20% quizzes
        final_avg = (test_avg * 0.5 + hw_avg * 0.3 + quiz_avg * 0.2)
        letter = get_letter_grade(final_avg)
        subject_averages.append(final_avg)

        print(f"{subject:<15} | {test_avg:<7.1f} | {hw_avg:<7.1f} | "
              f"{quiz_avg:<7.1f} | {final_avg:<7.1f} | {letter}")

    print("-" * 60)
    if subject_averages:
        overall_avg = calculate_average(subject_averages)
        overall_letter = get_letter_grade(overall_avg)
        overall_gpa = get_gpa(overall_avg)

        print(f"{'Overall Average:':<15} | {overall_avg:>45.1f} | {overall_letter}")
        print(f"{'GPA:':<15} | {overall_gpa:>45.2f} |")
    print("-" * 60)


def view_all_students():
    """Display summary of all students."""
    if not students:
        print("\nNo students in grade book!")
        return

    print(f"\n{'ID':<10} | {'Name':<20} | {'Subjects':<10} | {'Average':<8} | Grade")
    print("-" * 70)

    for student_id, student in students.items():
        name = student["name"]
        num_subjects = len(student["grades"])

        # Calculate weighted average for all subjects
        subject_averages = []
        for subject, categories in student["grades"].items():
            test_avg = calculate_average(categories.get("tests", []))
            hw_avg = calculate_average(categories.get("homework", []))
            quiz_avg = calculate_average(categories.get("quizzes", []))
            final_avg = (test_avg * 0.5 + hw_avg * 0.3 + quiz_avg * 0.2)
            subject_averages.append(final_avg)

        if subject_averages:
            avg = calculate_average(subject_averages)
            letter = get_letter_grade(avg)
            print(f"{student_id:<10} | {name:<20} | {num_subjects:<10} | {avg:<8.1f} | {letter}")
        else:
            print(f"{student_id:<10} | {name:<20} | {num_subjects:<10} | {'N/A':<8} | N/A")


def class_statistics():
    """Display statistics for the entire class."""
    if not students:
        print("\nNo students in grade book!")
        return

    print("\n===== CLASS STATISTICS =====")
    print(f"Total Students: {len(students)}\n")

    # Collect all subjects
    all_subjects = set()
    for student in students.values():
        all_subjects.update(student["grades"].keys())

    if not all_subjects:
        print("No grades recorded yet!")
        return

    # Statistics for each subject
    for subject in sorted(all_subjects):
        subject_averages = []
        student_names = []

        for student_id, student in students.items():
            if subject in student["grades"]:
                categories = student["grades"][subject]
                test_avg = calculate_average(categories.get("tests", []))
                hw_avg = calculate_average(categories.get("homework", []))
                quiz_avg = calculate_average(categories.get("quizzes", []))
                final_avg = (test_avg * 0.5 + hw_avg * 0.3 + quiz_avg * 0.2)

                subject_averages.append(final_avg)
                student_names.append(student["name"])

        if subject_averages:
            avg = calculate_average(subject_averages)
            highest = max(subject_averages)
            lowest = min(subject_averages)
            highest_student = student_names[subject_averages.index(highest)]
            lowest_student = student_names[subject_averages.index(lowest)]

            print(f"{subject}:")
            print(f"  Average: {avg:.1f}")
            print(f"  Highest: {highest:.1f} ({highest_student})")
            print(f"  Lowest: {lowest:.1f} ({lowest_student})")
            print()


def top_performers():
    """Display top performing students."""
    if not students:
        print("\nNo students in grade book!")
        return

    # Calculate weighted average for each student
    student_averages = []
    for student_id, student in students.items():
        subject_averages = []
        for subject, categories in student["grades"].items():
            test_avg = calculate_average(categories.get("tests", []))
            hw_avg = calculate_average(categories.get("homework", []))
            quiz_avg = calculate_average(categories.get("quizzes", []))
            final_avg = (test_avg * 0.5 + hw_avg * 0.3 + quiz_avg * 0.2)
            subject_averages.append(final_avg)

        if subject_averages:
            avg = calculate_average(subject_averages)
            gpa = get_gpa(avg)
            student_averages.append((student["name"], student_id, avg, gpa))

    if not student_averages:
        print("\nNo grades recorded yet!")
        return

    # Sort by average (highest first)
    student_averages.sort(key=lambda x: x[2], reverse=True)

    print("\n===== TOP PERFORMERS =====\n")
    print(f"{'Rank':<6} | {'Name':<20} | {'ID':<10} | {'Average':<8} | {'GPA':<6} | Grade")
    print("-" * 75)

    for rank, (name, student_id, avg, gpa) in enumerate(student_averages[:10], 1):
        letter = get_letter_grade(avg)
        print(f"{rank:<6} | {name:<20} | {student_id:<10} | {avg:<8.1f} | {gpa:<6.2f} | {letter}")


def display_menu():
    """Display the main menu."""
    print("\n===== GRADE BOOK SYSTEM =====\n")
    print("1. Add student")
    print("2. Add grade")
    print("3. View student report")
    print("4. View all students")
    print("5. Class statistics")
    print("6. Top performers")
    print("7. Quit")


# Main program
print("Welcome to Grade Book System!")
print("Grades are weighted: Tests 50%, Homework 30%, Quizzes 20%")

while True:
    display_menu()

    choice = input("\nChoose option: ").strip()

    if choice == '1':
        add_student()
    elif choice == '2':
        add_grade()
    elif choice == '3':
        view_student_report()
    elif choice == '4':
        view_all_students()
    elif choice == '5':
        class_statistics()
    elif choice == '6':
        top_performers()
    elif choice == '7':
        print("\nGoodbye!")
        break
    else:
        print("Invalid option! Please choose 1-7.")
```

## Explanation

### Data Structure

```python
students = {
    "S001": {
        "name": "Alice Johnson",
        "grades": {
            "Math": [95, 88, 92],
            "English": [85, 90],
            "Science": [92, 95, 89, 91]
        }
    },
    "S002": {
        "name": "Bob Smith",
        "grades": {
            "Math": [78, 82],
            "English": [88, 85, 90]
        }
    }
}
```

### Key Concepts

1. **Nested Dictionaries**
   - Students dictionary contains student dictionaries
   - Each student has a grades dictionary
   - Each subject has a list of grades

2. **Statistical Calculations**
   ```python
   # Average
   avg = sum(grades) / len(grades)

   # Finding max/min with student names
   highest = max(subject_grades)
   highest_student = student_names[subject_grades.index(highest)]
   ```

3. **Letter Grade Conversion**
   ```python
   def get_letter_grade(average):
       if average >= 90: return 'A'
       elif average >= 80: return 'B'
       elif average >= 70: return 'C'
       elif average >= 60: return 'D'
       else: return 'F'
   ```

4. **Sorting with Lambda**
   ```python
   # Sort by average (highest first)
   student_averages.sort(key=lambda x: x[2], reverse=True)
   ```

5. **Safe Dictionary Access**
   ```python
   # Using .get() to avoid KeyError
   grades = student["grades"].get(subject, [])
   ```

## Common Patterns

1. **Collecting all grades for a student**
   ```python
   all_grades = []
   for grades_list in student["grades"].values():
       all_grades.extend(grades_list)
   avg = sum(all_grades) / len(all_grades)
   ```

2. **Finding unique subjects across all students**
   ```python
   all_subjects = set()
   for student in students.values():
       all_subjects.update(student["grades"].keys())
   ```

3. **Weighted averages**
   ```python
   final = (tests * 0.5) + (homework * 0.3) + (quizzes * 0.2)
   ```

## Extensions

1. **Grade distribution**
   ```python
   def grade_distribution():
       distribution = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
       for student in students.values():
           # Calculate average
           letter = get_letter_grade(avg)
           distribution[letter] += 1

       # Display histogram
       for grade, count in distribution.items():
           print(f"{grade}: {'█' * count} ({count})")
   ```

2. **Class rank**
   ```python
   def calculate_ranks():
       # Sort students by average
       ranked = sorted(student_averages, key=lambda x: x[2], reverse=True)
       # Assign ranks
       for rank, (name, id, avg) in enumerate(ranked, 1):
           students[id]["rank"] = rank
   ```

3. **Grade curve**
   ```python
   def curve_grades(curve_amount=5):
       """Add curve_amount points to all grades."""
       for student in students.values():
           for subject, grades in student["grades"].items():
               student["grades"][subject] = [
                   min(100, grade + curve_amount) for grade in grades
               ]
   ```
