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


# TODO: StudentManagement
# # DONE: enter_info()
# # DONE: displayOptions()
# # TODO: Custom exception?

# TODO: StudentRecordClass
# # DONE: DisplayAllStudents()
# # TODO: DisplaySubjectClassList()
# # TODO: DisplayOldest()
# # TODO: DisplayYoungest()

# TODO: EncodeDecodeClass
# # TODO: EncodeStudentList()
# # TODO: DecodeStudentList()


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

    print("\n\n")


def displayOptions():
    try:
        # Ask for user input.
        user_input = input("\n" +
                           "1. Would you like to see a list of all registered students?\n" +
                           "2. Would you like to see a class list for a specific subject?\n" +
                           "3. Would you like to see who your oldest student is?\n" +
                           "4. Would you like to see who your youngest student is?\n" +
                           "Enter a number for the selected task, or X to skip this: ")

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
        displaySubjectClassList()
    elif user_input == "3":
        displayOldest()
    elif user_input == "4":
        displayYoungest()
    elif user_input.upper() == "X":
        print("X")


if __name__ == "__main__":

    while True:
        try:
            # Ask for user input, convert to upper case.
            user_input = input("Would you like to enter a student's information? " +
                               "Type Y for Yes and N for No: ").upper()

        except Exception("Oops something is buggy"):
            # Task specifies to catch all exceptions like this, even though style guide
            # suggests "Too broad exception clause".
            print("Oops something is buggy")

        # Using a ternary operator to make the code cleaner. Idk how this affects speed.
        entering_info = True if user_input == "Y" else False if user_input == "N" else None  # Ternary operator

        if entering_info:
            enterStudentInfo()
            continue  # Continues the loop after running enter_info().

        elif entering_info is False:
            displayOptions()
            break  # Breaks out of the loop if user types N.

        # Only runs if Y or N is not typed.
        # We do not need to wrap the following line in an else clause, so we can save on
        # execution time by omitting it.
        print("Please enter either Y or N.")
