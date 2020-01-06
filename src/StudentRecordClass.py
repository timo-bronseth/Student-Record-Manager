# -------------------------------------------------------------------------------------
# Timo Brønseth, January 2020.
# -------------------------------------------------------------------------------------


# Function name starts with an underscore to indicate that it's for internal
# module use only. It gets excluded from module when module is imported.
def _GetStudentObjects():
    """Returns a list of all the student objects in StudentRecords.txt file."""
    studentObjects = []  # Initialise the list.

    with open('StudentRecords.txt', 'r') as file:  # Open in 'read' mode.
        studentRecords = file.read()  # Gets the whole file as raw text.
        studentRecords = studentRecords.splitlines()  # Converts the string to a list of all the lines in the text.

        for studentRecord in studentRecords:
            # 'studentRecord' currently contains a string of info for a single student.
            # .split makes a list out of each piece of info separated by a comma in the string.
            studentRecord = studentRecord.split(',')

            # Makes a StudentRecordClass object based on studentRecord.
            # '*studentRecord' is a quick way to unpack the list, to pass
            # each item as an argument into the function.
            studentObject = StudentRecordClass(*studentRecord)

            # Appends the studentObject to the list of studentObjects.
            studentObjects.append(studentObject)

    return studentObjects


class StudentRecordClass:
    """Manipulate a database of student records."""

    # This is the constructor for the class.
    # "self" here points to the memory locations in which the student instance will be stored.
    # Basically, when you define a new object in the class (e.g. john = StudentRecordClass(details)),
    # the class receives the "john" pointer as the first argument automatically, so we don't need to
    # call the class with "john" as an additional argument.
    # Using the name "self" for the instance is optional, but it's very much the convention.
    # The keyword "this" is often used instead of "self" for other languages, like C# and Java.
    def __init__(self, fodselsNummer, firstName, lastName, age, email, programmingCourse):
        """Class constructor."""

        # The following lines define the properties/attributes/fields of the instance/object from the arguments.
        self.fodselsNummer = fodselsNummer
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.email = email
        self.programmingCourse = programmingCourse

    # A method for this class. Can be called like this "objectName.DisplayName()".
    def DisplayName(self):
        """Accessor method. Prints the name variables from the student instance object."""

        print("{} {}".format(self.firstName.capitalize(), self.lastName.capitalize()))

    def FormatRecord(self):
        """Takes the student record object and returns the attribute values in a formatted string."""

        formattedStudentRecord = "\n"  # Start the string with a newline.

        # Gets a dictionary representation of the object, and converts it to a list.
        values = list(self.__dict__.values())

        # Iterates through the list, appending each value to the string, separated by a comma.
        for value in values[:-1]:
            formattedStudentRecord += value + ","
        formattedStudentRecord += values[-1]  # Adding the last item without ending on a comma.

        return formattedStudentRecord

    def addToFile(self):
        """Mutator method. Writes a formatted record into the StudentRecords.txt file."""

        print("\nWriting student information to Student Record File...")

        # Opening the file with context manager.
        # This is cleaner and has superior functionality compared to just using file = open().
        # This creates file if it doesn't already exist.
        with open('StudentRecords.txt', 'a') as studentRecords:  # a for append mode.
            studentRecords.write(self.FormatRecord())  # FormatRecord() is a method of the class.

    @staticmethod
    # The @staticmethod decorator is just a way of telling the interpreter that this function
    # should not automatically be passed an object instance (i.e. "self") as the first argument.
    # I'm using it because then I can include these functions inside the class.
    def DisplayAllStudents():
        """Accessor method. Loops through list of student objects and calls DisplayName() on them."""

        # Get a list of all student objects.
        studentObjects = _GetStudentObjects()

        print("\nThe students registered are:")
        for student in studentObjects:
            student.DisplayName()

    @staticmethod
    # Parameter variable name is missing an underscore, but it's how it was specified in the assessment doc.
    def DisplaySubjectClassList(subjectname):
        """Accessor method. Prints all the students who currently take a specific programming course."""

        print("DisplaySubject {}.".format(subjectname))
        # Get a list of all student objects.
        studentObjects = _GetStudentObjects()

        # Filtering the list based on programming course using list comprehension.
        subjectTakers = [student for student in studentObjects if student.programmingCourse == subjectname]

        # Prints the names of students that take the specified programming course.
        print("\nThe students registered for {} are:".format(subjectname.capitalize()))
        for student in subjectTakers:
            student.DisplayName()

    @staticmethod
    def DisplayOldest():
        """Accessor method. Displays oldest student(s)."""

        # Get a list of all student objects.
        studentObjects = _GetStudentObjects()

        # Find the age of the oldest student(s)
        for i, student in enumerate(studentObjects):
            studentAge = int(student.age)  # Convert from str to int.

            # If studentAge is larger than oldestAge, sets oldestAge to it.
            # But oldestAge is not defined for the first iteration, so condition
            # is also fulfilled if it's the first iteration (i.e. i == 0).
            if i == 0 or studentAge > oldestAge:
                oldestAge = studentAge

        # Searches through the student list, and adds all the students with the oldest age to a string.
        oldestStudents = ""
        for student in studentObjects:
            if int(student.age) == oldestAge:
                oldestStudents += "{} {}, ".format(student.firstName.capitalize(), student.lastName.capitalize())
        oldestStudents = oldestStudents[:-2]  # Remove ", " at the end of the string.

        # Print results
        print("\nThe eldest student(s) is/are {}. They are {}."
              .format(oldestStudents, oldestAge))

    @staticmethod
    def DisplayYoungest():
        """Accessor method. Displays the youngest student(s)."""

        # Get a list of all student objects.
        studentObjects = _GetStudentObjects()

        # Find the age of the youngest student(s)
        for student in studentObjects:
            studentAge = int(student.age)  # Convert from str to int.

            # Does the same thing as in DisplayOldest(), except this time condition
            # tests to see if variable is undefined by trying to run the code, and
            # defining youngestAge if it is not already defined.
            try:
                if studentAge < youngestAge:
                    youngestAge = studentAge
            except NameError:  # Catches a NameError if a variable is not defined.
                youngestAge = studentAge

        # Searches through the student list, and adds all the students with the youngest age to a string.
        youngestStudents = ""
        for student in studentObjects:
            if int(student.age) == youngestAge:
                youngestStudents += "{} {}, ".format(student.firstName.capitalize(), student.lastName.capitalize())
        youngestStudents = youngestStudents[:-2]  # Remove ", " at the end of the string.

        # Print results
        print("\nThe youngest student(s) is/are {}. They are {}."
              .format(youngestStudents, youngestAge))
