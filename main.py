
def compare_chars(char1, char2):
    if char1 < char2:
        return -1
    elif char1 > char2:
        return 1
def sort_it(string):
    lowerstring = string.lower()

    no_special = ""
    for char in lowerstring:
        if char.isalpha():
            no_special += char

    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(no_special) - 1):
            char1 = no_special[i]
            char2 = no_special[i + 1]
            compare = compare_chars(char1, char2)

            if compare == 1:
                no_special = no_special[:i] + char2 + char1 + no_special[i+2:]
                is_sorted = False

    return no_special



string = "When not studying nuclear physics, Bambi likes to play beach volleyball."
print(sort_it(string))