# -------------------------------------------------------------------------------------
# Timo Brønseth, January 2020.
# -------------------------------------------------------------------------------------
import string


def _SwapDigits(cipherText: str) -> str:  # Using type hints to show that both arg and return val should be string.
    """Swaps the first and last digits of any numbers found in the string.

    For internal use.

    Symmetric: can be used to encrypt and decrypt."""

    # Get list of lines in cipherText.
    cipherTextLines = cipherText.split('\n')  # cipherTextLines is a list of strings.

    # Iterate over all lines.
    for i, line in enumerate(cipherTextLines):

        # Get list of items in line.
        lineItems = line.split(',')  # lineItems is a list of strings.

        # Iterate over all items in the line.
        for j, item in enumerate(lineItems):

            # Only proceed with items that can be converted to integers.
            try:
                int(item)
            except ValueError:  # If item cannot be converted to integer...
                continue  # Skip to next item in list.

            # Make a list of digits (as strings) from the integer.
            digits = list(item)  # digits is a list of strings.

            # Using unpacking, we are able to swap the first and last digits in a single line of code.
            digits[0], digits[-1] = digits[-1], digits[0]

            # Insert the list of digits it back into lineItems as a string.
            lineItems[j] = "".join(digits)

        # Insert the line back into cipherTextLines as a string.
        cipherTextLines[i] = ",".join(lineItems)

    # Insert the cipherTextLines back into cipherText as a string.
    cipherText = "\n".join(cipherTextLines)

    return cipherText


class EncodeDecodeClass:
    """Encrypt or decrypt a file."""

    # Internal class constant
    _ALPHABET = string.ascii_lowercase

    def __init__(self, fileName='StudentRecords.txt'):
        """Class constructor."""
        self.fileName = fileName

    @classmethod
    def EncodeStudentList(cls, fileName='StudentRecords.txt', numShifts=5) -> str:
        """Takes a plaintext, encrypts it, and returns a ciphertext.

        It uses a 5-shifted Ceasar Cipher (aka ROT(5)), which works by shifting each letter
        in the text 5 letters forward in the alphabet. It also encrypts numbers by swapping
        the last and first digits."""

        # Open the original StudentRecords.txt file.
        with open(fileName, 'r') as originalFile:
            studentRecords = originalFile.read()

        # Encrypt the contents of the file.
        encryptedRecords = cls.CaesarShiftPlus(studentRecords, numShifts)

        # Open the EncryptedRecords.txt file, or create it if it does not exist.
        with open('EncryptedRecords.txt', 'w') as encryptedFile:  # 'w' mode replaces text as necessary.

            # Write the encrypted contents into the file.
            encryptedFile.write(encryptedRecords)

        print("\nFile encoded.")

    @classmethod
    def DecodeStudentList(cls, fileName='EncryptedRecords.txt', numShifts=-5) -> str:  # Notice numShifts is -5 now.
        """Takes a ciphertext, decrypts it, and returns a plaintext.

        This is the symmetric opposite of EncodeStudentList(), except that it stores the
        decoded contents into a new file, DecodedStudentRecords.txt.

        Notice that numShifts is -5 by default here, as opposed to 5 in EncodeStudentList()."""

        # Open the encrypted EncryptedRecords.txt file.
        with open(fileName, 'r') as encryptedFile:
            encryptedRecords = encryptedFile.read()

        # Decrypt the contents of the file.
        decryptedRecords = cls.CaesarShiftPlus(encryptedRecords, numShifts)

        # Open the DecodedStudentRecords.txt file, or create it if it does not exist.
        with open('DecodedStudentRecords.txt', 'w') as decryptedFile:

            # Write the decrypted contents into the file.
            decryptedFile.write(decryptedRecords)

        print("\nFile decoded.")

    @classmethod
    def CaesarShiftPlus(cls, plainText: str, numShifts: int) -> str:
        """Takes a plaintext, encrypts it, and returns a ciphertext.

        It uses a Ceasar Cipher, which works by shifting each letter in the text n letters forward
        in the alphabet. It also changes numbers by swapping the last and first digits.

        It is bidirectional, so can be used to encrypt and decrypt (with negative numShifts)."""

        # cipherText starts out as a plaintext list, and then gets encrypted.
        cipherText = list(plainText)  # Converts string to a list of characters.

        # Implement the Caesar shift.
        for i, character in enumerate(plainText):
            character = character.lower()  # Convert to lower case.
            if character in cls._ALPHABET:
                indexInAlphabet = cls._ALPHABET.find(character)
                cipherText[i] = cls._ALPHABET[(indexInAlphabet + numShifts) % 26]

        # Converts cipherText from list of characters to a string.
        cipherText = "".join(cipherText)

        # Applies the SwapDigits cipher, swapping the first and last digit for each number in the text.
        cipherText = _SwapDigits(cipherText)

        return cipherText

    # @staticmethod
    # Using the @staticmethod decorator and including this function inside the class,
    # because the function purpose is closely associated with the rest of the class.
