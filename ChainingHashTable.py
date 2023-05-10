#Cited from https://westerngovernorsuniversity-my.sharepoint.com/:u:/g/personal/cemal_tepe_wgu_edu/EXaXbjKAci5EhnaWjPab6iMBc0zOUb_dOa_b-FwY4zeumg?e=1EN3Bl
class ChainingHashTable:
    def __init__(self, initial_capacity = 20):
        #initialize the hash table with empty bucket list entries
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])
    #Time Complexity O(1)
    #Space Complexity O(n)
    #Inserts a new item into the hash table
    def insert(self,key,item): #does both insert and update
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        #update key if it is already in the bucket
        for kv in bucket_list:
            #print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        #if not, insert the item to the end of the bucket list
        key_value = [key,item]
        bucket_list.append(key_value)
        return True

    # Time Complexity O(1)
    # Space Complexity O(n)
    #Search for an item with matching key in the hash table
    #Returns the item if found, or None if not found
    def search(self,key):
        #get the bucket list where this key would be
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        #print (bucket_list)
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]
        return None

    #Remove an item with matching key from the hash table
    def remove(self,key):
        #get the bucket list where this item will be removed from
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        #remove the item from the bucket list if it is present
        for kv in bucket_list:
            #print (key_value)
            if kv[0]== key:
                bucket_list.remove(kv[0],kv[1])