grade = int(input())
max_grade = int(input())
percent_grade = round(grade / max_grade * 100, 2)

if percent_grade < 60:
    print("F")
elif percent_grade < 70:
    print("D")
elif percent_grade < 80:
    print("C")
elif percent_grade < 90:
    print("B")
else:
    print("A")
