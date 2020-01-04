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

    with open('StudentRecords.txt', 'r') as file:  # Open in 'read' mode.
        student_records = file.read()  # Gets the whole file as raw text.
        student_records = student_records.splitlines()  # Converts the string to a list of all the lines in the text.

        for student_record in student_records:

            # 'student_record' currently contains a string of info for a single student.
            # .split makes a list out of each piece of info separated by a comma in the string.
            student_record = student_record.split(',')

            # Makes a StudentRecordClass object based on student_record.
            # '*student_record' is a quick way to unpack the list, to pass
            # each item as an argument into the function.
            student_object = StudentRecordClass(*student_record)

            # Appends the student_object to the list of student_objects.
            student_objects.append(student_object)

    return student_objects


def displayAllStudents():
    # Style guide suggests functions should be snake case instead of CamelCase contrary to task specification.

    # Get a list of all student objects.
    student_objects = getStudentObjects()

    print("\nThe students registered are:")
    for student in student_objects:
        student.displayName()


def displaySubjectClassList(subjectname):
    # Parameter variable name is missing an underscore, but it's how it was specified in the assessment doc.

    # Get a list of all student objects.
    student_objects = getStudentObjects()

    # Filtering the list based on programming course using list comprehension.
    subject_takers = [student for student in student_objects if student.programmingCourse == subjectname.lower()]

    # Prints the names of students that take the specified programming course.
    print("\nThe students registered for {} are:".format(subjectname))
    for student in subject_takers:
        student.displayName()


def displayOldest():

    # Get a list of all student objects.
    student_objects = getStudentObjects()

    # Find the age of the oldest student(s)
    for i, student in enumerate(student_objects):
        student_age = int(student.age)  # Convert from str to int.

        # If student_age is larger than oldest_age, sets oldest_age to it.
        # But oldest_age is not defined for the first iteration, so condition
        # is also fulfilled if it's the first iteration (i.e. i == 0).
        if i == 0 or student_age > oldest_age:
            oldest_age = student_age

    # Searches through the student list, and adds all the students with the oldest age to a string.
    oldest_students = ""
    for student in student_objects:
        if int(student.age) == oldest_age:
            oldest_students += "{} {}, ".format(student.firstName.capitalize(), student.lastName.capitalize())
    oldest_students = oldest_students[:-2]  # Remove ", " at the end of the string.

    # Print results
    print("\nThe eldest student(s) is/are {}. They are {}."
          .format(oldest_students, oldest_age))


def displayYoungest():
    # Get a list of all student objects.
    student_objects = getStudentObjects()

    # Find the age of the oldest student(s)
    # youngest_age = 999  # Start from 999, and search downward.
    for student in student_objects:
        student_age = int(student.age)  # Convert from str to int.

        # Does the same thing as in displayOldest(), except this time condition
        # tests to see if variable is undefined by trying to run the code, and
        # defining youngest_age if it is not already defined.
        try:
            if student_age < youngest_age:
                youngest_age = student_age
        except NameError:  # Catches a NameError if a variable is not defined.
            youngest_age = student_age

    # Searches through the student list, and adds all the students with the youngest age to a string.
    youngest_students = ""
    for student in student_objects:
        if int(student.age) == youngest_age:
            youngest_students += "{} {}, ".format(student.firstName.capitalize(), student.lastName.capitalize())
    youngest_students = youngest_students[:-2]  # Remove ", " at the end of the string.

    # Print results
    print("\nThe youngest student(s) is/are {}. They are {}."
          .format(youngest_students, youngest_age))
