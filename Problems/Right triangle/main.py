class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here
        self.s = 1 / 2.0 * self.a * self.b


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
if (input_c ** 2) != (input_a ** 2) + (input_b ** 2):
    print("Not right")
else:
    right_triangle = RightTriangle(input_c, input_a, input_b)
    print(right_triangle.s)
