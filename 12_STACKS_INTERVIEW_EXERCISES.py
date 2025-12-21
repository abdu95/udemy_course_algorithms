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
    

def sort_stack(input_stack):
    highest_to_lowest = Stack()
    while not input_stack.is_empty():
        temp = input_stack.pop()
        
        # we stop pushing peek to first stack when highest_to_lowest is empty or temp > peek
        while not highest_to_lowest.is_empty() and highest_to_lowest.peek() > temp:
            input_stack.push(highest_to_lowest.pop())
        
        highest_to_lowest.push(temp)

    # pop items from second stack to first stack so that highest item from second stack is pushed to the bottom of the first stack   
    while not highest_to_lowest.is_empty():
        input_stack.push(highest_to_lowest.pop())





my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()



"""
    EXPECTED OUTPUT:
    ----------------
    Stack before sort_stack():
    2
    4
    5
    1
    3

    Stack after sort_stack:
    1
    2
    3
    4
    5

"""
