"""
Source code for COS 255 Experiment 1.
@author Ben Gaudreau
@version 4 Feb 2024
"""
# String constants
binaryDigits = "01"
decimalDigits = "0123456789"
hexDigits = "0123456789ABCDEF"

# Base-10 and base-16 digit conversions
decimalDigitToHexDigit = {
    "0" : "0",
    "1" : "1",
    "2" : "2",
    "3" : "3",
    "4" : "4",
    "5" : "5",
    "6" : "6",
    "7" : "7",
    "8" : "8",
    "9" : "9",
    "10" : "A",
    "11" : "B",
    "12" : "C",
    "13" : "D",
    "14" : "E",
    "15" : "F"
    }
hexDigitToDecimalDigit = {
    "0" : "0",
    "1" : "1",
    "2" : "2",
    "3" : "3",
    "4" : "4",
    "5" : "5",
    "6" : "6",
    "7" : "7",
    "8" : "8",
    "9" : "9",
    "A" : "10",
    "B" : "11",
    "C" : "12",
    "D" : "13",
    "E" : "14",
    "F" : "15"
}

# Returns true if the input number contains only binary digits
def isBinary(num: str) -> bool:
    for n in num:
        if (not(n in binaryDigits)):
            return False
    return True
# Returns true if the input number contains only decimal digits
def isDecimal(num: str) -> bool:
    for n in num:
        if (not(n in decimalDigits)):
            return False
    return True
# Returns true if the input number contains only hexadecimal digits
def isHex(num: str) -> bool:
    for n in num.upper():
        if (not(n in hexDigits)):
            return False
    return True

# Methods to convert betwen base-2, base-10, and base-16
def binaryToDec(num: str) -> str:
    if (isBinary(num)):
        result = 0
        digit = 0
        for n in reversed(num):
            result += int(n) * 2**digit
            digit += 1
        return str(result)
    else:
        print("That is not a positive binary number!")
        exit()
def decToBinary(num: str) -> str:
    if (isDecimal(num)):
        inum = int(num)
        result = ""
        while (inum > 0):
            result = str(inum % 2) + result
            inum = inum >> 1
        return result
    else:
        print("That is not a positive decimal number!")
        exit()
def hexToDec(num: str) -> str:
    if (isHex(num)):
        result = 0
        digit = 0
        for n in reversed(num):
            result += int(hexDigitToDecimalDigit[n.upper()]) * 16**digit
            digit += 1
        return str(result)
    else:
        print("That is not a positive binary number!")
        exit()
def decToHex(num: str) -> str:
    if (isDecimal(num)):
        inum = int(num)
        result = ""
        while (inum > 0):
            result = decimalDigitToHexDigit[str(inum % 16)] + result
            inum = inum // 16
        return result
    else:
        print("That is not a positive decimal number!")
        exit()
def binaryToHex(num: str) -> str:
    return decToHex(binaryToDec(num))
def hexToBinary(num: str) -> str:
    return decToBinary(hexToDec(num))


def main():
    algorithm = -1
    numToConvert = -1
    while (not(algorithm in range(1,7))):
        algorithm = int(input("Please select a conversion:\n"
                              + "1. Binary to Decimal\n"
                              + "2. Decimal to Binary\n"
                              + "3. Hexadecimal to Decimal\n"
                              + "4. Decimal to Hexadecimal\n"
                              + "5. Binary to Hexadecimal\n"
                              + "6. Hexadecimal to Binary\n"))
        if (not(algorithm in range(1,7))):
            print("Invalid entry. Please try again.\n")
    numToConvert = input("Enter a positive integer to be converted:\n")
    match algorithm:
        case 1:
            print(numToConvert + " to decimal is " + binaryToDec(numToConvert))
        case 2:
            print(numToConvert + " to binary is " + decToBinary(numToConvert))
        case 3:
            print(numToConvert + " to decimal is " + hexToDec(numToConvert))
        case 4:
            print(numToConvert + " to hexadecimal is " + decToHex(numToConvert))
        case 5:
            print(numToConvert + " to hexadecimal is " + binaryToHex(numToConvert))
        case 6:
            print(numToConvert + " to binary is " + hexToBinary(numToConvert))
    return

main()