# 16 Hash Table 

## 16.72 Hash Table Intro

*Imagine a table with two columns: address and key-value. Each key-value has a special address that is generated using hash function. This is called hash table.*

- A hash table is a super-fast data structure that stores data as key-value pairs
- It uses a special function (hash function) to convert a unique key into an array index (bucket), 
    - It allows for near-instant lookups, insertions, and deletions, ideal for big datasets where speed is crucial for finding items like or IP addresses

Dictionary: built-in hash table with key & value
```
{"nails": 1000}
```

HASH FUNCTION

Perform hash on the key

> Function input: key 

> Function output: address and key-value pair 

Characteristics of hash function: 

- Hash function is one way:
    pass key -> get address as output. You cannot determine key by passing address. 
    + key => address 
    - key <= address  
- Hash function is deterministic:
we expect function produces same output every execution for same input

Every time we pass "nails" we get 2 as output


set_item(), get_item()


## 16.73 Collisions 

Collision happens when you put key-value pair to address that was already occupied with another key-value pair 

SEPARATE CHAINING (list)

we put two key-value pairs within a list inside the same address of 2 


```
0
1
2 [ ['nails', 1000], 1000]
3 
4 ['bolts', 1400]
5
6 ['screws', 800]
7
```

SEPARATE CHAINING (linked list)

to find paint, go to address 2 and iterate until you find it
```
0
1
2 => 'nails' => 'nuts' => 'paint'
3 
4 => 'bolts'
5
6 => 'screws'
7
```


LINEAR PROBING (form of oepn addressing)

if there is already key-value pair in the given address, go down until you find empty address 



## 16.74 Constructor

You should have prime number of addresses, seven for example (from 0 to 6).
Reason is increases the amount of randomness for how the key-value pairs will be distributed through the hash table, so it reduces your collisions. 

self.data_map
    a list with 7 items in it, all of them are None
hash 
    INPUT: a key 
    OUTPUT: address (where we store that key-value pair)  
ord() 
    gets ASCII number for each letter  
% modulo - remainder. 
    when you divide any number by 7 (length). Remainder of any number to 7 is between 0 and 6. 0-6: address space

```python
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        result_hash = 0
        for letter in key:
            result_hash = (result_hash + ord(letter) * 23) % len(self.data_map)
        return result_hash 
```

## 16.75 Set
    INPUT: key, value
    OUTPUT: none 
        passes key to the hash method to create an address. Also creates a list with key-value pair and adds it to an address

```python 
    def set_item(self, key, value):
        address = self.__hash(key)
        if self.data_map[address] == None:
            self.data_map[address] = []
        self.data_map[address].append([key, value])
```

## 16.76 Get
    INPUT: key
    OUTPUT: value 
        when key is passed, uses hash method to determine the address. Then finds key-value in that address and returns value

```python
    def get_item(self, key):
        address = self.__hash(key)
        if self.data_map[address] is not None:
            for i in range(len(self.data_map[address])):
                if self.data_map[address][i][0] == key:
                    return self.data_map[address][i][1]
        return None  
```

This is my solution. I think its more readable 

```python
    def get_item(self, key):
        address = self.__hash(key)
        if self.data_map[address] is not None:
            for sublist in self.data_map[address]:
                if sublist[0] == key:
                    return sublist [1]
        return None 
        
```



## 16.77 Keys
    INPUT: None
    OUTPUT: list of keys  
        gets all keys from hash table, puts them into a list and returns that list


```
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
```

This is my solution. I think its more readable 
```
    def keys(self):
        keys_list = []
        for top_list in self.data_map:
            if top_list is not None:
                for sublist in top_list:
                    keys_list.append(sublist[0])
        return keys_list
```

## 16.78 Big O

    Hash method: O(1)
        For a given key of a certain number of letters, it will always be same number of operations to calculate the hash
    
    Insert by key - set_item: O(1)
    Lookup by key - get_item: O(1)
        can be O(N). But assumption keys will be sitributed for each address equally.  
    Lookup by value: O(1)


## 16.79 Interview question 

    Determine if two given lists have item in common

    1 naive approach (obvious): 
        Nested for loop - O(N^2)
        1st for loop: iterate through items of first list - X
        2nd for loop: iterate through items of second list and check if any element equal to first element in first list
        ~~
        2nd for loop: iterate through items of second list and check if any element equal to second element in first list
        ~~
        2nd for loop: iterate through items of second list and check if any element equal to third element in first list
        ++ 

```python
   def item_in_common(list1, list2):
        for i in list1:
            for j in list2:
                if i == j:
                    return True 
        
        return False
```

    O(N) > O(N^2)
    2 approach - dictionary: O(N) + O(N) = O(2N) = O(N)
        Loop throught the first list, add items to dictionary as a key, assign value True
        Loop through the second list and compare each item to keys in dictionary. 

```python
    def item_in_common(list1, list2):
        my_dict = {}
        for i in list1:
            my_dict[i] = True
        
        for j in list2:
            if j in my_dict:
                return True
            
        return False
```



