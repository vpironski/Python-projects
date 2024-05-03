class Card:
    def __init__(self,name,suit):
        self.name=name
        self.suit=suit
        if(name== "7"):
            self.rank = 0
        elif(name=="8"):
            self.rank = 0
        elif(name=="9"):
            self.rank = 14
        elif(name=="10"):
            self.rank = 10
        elif(name=="j"):
            self.rank = 20
        elif(name=="q"):
            self.rank = 3
        elif(name=="k"):
            self.rank = 4
        elif(name=="a"):
            self.rank = 11
        
    def __init__(self,name,suit, rank):
        self.name = name
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.name, " ", self.suit," ",str(self.rank)
    def get_name(self):
        return self.name
    def get_suit(self):
        return self.suit
    def get_rank(self):
        return self.rank
    

    def calculate(sum, card):
        sum = sum + card.get_rank()
        return sum
    
    def result(sum):
        print(sum)
            