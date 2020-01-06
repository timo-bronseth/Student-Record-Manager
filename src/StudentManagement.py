# -------------------------------------------------------------------------------------
# This program provides an interface that allows the user to access and add to a
# student records Database. It also allows the user to encrypt and decrypt the file.
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
from StudentRecordClass import StudentRecordClass as Database
from EncodeDecodeClass import EncodeDecodeClass as Crypto
from ExceptionHandling import ExceptionHandlingClass as ExceptionHandling
from textwrap import dedent


def EnterStudentInfo():
    """Prompts the user to enter student information,
    and stores it in the StudentRecords.txt file."""

    # Querying user for student info, and converting to appropriate case.
    # Also tests for specific ValueErrors for each input.
    print("\nPlease fill out the student record form: ")
    fodselsNummer = ExceptionHandling.QueryInt("fodselsnummer")
    firstName = ExceptionHandling.QueryStr("first name").capitalize()
    lastName = ExceptionHandling.QueryStr("last name").capitalize()
    age = ExceptionHandling.QueryInt("age")
    email = ExceptionHandling.QueryStr("email").lower()
    programmingCourse = ExceptionHandling.QueryCourse("programming course").lower()

    # Defining new student object from entered info.
    studentObject = Database(fodselsNummer, firstName, lastName, age, email, programmingCourse)

    # Appends student object into StudentRecords.txt file.
    studentObject.addToFile()

    # Query the user if they wish to enter an additional student record.
    Main()


def DisplayOptions():
    """Provides the user the option of using several accessor methods to display information
    from the database."""

    # Ask for user input via the ErrorHandling method.
    # textwrap.dedent() removes the indentations from the string.
    queryString = dedent("""
                            1. Would you like to see a list of all registered students?
                            2. Would you like to see a class list for a specific subject?
                            3. Would you like to see who your oldest student is?
                            4. Would you like to see who your youngest student is?
                            Enter a number for the selected task, or X to skip this: """)
    errorPrompt = "\nPlease select either 1, 2, 3, 4 or X."
    conditionList = ["1", "2", "3", "4", "X"]
    userInput = ExceptionHandling.QueryStrGeneral(queryString, errorPrompt, conditionList)

    # Execute functions depending on the value of userInput.
    if userInput == "1":
        Database.DisplayAllStudents()
    elif userInput == "2":
        subjectname = ExceptionHandling.QueryCourse("programming course").lower()
        Database.DisplaySubjectClassList(subjectname)  # Get subject name first.
    elif userInput == "3":
        Database.DisplayOldest()
    elif userInput == "4":
        Database.DisplayYoungest()
    elif userInput.upper() == "X":
        EncryptOption()


def EncryptOption():
    """Queries the user about encrypting the student records file."""

    # Ask for user input via the ErrorHandling method.
    queryString = "\nWould you like to encode a copy of the student records? Type Y for Yes or N for No: "
    errorPrompt = "\nPlease select either Y or N."
    conditionList = ["Y", "N"]
    userInput = ExceptionHandling.QueryStrGeneral(queryString, errorPrompt, conditionList)

    if userInput == "Y":
        Crypto.EncodeStudentList('StudentRecords.txt', 5)

    elif userInput == "N":
        DecryptOption()


def DecryptOption():
    """Provides to the user the option to decode the encrypted records."""

    # Ask for user input via the ErrorHandling method.
    queryString = "\nWould you like to decode the encoded file? Y/N: "
    errorPrompt = "\nPlease select either Y or N."
    conditionList = ["Y", "N"]
    userInput = ExceptionHandling.QueryStrGeneral(queryString, errorPrompt, conditionList)

    if userInput == "Y":
        Crypto.DecodeStudentList('EncryptedRecords.txt', -5)

    elif userInput == "N":
        print("\nThe assessment is over. Have a nice day.")


def Main():
    """Main function for the Student Record Manager program."""

    # Ask for user input via the ErrorHandling method.
    queryString = "\nWould you like to enter a student's information? " + \
                  "Type Y for Yes and N for No: "
    errorPrompt = "\nPlease select either Y or N."
    conditionList = ["Y", "N"]
    userInput = ExceptionHandling.QueryStrGeneral(queryString, errorPrompt, conditionList)

    if userInput == "Y":
        EnterStudentInfo()

    elif userInput == "N":
        DisplayOptions()


# Main entry point for the program. Only executes if this .py file is run.
if __name__ == "__main__":
    Main()
