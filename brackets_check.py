from class_stack import Stack

def check_brackets(brackets_string):
    brackets_string_length = len(brackets_string)

    for id, item in enumerate(brackets_string, start=1):

        if item in BRACKETS_DICT.keys():
            stack.push(item)
        elif item in BRACKETS_DICT.values():

            if BRACKETS_DICT.get(stack.peek()) == item:
                stack.pop()
            else:
                return f'{brackets_string} is not balanced'

        if id == brackets_string_length:

            if stack.isEmpty():
                return f'{brackets_string} is balanced'
            else:
                return f'{brackets_string} is not balanced'


if __name__ == '__main__':
    BRACKETS_DICT = {'(': ')', '{': '}', '[': ']'}
    stack = Stack()
    brackets_strings = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}', '{{[(])]}}', '[[{())}]']

    for string in brackets_strings:
        check_brackets(string)
        print(check_brackets(string))
