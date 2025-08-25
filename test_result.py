import sys
from helpers import ColorsHelper
from unittest import TextTestResult


# overriding key methods for compact results
class CompactTestResult(TextTestResult):
    def printErrors(self):
        for error in self.errors:
            print(error[1]) # index of formatted_msg

    def addError(self, test, err):
        formatted_msg = ''
        formatted_msg += ColorsHelper.colored_text('-' * 100, 'red', bold=True)
        formatted_msg += '\n'
        formatted_msg += ColorsHelper.colored_text(f'Error during {test._testMethodName}: ', 'red')
        formatted_msg += ColorsHelper.colored_text(sys.exc_info()[1], 'white', bold=True)
        formatted_msg += '\n'
        formatted_msg += ColorsHelper.colored_text('-' * 100, 'red', bold=True)
  
        self.errors.append((test, formatted_msg))

    def addFailure(self, test, err):
        formatted_msg = ''
        formatted_msg += ColorsHelper.colored_text('-' * 100, 'red', bold=True)
        formatted_msg += '\n'
        formatted_msg += ColorsHelper.colored_text(f'{test._testMethodName} failed: ', 'yellow')
        formatted_msg += ColorsHelper.colored_text(err[1], 'white', bold=True)
        formatted_msg += '\n'
        formatted_msg += ColorsHelper.colored_text('-' * 100, 'red', bold=True)

        self.failures.append((test, formatted_msg))
        print(formatted_msg)

    def addSuccess(self, test):
        formatted_msg = ''
        formatted_msg += ColorsHelper.colored_text('-' * 100, 'green', bold=False)
        formatted_msg += '\n'
        formatted_msg += ColorsHelper.colored_text(f'=> {test._testMethodName} passed!', 'green')
        formatted_msg += '\n'
        formatted_msg += ColorsHelper.colored_text('-' * 100, 'green', bold=False)

        print(formatted_msg)

    def stopTestRun(self):
        return super().stopTestRun()