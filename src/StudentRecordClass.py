class StudentRecordClass:
    # Class variables
    num_students = 0

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
    def displayName(self):
        # TODO: Need "self" as an argument, because instance is automatically
        # TODO: passed as an argument whenever calling this method, and that would cause a
        # TODO: mismatch between arguments passed and received?
        print("{} {}".format(self.firstName, self.lastName))
        # String in the code is easier to read when using the format() method.

    # Takes the student record object and returns the attribute values in a formatted string.
    def formatRecord(self):
        formattedStudentRecord = "\n"  # Start the string with a newline.

        # Gets a dictionary representation of the object, and converts it to a list.
        values = list(self.__dict__.values())

        # Iterates through the list, appending each value to the string, separated by a comma.
        for value in values[:-1]:
            formattedStudentRecord += value + ","
        formattedStudentRecord += values[-1]  # Adding the last item without ending on a comma.

        return formattedStudentRecord

    # TODO: COMMENT
    def addToFile(self):
        print("Writing student information to Student Record File...")

        # Opening the file with context manager.
        # This is cleaner and has superior functionality compared to just using file = open().
        # This creates file if it doesn't already exist.
        with open('StudentRecords.txt', "a") as studentRecords:  # a for append mode.
            studentRecords.write(self.formatRecord())  # formatRecord() is a method of the class.
        StudentRecordClass.num_students += 1  # Iterate the class variable.


# Returns a list of all the student objects in the StudentRecords.txt file.
def getStudentObjects():
    student_objects = []  # Initialise the list.

    with open('StudentRecords.txt', 'r') as studentRecords:  # Open in 'read' mode.
        students_info = studentRecords.read()  # Gets the whole file as raw text.
        students_info = students_info.splitlines()  # Converts the string to a list of all the lines in the text.

        for student_info in students_info:

            # 'student_info' currently contains a string of info for a single student.
            # .split makes a list out of each piece of info separated by a comma in the string.
            student_info = student_info.split(',')

            # Makes a StudentRecordClass object based on student_info.
            # '*student_info' is a quick way to unpack the list, to pass
            # each item as an argument into the function.
            student_object = StudentRecordClass(*student_info)

            # Appends the student_object to the list of student_objects.
            student_objects.append(student_object)

    return student_objects


def displayAllStudents():
    # Style guide suggests functions should be snake case instead of CamelCase contrary to task specification.

    student_objects = getStudentObjects()

    print("\nThe students registered are:")
    for student in student_objects:
        student.displayName()


def displaySubjectClassList():
    print("displaySubjectClassList")
    pass


def displayOldest():
    print("displayOldest")
    pass


def displayYoungest():
    print("displayYoungest")
    pass
