
def is_legal_name(name):
    return len(name.strip()) > 0



def get_name(text):
    name = input(f"{text}: ")
    while not is_legal_name(name):
        name = input(f"{text}: ")
    return name.lower()



def get_difficult():
    difficult = input("enter difficulty: ")
    while difficult.lower() not in ("hard", "easy", "medium"):
        difficult = input("enter difficulty: ")
    return difficult