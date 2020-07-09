number_to_text = ["zero", "one", "two", "three", "four", "five", "six",
                  "seven", "eight", "nine"]
phone_number = input()

for number in phone_number:
    print(number_to_text[int(number)])
