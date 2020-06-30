from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult
import re

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)


class CreditCalcTest(StageTest):
    def generate(self):
        return [
            TestCase(
                stdin='1000\nm\n200',
                attach=(5, 'months'),
            ),
            TestCase(
                stdin='1000\nm\n150',
                attach=(7, 'months'),
            ),
            TestCase(
                stdin='1000\nm\n1000',
                attach=(1, 'month'),
            ),
            TestCase(
                stdin='1000\np\n10',
                attach=100,
            ),
            TestCase(
                stdin='1000\np\n9',
                attach=['112', '104'],
            ),
        ]

    def check(self, reply, attach):

        if isinstance(attach, tuple):
            a, b = attach
            if a == 1:
                if '1 months' in reply:
                    output = '{0} should be in the output, but you output {1}'
                    return CheckResult.wrong(
                        output.format('1 month', reply),
                    )

            if str(a) not in reply or b not in reply:
                output = (
                    '"{0} {1}" should be in the output, but you output {2}'
                )
                return CheckResult.wrong(
                    output.format(a, b, reply),
                )

        elif isinstance(attach, list):
            if attach[0] not in reply or attach[1] not in reply:
                numbers = re.findall(r'[-+]?(\d*\.\d+|\d+)', reply)
                if len(numbers) == 0:
                    output = (
                        'Correct monthly payment is {0} and last payment is'
                        ' {1}, but there are no any numbers in your output'
                        .format(attach[0], attach[1])
                    )
                elif len(numbers) == 1:
                    output = (
                        'Correct monthly payment is {0} and last payment is'
                        ' {1}, but there are only {2} in your output'
                        .format(attach[0], attach[1], numbers[0])
                    )
                else:
                    output = (
                        'Correct monthly payment is {0} and last payment is'
                        ' {1}, but there are only {2} {3} in your output'
                        .format(attach[0], attach[1], numbers[0], numbers[1])
                    )
                return CheckResult.wrong(output)
        else:
            if str(attach) not in reply:
                output = (
                    'Correct monthly payment is {0}. But your output is {1}'
                )
                return CheckResult.wrong(
                    output.format(attach, reply),
                )

        return CheckResult.correct()


if __name__ == '__main__':
    CreditCalcTest('creditcalc.creditcalc').run_tests()
