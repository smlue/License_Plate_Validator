# License_Plate_Validator
The function implemented verifies the validity for a Czech license plate and differentiates the type of license plate. This is either regular, electrical, or custom. License plates for special vehicles, persons with diplomatic privileges, historical and sports vehicles, etc. are not distinguished and thus fall under the invalid license plates.
## Universal rules for any (valid) license plate:
A license plate is always a sequence of digits and uppercase letters (only Arabic numerals and Latin letters without diacritics).
The letters G, O, Q, and W cannot be used due to their easy confusion with other characters.
The Czech letter "CH" is not a single Latin letter; it consists of two Latin letters.
A license plate must contain at least one digit, meaning it cannot consist solely of letters.
It must not contain any other characters such as -, *, /, ?, !, §, etc.
Whitespace characters are also not allowed (except as described in the previous paragraph).
## Standard passenger car license plate:
A string containing 7 characters.
It has the format DLDLLLL, where:
D represents any decimal digit (the first character of the string cannot be zero).
L represents any allowed letter.
Z represents any allowed character (letter or digit).
The letter after the first digit represents the region code (see regional codes).
Exception for Prague (effective from 2023): If the region code in the second position corresponds to Prague, then the fourth position may contain any allowed letter instead of a digit.
## Custom license plate:
A string containing 7 or 8 characters.
It does not meet at least one criterion of a standard license plate but adheres to all universal rules.
It does not start with the EL prefix.
## License plate for electric vehicles:
A string containing 7 characters.
It follows the format ELDDDZZ, where:
EL is the prefix.
DDD represents three digits.
ZZ represents two allowed characters at the end (letters or digits).
