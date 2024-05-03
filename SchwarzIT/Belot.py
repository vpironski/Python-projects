from Card import Card

def main():
    word=input()
    sum = 0
    while word != "END":
        word = word.split(", ")
        name=str(word[0]).lower()
        suit=str(word[1]).lower()
        # try:
        #     rank = int(word[2])
        # except IndexError :
        #     pass

        # try:
        #     card = Card(name, suit,rank)
        # except TypeError:
        card = Card(name, suit)
        
        sum = Card.calculate(sum, card)
        word=input()

        Card.result(sum)

if __file__ == "__main__":
    main()