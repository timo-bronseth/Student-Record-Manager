# -------------------------------------------------------------------------------------
# This program provides an interface that allows the user to access and add to a
# student records database. It also allows the user to encrypt and decrypt the file.
#
# This StudentManagement.py file in particular deals with everything that has to do
# with querying the user, and calling the corresponding functions from other .py files.
#
# A note on code style: Assessment document says to use their function and variable
# names, but it uses CamelCase for function and variable names. This goes against both
# PEP8 and Google Style Guide. Seems weird, but I decided to conform to it with all the
# functions and variables I write in order to stay consistent.
#
# Timo Brønseth, January 2020.
# -------------------------------------------------------------------------------------
from StudentRecordClass import StudentRecordClass as database
from EncodeDecodeClass import EncodeDecodeClass as crypto
from textwrap import dedent

# DONE: StudentManagement
# # DONE: enter_info()
# # DONE: DisplayOptions()

# DONE: StudentRecordClass
# # DONE: DisplayAllStudents()
# # DONE: DisplaySubjectClassList()
# # DONE: DisplayOldest()
# # DONE: DisplayYoungest()

# TODO: EncodeDecodeClass
# # TODO: EncodeStudentList()
# # TODO: DecodeStudentList()

# TODO: Make all function and variable names have consistent style (CamelCase)
# TODO: Use triple-quotes for commenting functions.


def EnterStudentInfo():
    try:
        # Querying user for student info, and converting to lowercase.
        fodselsNummer, firstName, lastName, age, email, programmingCourse = \
            input("\nFodselsnummer: ").lower(), \
            input("First name: ").capitalize(), \
            input("Last name: ").capitalize(), \
            input("Age: ").lower(), \
            input("E-mail: ").lower(), \
            input("Programming Course: ").lower()

    except Exception("Oops something is buggy"):
        print("\nOops something is buggy")

    # Defining new student object from entered info.
    studentObject = database(fodselsNummer, firstName, lastName, age, email, programmingCourse)

    # Appends student object into StudentRecords.txt file.
    studentObject.addToFile()


# Queries the user for which programming course to display students from.
# It's very short, but I think it seems cleaner to have it here.
def GetSubjectName():
    programmingCourses = ["Python", "Java", "C", "Php", "Ruby"]

    try:
        # Capitalize() to convert to "Python" in case they write "python".
        subjectname = input("\nSpecify programming course: ").capitalize()

        if subjectname not in programmingCourses:
            print("\nWe do not offer that course.\nPlease specify one of {}."
                  .format(str(programmingCourses).strip('[]')))
            GetSubjectName()

    except Exception("Oops something is buggy"):
        # Task specifies to catch all exceptions like this, even though style guide
        # suggests "Too broad exception clause".
        print("\nOops something is buggy")

    return subjectname


def DisplayOptions():
    """Queries the user on"""

    try:
        # Ask for user input.
        # textwrap.dedent() removes the indentations from the string.
        userInput = input(dedent("""
                                              1. Would you like to see a list of all registered students?
                                              2. Would you like to see a class list for a specific subject?
                                              3. Would you like to see who your oldest student is?
                                              4. Would you like to see who your youngest student is?
                                              Enter a number for the selected task, or X to skip this: """))

    except Exception("Oops something is buggy"):
        # Task specifies to catch all exceptions like this, even though style guide
        # suggests "Too broad exception clause".
        print("\nOops something is buggy")

    # Check if userInput points to either of the options, and recursively call
    # the DisplayOptions() function until userInput has an actionable value.
    if userInput not in ["1", "2", "3", "4", "X", "x"]:
        print("\nPlease select either 1, 2, 3, 4 or X.")
        DisplayOptions()

    # Execute functions depending on the value of userInput.
    elif userInput == "1":
        database.DisplayAllStudents()
    elif userInput == "2":
        database.displaySubjectClassList(GetSubjectName())  # Get subject name first.
    elif userInput == "3":
        database.DisplayOldest()
    elif userInput == "4":
        database.DisplayYoungest()
    elif userInput.upper() == "X":
        EncryptOption()


def EncryptOption():
    """Queries the user about encrypting the student records file."""

    try:
        userInput = input("\nWould you like to encode a copy of the student records? Type Y for Yes or N for No: ")\
                     .upper()

        if userInput not in ["Y", "N"]:
            print("\nPlease select either Y or N.")
            EncryptOption()

        elif userInput == "Y":
            crypto.EncodeStudentList('StudentRecords.txt', 5)

        elif userInput == "N":
            DecryptOption()

    except Exception("Oops something is buggy"):
        print("\nOops something is buggy")


def DecryptOption():
    try:
        userInput = input("\nWould you like to decode the encoded file? Y/N: ").upper()

        if userInput not in ["Y", "N"]:
            print("\nPlease select either Y or N.")
            DecryptOption()

        elif userInput == "Y":
            crypto.DecodeStudentList('EncryptedRecords.txt', -5)

        elif userInput == "N":
            print("\nThe assessment is over. Have a nice day.")

    except Exception("Oops something is buggy"):
        print("\nOops something is buggy")


# Main entry point for the program. Only executes if this .py file is run.
if __name__ == "__main__":
    while True:
        try:
            # Ask for user input, convert to upper case.
            userInput = input("\nWould you like to enter a student's information? " +
                               "Type Y for Yes and N for No: ").upper()

            if userInput == "Y":
                EnterStudentInfo()
                continue  # Continues the loop after running EnterStudentInfo().

            elif userInput == "N":
                DisplayOptions()
                break  # Breaks out of the loop if user types N.

            else:
                print("\nPlease select either Y or N.")

        except Exception("Oops something is buggy"):
            # Task specifies to catch all exceptions like this, even though style guide
            # suggests "Too broad exception clause".
            print("\nOops something is buggy")
