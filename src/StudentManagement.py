# -------------------------------------------------------------------------------------
# Takes student information as input (fodselsNummer, firstName, lastName, age, email, programmingCourse)
# and stores it in a structured records file. The file should be searchable.
#
# Timo Brønseth, January 2020
# -------------------------------------------------------------------------------------
from StudentRecordClass import StudentRecordClass
from EncodeDecodeClass import EncodeDecodeClass

# TODO: StudentManagement
#   TODO: enter_info()
#   TODO: do_something_else()

# TODO: StudentRecordClass
#   TODO: DisplayAllStudents()
#   TODO: DisplaySubjectClassList()
#   TODO: DisplayOldest()
#   TODO: DisplayYoungest()

# TODO: EncodeDecodeClass
#   TODO: EncodeStudentList()
#   TODO: DecodeStudentList()


def enter_info():
    print("Writing student information to Student Record File...")
    print("\n\n")


def do_something_else():
    print("N")
    print("\n\n")


if __name__ == "__main__":

    # This is very neat and all, but not very functional.
    # # Runs query_user() until it returns something other than None.
    # while welcome_query() is None:
    #     print("Please enter either Y or N.")
    #     continue

    # The advantage of this formulation is that we do not need to define "entering_info"
    # before we use it as a condition for the while loop. If entering_info is undefined,
    # then that too is "not True or False", therefore the loop will run.
    while True:
        try:
            # Ask for user input
            user_input = input("Would you like to enter a student's information? Type Y for Yes and N for No: ")
        except Exception("Oops something is buggy"):
            # Task specifies to catch all exceptions like this, even though style guide
            # suggests "Too broad exception clause".
            print("Oops something is buggy")

        # Using a ternary operator to make the code cleaner. Idk how this affects speed.
        entering_info = True if user_input == "Y" else False if user_input == "N" else None  # Ternary operator

        if entering_info:
            enter_info()
            continue  # Continues the loop after running enter_info().

        elif entering_info is False:
            do_something_else()
            break  # Breaks out of the loop if user types N.

        # Only runs if Y or N is not typed.
        # We do not need to wrap the following line in an else clause, so we can save on
        # execution time by omitting it.
        print("Please enter either Y or N.")
