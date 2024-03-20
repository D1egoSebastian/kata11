

def compare_chars(char1, char2):
    if char1 < char2:
        return -1
    elif char1 > char2:
        return 1

def sort_it(string):

    stringlower = string.lower()

    not_special = ""
    for char in stringlower:
        if char.isalpha():
            not_special += char

    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(not_special) - 1):
            char1 = not_special[i]
            char2 = not_special[i + 1]
            compare = compare_chars(char1, char2)

            if compare == 1:
                not_special = not_special[:i] + char2 + char1 + not_special[i + 2:]
                is_sorted = False

    return not_special

string = "ABC"
answer = sort_it(string)
print(answer)


