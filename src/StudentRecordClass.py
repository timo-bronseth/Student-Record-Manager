
if __name__ == "__main__":
    print(__name__)

class StudentRecordClass:

    # This is the constructor for the class.
    # "self" here points to the memory locations in which the student instance will be stored.
    # Basically, when you define a new object in the class (e.g. john = StudentRecordClass(details)),
    # the class receives the "john" pointer as the first argument automatically, so we don't need to
    # call the class with "john" as an additional argument.
    # Using the name "self" for the instance is optional, but it's very much the convention.
    # The keyword "this" is often used instead of "self" for other languages, like C# and Java.
    def __init__(self, fodselsNummer, firstName, lastName, age, email, programmingCourse):

        # The following lines define the properties/attributes/fields of the instance/object from the arguments.
        self.fodselsNummer = fodselsNummer
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.email = email
        self.programmingCourse = programmingCourse

        # A method for this class. Can be called like this "objectName.displayName()".
        def displayName():
            # TODO: Need "self" as an argument, because instance is automatically
            # TODO: passed as an argument whenever calling this method, and that would cause a
            # TODO: mismatch between arguments passed and received?
            print("Name:", firstName, lastName)
            print("Name: {} {}".format(firstName, lastName))  # Is there any difference between these two?
            # Is it better to access these variables via the instance ("self.firstName") or the class (firstName)?


def DisplayAllStudents():
    # Style guide suggests functions should be lower case contrary to task specification.
    pass


def DisplaySubjectClassList():
    pass


def DisplayOldest():
    pass


def DisplayYoungest():
    pass

