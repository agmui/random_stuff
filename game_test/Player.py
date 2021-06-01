import os
import random
import json

data = os.path.join("game_test", "data.json")
with open(data) as f:
    data = json.load(f)


class Card:
    def __init__(self, name, text, type, img):
        self.name = name
        self.text = text
        self.type = type
        self.img = img


class Player:
    def __init__(self, username):
        self.name = username
        self.hand = []
        self.stable = []

    def addCard(self, card, where):
        if where == "hand":
            self.hand.append(card)  # apply to js
        elif where == "stable":
            self.stable.append(card)

    def removeCard(self, card, where):
        if where == "hand":
            if card in self.hand:
                self.hand.remove(card)
        elif where == "stable":
            if card in self.stable:
                self.stable.remove(card)

    def getName(self):
        return self.name

    def getHand(self):
        return self.hand

    def getHandName(self):
        return [i.getName() for i in self.hand]

    def getStable(self):
        return self.stable

    def getStableName(self):
        return [i.getStable() for i in self.stable]


class Board:
    def __init__(self, playerNames):
        self.log = []
        self.players = [Player(i) for i in playerNames]
        self.deck = []
        for i in data:
            for j in range(int(i["quantity"])):
                self.deck.append(Card(i["name"], i["text"], i["type"], i["img"]))
        self.discard = []
        self.turn = 0
        self.phase = 1
        self.bypass = []

    def setup(self):
        for i in self.players:
            i.addCard(self.drawFromDiscard(5))

    def drawFromDeck(self, num=1):
        return [self.deck[random.randint(0, len(self.deck))] for i in range(num)]

    def drawFromDiscard(self):
        return random.randint(0, len(self.discard))

    def addCard(self, card, where):
        if where == "deck":
            self.deck.append(card)
        elif where == "discard":
            self.discard.append(card)

    def removeCard(self, card, where):
        if where == "deck":
            for i in self.deck:
                if i.name == card.name:
                    self.deck.remove(i)
                    return
        elif where == "discard":
            for i in self.discard:
                if i.name == card.name:
                    self.discard.remove(i)
                    return
        print("Player class:", card.name, "not in", where)

    # some function to talk to AutoCard class

    def move(self, name, card, f, t, bypass=False):
        if f == "deck":
            return
        elif f == "discard":
            return
        elif f == "hand" or f == "stable":
            return
        else:
            print()

        if t == "deck":
            return
        elif t == "discard":
            return
        elif t == "hand" or f == "stable":
            return
        else:
            print()

        for i in self.players:
            if len(i.getStable()) >= 7:
                print(i.getName, "wins")
                return i


    # interupt?

    # def rotateTurn(self, )

    # def rotatePhase(self, )

    def getTurn(self):
        return self.turn

    def getPhase(self):
        return self.phase

    # def getPlayer(self)

    def getDeck(self):
        return self.deck

    def getDiscard(self):
        return self.discard


def main():
    c = Card("test", "test", "test", "test")
    game = Board(["hi"])


main()
