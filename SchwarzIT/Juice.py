class Juices:
    def __init__(self, name, price, man, qty):
        self.name = name
        self.price = price
        self.man = man
        self.qty = qty

    def __str__(self):
        return self.name + ': ' + str(self.price) + ' ' + self.man + ' ' + str(self.qty)
    
    def info(self):
        print(self.get_name)
        print(self.get_price)
        print(self.get_man)
    
    def order(self, orders):
        if(self.get_qty >= orders):
            print("OK")
            self.set_qty(self.get_qty,self.get_qty - orders)
        

    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def get_man(self):
        return self.man

    def get_qty(self):
        return self.qty
    
    def set_qty(self, qty):
        self.qty = qty

orange = Juices("orange",5,"Cappy",40)
apple = Juices("apple",3,"Cappy",30)
pear = Juices("pear",7,"Queens",10)
juicesBox = [orange, apple, pear]

line = input()

def search(word, array):
    for i in array:
        if i.get_man() == word:
            print(i)

search(line, juicesBox)