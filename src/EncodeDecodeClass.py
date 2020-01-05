# -------------------------------------------------------------------------------------
# Timo Brønseth, January 2020.
# -------------------------------------------------------------------------------------
import string


def _SwapNumCipher(cipherText: str):
    """For internal use."""

    # cipherText = cipherText.split(',')

    print(cipherText)

    return cipherText

class EncodeDecodeClass:
    """Encrypt or decrypt a file."""

    # Class constants
    _ALPHABET = string.ascii_lowercase

    def __init__(self, fileName='StudentRecords.txt'):
        """Class constructor."""

        self.fileName = fileName

    @classmethod
    def EncodeStudentList(cls, fileName='StudentRecords.txt', numShifts = 5):
        """Takes a plaintext, encrypts it, and returns a ciphertext.

        It uses a Ceasar Cipher, which works by shifting each letter in the text n letters forward
        in the alphabet. It also changes numbers by swapping the last and first digits."""

        # Open the original StudentRecords.txt file.
        with open(fileName, 'r') as originalFile:
            studentRecords = originalFile.read()  # Converts into list of characters.

        # Encrypt the contents of the file.
        encryptedRecords = cls.CaesarShiftPlus(studentRecords, 5)

        # Open the EncryptedRecords.txt file, or create it if it does not exist.
        with open('EncryptedRecords.txt', 'w') as encryptedFile:  # 'w' mode replaces text as necessary.

            # Write the encrypted contents into the file.
            encryptedFile.write(encryptedRecords)

    def DecodeStudentList(self):
        """..."""

    @classmethod
    def CaesarShiftPlus(cls, plainText, numShifts: int):
        """Takes a plaintext, encrypts it, and returns a ciphertext.

        It uses a Ceasar Cipher, which works by shifting each letter in the text n letters forward
        in the alphabet. It also changes numbers by swapping the last and first digits."""

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

        # Applies the SwapNumCipher, swapping the first and last digit for each number in the text.
        cipherText = _SwapNumCipher(cipherText)

        return cipherText

    # @staticmethod
    # Using the @staticmethod decorator and including this function inside the class,
    # because the function purpose is closely associated with the rest of the class.
