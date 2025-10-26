# Exercise 24: Simple Grade Book
# Objective: Create a grade book system with student management and statistics

# Hint: Use nested dictionaries to store students and their grades
# Hint: Structure: students = {"S001": {"name": "Alice", "grades": {"Math": [95, 88]}}}
# Hint: Create helper functions for calculations (average, letter grade, GPA)
# Hint: Use .get() for safe dictionary access
# Hint: Validate all inputs (grades 0-100, non-empty names)

students = {}


def get_letter_grade(average):
    """Convert numeric grade to letter grade."""
    # A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: 0-59
    pass


def get_gpa(average):
    """Convert numeric grade to GPA (4.0 scale)."""
    # A: 4.0, B: 3.0, C: 2.0, D: 1.0, F: 0.0
    pass


def calculate_average(grades_list):
    """Calculate average from a list of grades."""
    # Return 0 if empty, otherwise sum/length
    pass


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
    # Get student name and ID
    # Check if ID already exists
    # Create student dictionary with name and empty grades dictionary
    # Add to students dictionary
    pass


def add_grade():
    """Add a grade for a student in a subject."""
    # Get student ID and check if exists
    # Get subject name
    # Get grade (validate 0-100)
    # Add grade to student's grades for that subject
    # If subject doesn't exist, create new list
    pass


def view_student_report():
    """Display detailed report for a student."""
    # Get student ID and check if exists
    # Display student name and ID
    # Display table header
    # Loop through subjects and display grade, letter grade
    # Calculate and display overall average and GPA
    pass


def view_all_students():
    """Display summary of all students."""
    # Check if any students exist
    # Display header
    # Loop through all students
    # Display ID, name, number of subjects, overall average
    pass


def class_statistics():
    """Display statistics for the entire class."""
    # Calculate statistics for each subject
    # Find highest and lowest for each subject
    # Calculate class average
    # Display formatted statistics
    pass


def top_performers():
    """Display top performing students."""
    # Calculate average for each student
    # Sort students by average (highest first)
    # Display top 3 or all if less than 3
    pass


# Main program loop
while True:
    display_menu()

    # Get user choice


    # Call appropriate function


    # Handle invalid choice
