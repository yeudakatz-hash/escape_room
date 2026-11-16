def str_to_int(num):
    try:
        return int(num)
    except:
        return 0


def is_legal_num(num, rang):
    try:
        return  0 < num < rang
    except:
        return 0


def get_num(text, rang):
    num = str_to_int(input(f"{text}: "))
    while not is_legal_num(num, rang) or str_to_int(num) == 0:
        try:
            num = str_to_int(input(f"{text}: "))
        except:
            continue
    return str_to_int(num)
