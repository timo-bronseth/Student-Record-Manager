# -------------------------------------------------------------------------------------
# Timo Brønseth, January 2020.
# -------------------------------------------------------------------------------------


class ExceptionHandlingClass:
    """All input queries to the user are handled via this class.

    First, inputs are checked for ValueErrors, and the user is queried
    for valid entries until there is not ValueError.

    Second, inputs are checked for all exceptions, just in case there
    are any that aren't ValueErrors. The program notifies the user that
    something is buggy, and then exits."""

    @classmethod
    def QueryInt(cls, varName: str) -> str:
        """Queries the user for an integer, and recursively calls itself
        until user has successfully entered an integer."""

        # userInput needs to be raised to global so that it can be updated
        # while recursively calling this function in the except clause.
        global userInput

        try:
            userInput = input("{}: ".format(varName.capitalize()))

            # Raises a ValueError if userInput cannot be recast as integer.
            if not userInput.isdigit():
                raise ValueError

        except ValueError:
            # Reprompt user for valid entry.
            print("\nPlease enter a valid {}.".format(varName))
            cls.QueryInt(varName)

        # If input somehow causes an error which is not a ValueError, this catches it,
        # and prints the error message "Oops something is buggy".
        except Exception:
            # Only runs for errors which are not ValueErrors.
            # Assignment says to catch all input errors like this.
            # Don't blame me if it's silly!
            print("\nOops something is buggy")

        return userInput

    @classmethod
    def QueryStr(cls, varName: str) -> str:
        """Queries the user for a string, and recursively calls itself
        until user has successfully entered an string."""

        global userInput

        try:
            userInput = input("{}: ".format(varName.capitalize()))

            # Raises a ValueError if userInput CAN be recast as integer.
            if userInput.isdigit():
                raise ValueError

        except ValueError:
            # Reprompt user for valid entry.
            print("\nPlease enter a valid {}.".format(varName))
            cls.QueryStr(varName)

        except Exception:
            print("\nOops something is buggy")

        return userInput

    @classmethod
    def QueryCourse(cls, varName: str) -> str:
        """Queries the user for a programming course string, and recursively
        calls itself until user has successfully entered such."""

        global userInput
        _programmingCourses = ["python", "java", "c", "php", "ruby"]

        try:
            userInput = input("{}: ".format(varName.capitalize()))

            # Raises a ValueError if userInput is not part of programmingCourses.
            if userInput.lower() not in _programmingCourses:
                raise ValueError

        except ValueError:
            # Reprompt user for valid entry.
            print("\nWe do not offer that course.\nPlease specify one of {}."
                  .format(str(_programmingCourses).strip('[]')))
            cls.QueryCourse(varName)

        except Exception:
            print("\nOops something is buggy")

        return userInput

    @classmethod
    def QueryStrGeneral(cls, queryString: str, errorPrompt: str, conditionList: list) -> str:
        """A more general version, with more arguments, to query user for a string."""

        global userInput

        try:
            userInput = input(queryString).upper()

            # Check if userInput points to either of the options, and recursively call
            # the function until userInput has an actionable value.
            if userInput not in conditionList:
                raise ValueError

        except ValueError:
            # Reprompt user for valid entry.
            print(errorPrompt)
            cls.QueryStr(queryString, errorPrompt, conditionList)

        except Exception:
            print("\nOops something is buggy")

        return userInput