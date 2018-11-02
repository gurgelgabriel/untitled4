def doubleevan():
    nomad = int(input("press a number"))
    if nomad % 2 == 1:
        return "-1"
    elif nomad % 2 == 0:
        return (nomad*2)

print(doubleevan())


def grade_percentage():
    grade = int(input("your percentage"))
    if grade <= 50:
        return "f"
    if 60 > grade >= 50:
        return "e"
    if 60 < grade <= 70:
        return "d"
    if 70 < grade <= 80:
        return "c"
    if 80 < grade < 90:
        return "b"
    if grade >= 90:
        return "a"

print(grade_percentage())
