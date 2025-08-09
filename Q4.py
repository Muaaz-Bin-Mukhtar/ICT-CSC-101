import string

def printChars(ch1, ch2, numberPerLine):
    chars = string.digits + string.ascii_uppercase  # Same as doing 0123456789A......Z
    output = chars[chars.index(ch1):chars.index(ch2)+1]

    for start in range(0, len(output), numberPerLine):
        print(output[start:start+numberPerLine])

printChars("0", "Z", 10)
