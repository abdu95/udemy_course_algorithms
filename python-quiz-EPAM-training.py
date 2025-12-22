# is set in python mutable? yes 
# is set dynamic like list? yes 
# is set ordered? no 
# set elements can be of any hashable type? yes 

# is this true? hash values of different keys may have duplicates? yes

# is this statement correct: functions are objects with call magic method? yes
# which one of these is used in python? parametric or ad hoc polymorphism? adhoc
# is tuple mutable? no
#  static method is not tied to specific object
# shortly explain abstraction in oop: Abstraction means hiding complex implementation details and showing only the essential features of an object.
# Exceptions are raised when Python executes the code
# what is executing, interpreting and compiling code in python
# what is first class entity in python? function
# what is / in arguments? In Python function definitions, the / in the argument list is used to indicate that all parameters before it must be passed positionally — they cannot be passed as keyword arguments.
# what will be the output? 


def foo(positional, only, /, either, pos, or_ = 'default', *, keyword, just, **keywords):
    print(positional, only, either, pos, or_, keyword, just, keywords)

# foo('a', 'b', 1,2, 'or_', keyword = 'keyword', just = 'just', unknown_keyword = 'something')


# what is update method in set? UNION
# can class methods modify the state of the object instance?
# are modules standard code bases? no
# is var keyword in python? NO
# what is encapsulation? bundling of data (attributes) and methods (functions) that operate on that data into a single unit — typically a class — and restricting direct access to some of the object's components.
# bundling of data (attributes) and methods (functions) that operate on that data into a single unit — typically a class — and restricting direct access to some of the object's components.
# what is map in python? built-in function used to apply a function to every item in an iterable (like a list or tuple) and return a map object (which is an iterator).
# lambda function in python
# a function accepts two args. write a decorator for this function
# @staticmethod decorator in python, what it does




city = 'Tash'
# city[0] = 't'

result = 20 / 2 + 12 * 2 - 9
# print(result)



# x = 1 
# def foo():
#     nonlocal x 
#     def bar():
#         print(x)
#     bar()

# x = 3
# foo()

x = 1 
def foo():
    globals()['x'] = 2
    def bar():
        print(x)
    
    bar()

foo()