class HashTable:
    def __init__(self):
        pass
    def extract_data_in_array(self):
        self.prices_array = [] #its an array
        with open("C://Users//DELL//Documents//Limansha//DSA//DSA_Python//DSA_Python//codebasicsTutorial//HashTable//prices.txt","r") as f:
            for line in f:
                tokens = line.split(',')
                self.prices_array.append([tokens[0],float(tokens[1])])        
        print(self.prices_array)

    def extract_data_in_map(self):
        self.prices = {} #this acts as dictioary/hashmap
        with open("C://Users//DELL//Documents//Limansha//DSA//DSA_Python//DSA_Python//codebasicsTutorial//HashTable//prices.txt","r") as f:
            for line in f:
                tokens = line.split(',')
                self.prices[tokens[0]] = float(tokens[1]) # making it float so that it will remove \n and gives only value
        
        print(self.prices)

    #internal implementation of dictionar/Hashmap is Hashtable - (it has an array + hash functn(to find the index))
    def get_hash(self,key):
        hash = 0 #array is of size 100
        for char in key:
            hash += ord(char)
        return hash % 100

h = HashTable()
h.extract_data_in_array()
# to get 7-Mar value from proces_array we need to perform search takes o(n)
for pair in h.prices_array:
    if(pair[0] == '7-Mar'):
        print(pair)
        break

h.extract_data_in_map()
print(h.prices['7-Mar']) #takes o(1) time


