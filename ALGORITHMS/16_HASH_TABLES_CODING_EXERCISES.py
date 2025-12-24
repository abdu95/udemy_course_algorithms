class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        result_hash = 0
        for letter in key:
            result_hash = (result_hash + ord(letter) * 23) % len(self.data_map)
        return result_hash 
        

    def set_item(self, key, value):
        address = self.__hash(key)
        if self.data_map[address] == None:
            self.data_map[address] = []
        self.data_map[address].append([key, value])

    
    def get_item(self, key):
        address = self.__hash(key)
        if self.data_map[address] is not None:
            for i in range(len(self.data_map[address])):
                if self.data_map[address][i][0] == key:
                    return self.data_map[address][i][1]
        return None  
    

    def keys(self):
        keys_list = []
        for top_list in self.data_map:
            if top_list is not None:
                for sublist in top_list:
                    keys_list.append(sublist[0])
        return keys_list


    def print_table(self):
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)




my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)
print(my_hash_table.keys())

# my_hash_table.print_table()

