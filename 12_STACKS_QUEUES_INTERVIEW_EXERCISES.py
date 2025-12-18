class Stack:
    def __init__(self):
        self.stack_list = []
        self.height = 1 

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()
        

def reverse_string(str_val):
    str_stack = Stack()
    for letter in str_val:
        str_stack.push(letter)
    
    result_str = ""
    while not str_stack.is_empty():
        temp = str_stack.pop()
        result_str += temp 
    
    return result_str


def is_balanced_parentheses(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            # I missed this condition: stack.pop() != '('
            if stack.is_empty() or stack.pop() != '(':
                return False
    return stack.is_empty()
    

