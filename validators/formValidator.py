import re


class FormValidator:

    @staticmethod
    def FieldTooShort(field, minLen):
        if len(field) < minLen:
            return True
        else:
            return False

    @staticmethod
    def FieldTooLong(field, maxLen):
        if len(field) > maxLen:
            return True
        else:
            return False
    
    @staticmethod
    def ValidText(field):
        if re.fullmatch(r"[\w\s.@#$!?']+", field):
            return False
        else:
            return True
    
    @staticmethod
    def FieldOutOfRange(field, minLen, maxLen):
        if len(field) < minLen or len(field) > maxLen:
            return True
        else:
            return False

    @staticmethod
    def EmailInvalid(email):
        if re.fullmatch(r"[a-zA-Z0-9]+@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)+", email):
            return False
        else:
            return True

    @staticmethod
    def PasswordValid(password):
        specialChars = ['!', '@', '#', '$', '%', '&']
        if password is None:
            return False
        elif len(password) < 8:
            return False
        elif not any(char.islower() for char in password):
            return False
        elif not any(char.isupper() for char in password):
            return False
        elif not any(char.isdigit() for char in password):
            return False
        elif not any(char in specialChars for char in password):
            return False
        else:
            return True
    
    @staticmethod
    def GenderInvalid(gender):
        if gender is not 0 or 1:
            return False
        else:
            return True
    
    @staticmethod
    def AgeInvalid(age):
        if (age < 18) or (age > 100):
            return True
        else:
            return False
