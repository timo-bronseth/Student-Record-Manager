# -------------------------------------------------------------------------------------
# Takes student information as input (fodselsNummer, firstName, lastName, age, email, programmingCourse)
# and stores it in a structured records file. The file should be searchable.
#
# Timo Brønseth, January 2020
# -------------------------------------------------------------------------------------
from StudentRecordClass import StudentRecordClass, \
    displayAllStudents, \
    displaySubjectClassList, \
    displayOldest, \
    displayYoungest
from EncodeDecodeClass import EncodeDecodeClass
import textwrap


# TODO: StudentManagement
# # DONE: enter_info()
# # DONE: displayOptions()
# # TODO: Custom exception?

# DONE: StudentRecordClass
# # DONE: DisplayAllStudents()
# # DONE: DisplaySubjectClassList()
# # DONE: DisplayOldest()
# # DONE: DisplayYoungest()

# TODO: EncodeDecodeClass
# # TODO: EncodeStudentList()
# # TODO: DecodeStudentList()

# TODO: Make all function and variable names have consistent style (CamelCase)

def enterStudentInfo():
    # TODO: "You should also have more specific (and appropriate) handling for Value Errors. If the
    # TODO: user inputs an incorrect value, they should be re-prompted for the correct value type
    # TODO: and then the program should continue."

    try:
        # Querying user for student info, and converting to lowercase.
        fodselsNummer, firstName, lastName, age, email, programmingCourse = \
            input("Fodselsnummer: ").lower(), \
            input("First name: ").lower(), \
            input("Last name: ").lower(), \
            input("Age: ").lower(), \
            input("E-mail: ").lower(), \
            input("Programming Course: ").lower()
    except Exception("Oops something is buggy"):
        print("Oops something is buggy")

    # Defining new student object from entered info.
    student_object = StudentRecordClass(fodselsNummer, firstName, lastName, age, email, programmingCourse)

    # Appends student object into StudentRecords.txt file.
    student_object.addToFile()


# Queries the user for which programming course to display students from.
# It's very short, but I think it seems cleaner to have it here.
def getSubjectName():
    programming_courses = ["Python", "Java", "C", "Php", "Ruby"]

    try:
        # Capitalize() to convert to "Python" in case they write "python".
        subjectname = input("\nSpecify programming course: ").capitalize()

        if subjectname not in programming_courses:
            print("We do not offer that course.\nPlease specify one of {}."
                  .format(str(programming_courses).strip('[]')))
            getSubjectName()

    except Exception("Oops something is buggy"):
        # Task specifies to catch all exceptions like this, even though style guide
        # suggests "Too broad exception clause".
        print("Oops something is buggy")

    return subjectname


def displayOptions():
    try:
        # Ask for user input.
        # textwrap.dedent() removes the indentations from the string.
        user_input = input(textwrap.dedent("""
                                              1. Would you like to see a list of all registered students?
                                              2. Would you like to see a class list for a specific subject?
                                              3. Would you like to see who your oldest student is?
                                              4. Would you like to see who your youngest student is?
                                              Enter a number for the selected task, or X to skip this: """))

    except Exception("Oops something is buggy"):
        # Task specifies to catch all exceptions like this, even though style guide
        # suggests "Too broad exception clause".
        print("Oops something is buggy")

    # Check if user_input points to either of the options, and recursively call
    # the displayOptions() function until user_input has an actionable value.
    if user_input not in ["1", "2", "3", "4", "X", "x"]:
        print("\nPlease select either 1, 2, 3, 4 or X.")
        displayOptions()

    # Execute functions depending on the value of user_input.
    if user_input == "1":
        displayAllStudents()
    elif user_input == "2":
        displaySubjectClassList(getSubjectName())  # Get subject name first.
    elif user_input == "3":
        displayOldest()
    elif user_input == "4":
        displayYoungest()
    elif user_input.upper() == "X":
        print("X")


# Main entry point for the program.
if __name__ == "__main__":

    while True:
        try:
            # Ask for user input, convert to upper case.
            user_input = input("Would you like to enter a student's information? " +
                               "Type Y for Yes and N for No: ").upper()

            if user_input == "Y":
                enterStudentInfo()
                continue  # Continues the loop after running enterStudentInfo().

            elif user_input == "N":
                displayOptions()
                break  # Breaks out of the loop if user types N.

            else:
                print("Please enter either Y or N.")

        except Exception("Oops something is buggy"):
            # Task specifies to catch all exceptions like this, even though style guide
            # suggests "Too broad exception clause".
            print("Oops something is buggy")
