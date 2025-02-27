def analyze_license_plate(plate):

    plate = plate.strip() #remove whitespace

    if len(plate) > 4 and plate[3] == " ": #removes a valid space in plate
        plate = plate[:3] + plate[4:]
    
    for el in plate: #checks for an invalid space inside plate
        if el == " ":
            return "invalid"
            
    if len(plate) != 7 and len(plate)  != 8: #checks for correct length of a valid license plate
        return "invalid"
        
    count = 0
    for el in plate:
        if not(el.isascii() and el.isalnum()):
            return "invalid"
        if not(el.isupper()) and el.isalpha():
            return "invalid"
        if el.isdecimal():
            count += 1
    
    if count == 0:
        return "invalid"

    for letter in "GOQW":
        if letter in plate:
            return "invalid"

    standard = True
    regions = "ASULKHEPCJBMTZ"

    if len(plate) == 7:
        if plate[0] == "0":
            standard = False
        for i in range(0, 7):
            element = plate[i]
            if i == 1:
                if not(element in kraje):
                    standard = False
                    break
            elif i == 2:
                if not(element.isascii() and element.isalnum()):
                    standard = False
            elif i == 3:
                if plate[1] != "A" and not element.isdigit():
                    standard = False
            else:
                if not element.isdigit():
                    standard = False
                
    else:
        standard = False

    if standard:
        return "standard"
    elif ((len(plate) == 7 or len(plate) == 8) and standard == False):
        if not (plate[0] == "E" and plate[1] == "L"):
            return "custom"
    elif ((len(plate) == 7 ) and plate[0] == "E" and plate[1] == "L" and plate[2].isdecimal() and plate[3].isdecimal() and plate[4].isdecimal()):
        return "electric"
    else:
        return "invalid"   


#SOME TEST_CASES

short_plates = [
    "",
    " ",
    " 1 ",
    " 1A ",
    " 1A2 3 ",
    " 1A2 34 ",
    " 1A2 345 ",
]
for plate in short_plates:
    try:
        analyze_license_plate(plate)
    except IndexError:
        print(f"TEST FAILED for plate {repr(plate)}")
        print("Try to analyze the function's input argument more carefully.")
        raise
    assert isinstance(analyze_license_plate(plate), str), "Your function does not return str object."
print("test OK")

plate_with_spaces = "   TRY PTHN1  "
assert analyze_license_plate(plate_with_spaces) == "custom", "You may have some problem with spaces."
print("test OK")

plate_with_spaces = "2RY  HARD"
assert analyze_license_plate(plate_with_spaces) == "invalid", "You may have some problem with spaces."
print("test OK")

standard_plate = "1A10000"
assert analyze_license_plate(standard_plate) == "standard", "Check your criteria for standard plate."
print("test OK")

only_digits_plate = "1234567"
assert analyze_license_plate(only_digits_plate) == "custom", "Check your criteria for custom plate."
print("test OK")

not_a_plate = "L1KEZPRO"
assert analyze_license_plate(not_a_plate) == "invalid", "Check your criteria for custom plate."
print("test OK")

invalid_plates = {
    "1S711-11": "invalid",
    "IAMTHE1!": "invalid",
    "LOVEZPR0": "invalid",
    "1aA0987":  "invalid",
    "1AA":      "invalid",
    "4PZ 000":  "invalid",
    "3AČ0123":  "invalid",
}

for test_case, result in invalid_plates.items():
    assert analyze_license_plate(test_case) == result, "test case: " + test_case
print("test OK")

standard_plates = {
    "9BU 0000   ": "standard",
    "3A40123\n":   "standard",
    "\t2CH0987":   "standard",
    "1CH 2345":    "standard",
}

for test_case, result in standard_plates.items():
    assert analyze_license_plate(test_case) == result,  "test case: " + test_case
print("test OK")

plates_with_spaces = {
    "   1AA0987   ": "standard",
    "1AA 0987":      "standard",
    "1AA  0987":     "invalid",
    "1A A0987":      "invalid",
    "ABCDE F1":      "invalid",
}

for test_case, result in plates_with_spaces.items():
    assert analyze_license_plate(test_case) == result, "test case: " + test_case
print("test OK")

custom_plates = {
    "L0V EZPR0": "custom",
    "FERRARI1":  "custom",
    "JAN H0NZA": "custom",
    "UV1D1ME":   "custom",
    "UVIDIME1":  "custom",
    "0PRAVIME":  "custom",
    "KABAT123":  "custom",
    "LACHTAN1":  "custom",
    "1234567":   "custom",
    "12345678":  "custom",
}

for test_case, result in custom_plates.items():
    assert analyze_license_plate(test_case) == result, "test case: " + test_case
print("test OK")

electric_plates = {
    "EL12345": "electric",
    "EL1 2345": "electric",
    "EL 12345": "invalid",
    "EL123ZZ": "electric",
    "EL123OO": "invalid",
    "EL121LE": "electric",
    "ELF ORIN": "invalid",
}

for test_case, result in custom_plates.items():
    assert analyze_license_plate(test_case) == result, "test case: " + test_case
print("test OK")

all_letters_plates = {
    "KAPITAN":  "invalid",
    "":  "invalid",
    "101 010101":  "invalid",
    "1010 1010":  "invalid",
    "XXXXXXXX": "invalid",
    "TRY HARD": "invalid",
    "LACHTAN":  "invalid",
}

for test_case, result in all_letters_plates.items():
    assert analyze_license_plate(test_case) == result, "test case: " + test_case
print("test OK")
