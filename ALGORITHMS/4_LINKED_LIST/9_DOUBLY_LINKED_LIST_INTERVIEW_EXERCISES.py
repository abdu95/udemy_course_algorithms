


## 49 Palindrome checker 

# my solution 
# no need for is_palindrome, redundant code for odd and even 


def is_palindrome(self):
    is_palindrome = False
    if self.length == 0 or self.length == 1:
        return True

    forward = self.head 
    backward = self.tail 
    
    if self.length % 2 == 0: 
        while forward.next == backward and backward.prev == forward: 
            if forward.value == backward.value:
                is_palindrome = True 
            forward = forward.next 
            backward = backward.prev  
    else: 
        while forward.next != backward.prev: 
            if forward.value == backward.value:
                is_palindrome = True 
            forward = forward.next 
            backward = backward.prev  
    
    return is_palindrome



# simpler code: 


def is_palindrome(self):
    if self.length <= 1:
        return True
        
    forward = self.head 
    backward = self.tail 
    for i in range(self.length // 2):
        if forward.value != backward.value:
            return False
        forward = forward.next 
        backward = backward.prev  
    return True



