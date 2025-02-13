def analyze_license_plate(plate):

    plate = plate.strip()

    if len(plate) > 4 and plate[3] == " ": #removes valid space in plate
        plate = plate[:3] + plate[4:]
    
    for el in plate: #checks for a space inside plate
        if el == " ":
            return "invalid"
            
    if len(plate) != 7 and len(plate)  != 8:
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
