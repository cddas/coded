# Check if a string can be obtained by rotating another string n places
def checkStr(str1, str2):
    if left_rotate(str1) == str2:
        return True
    elif right_rotate(str1) == str2:
        return True
    else:
        return False


def left_rotate(input_str):
    global displace
    new_str = ""
    if 1 <= displace <= len(input_str):
        new_str = input_str[displace:]+input_str[:displace]

    return new_str


def right_rotate(input_str):
    global displace
    n = len(input_str)
    new_str = ""
    if  1 <= displace <= len(input_str):
        new_str = input_str[-displace:]+input_str[:-displace]

    return new_str


if __name__=="__main__":
    displace = 4
    str1 = input("Enter the input string : ")
    str2 = input("Enter the string to be checked : ")

    if checkStr(str1, str2):
        print("Yes")
    else:
        print("No")




