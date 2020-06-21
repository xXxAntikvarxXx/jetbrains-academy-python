# put your python code here
one_hour = int(input())
one_minute = int(input())
one_seconds = int(input())

two_hour = int(input())
two_minute = int(input())
two_seconds = int(input())

print(
    (two_hour * 3600 + two_minute * 60 + two_seconds)
    - (one_hour * 3600 + one_minute * 60 + one_seconds)
)
