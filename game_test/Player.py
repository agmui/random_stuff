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
            self.hand += card  # apply to js
        elif where == "stable":
            self.stable += card

    def removeCard(self, card, where):
        if where == "hand":
            for j in card:
                for i in self.hand:
                    if i.name == j.name:
                        self.hand.remove(i)
        elif where == "stable":
            for j in card:
                for i in self.stable:
                    if i.name == j.name:
                        self.stable.remove(i)

    def getName(self):
        return self.name

    def getHand(self):
        return self.hand

    def getHandName(self):
        return [i.name for i in self.hand]

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
        self.sendPic = []
        self.bypass = []

    def setup(self):
        for i in self.players:
            i.addCard(self.drawFromDeck(5), "hand")

    def drawFromDeck(self, num=1):
        return [self.deck[random.randint(0, len(self.deck))] for i in range(num)]

    def drawFromDiscard(self):
        return random.randint(0, len(self.discard))

    def addCard(self, card, where):  # have js take card as list
        if where == "deck":
            self.deck += card
        elif where == "discard":
            self.discard += card

    def removeCard(self, card, where):  # have js take card as list
        if where == "deck":
            for j in card:
                for i in self.deck:
                    if i.name == j.name:
                        self.deck.remove(i)
                        # fix in js there should be no return
        elif where == "discard":
            for j in card:
                for i in self.discard:
                    if i.name == j.name:
                        self.discard.remove(i)
                        # fix in js there should be no return

    # some function to talk to AutoCard class

    def move(self, name, card, f, t, bypass=False):
        if self.bypass:
            if name == self.bypass[-1]: self.bypass.pop()
        elif name != self.getTurn() and bypass == False:
            print("Player class: not player's turn")
            return False
        elif len(self.bypass) > 0: return False

        print("MOVE:", name, "moved", card[0].name, "from", f, "to", t)
        if card == "random": card = self.drawFromDeck() if f == "deck" else self.drawFromDiscard()
        if type(card) != list: card = [card]
        for i in card:
            if type(i) != Card:
                i = Card(i.name, i.text, i.type, i.img)
        if f == "deck":
            self.removeCard(card, f)
            """if t != "discard" or t != "deck":
                if t == "Hand" or t == "Stable":
                    t = [name, t]
                self.sendPic.append({
                    "card": card,
                    "to": t
                })"""
        elif f == "discard":
            self.removeCard(card, f)  # probs can merge fix in js
            """if t != "discard" or t != "deck":
                if t == "Hand" or t == "Stable":
                    t = [name, t]
                self.sendPic.append({
                    "card": card,
                    "to": t
                })"""
            # fix so it looks like top in js
        elif f == "hand" or f == "stable":  # maybe can merge with bot
            # use get player function in js
            self.getPlayer(name).removeCard(card, f)
        else:
            self.getPlayer(f[0]).removeCard(card, f[1])  # change in js

        if t == "deck":  # can combine in js
            self.addCard(card, t)
        elif t == "discard":
            self.addCard(card, t)
        elif t == "hand" or t == "stable":
            # use function change in js
            self.getPlayer(name).addCard(card, t)
        else:  # use function in js
            self.getPlayer(t[0]).addCard(card, t[1])

        for i in self.players:
            if len(i.getStable()) >= 7:
                print(i.getName, "wins")
                return i

    def interrupt(self, toWho):
        print("Player class: recived interupt for", toWho)
        self.bypass.append(toWho)

    def rotateTurn(self):
        self.turn += 1
        if self.phase != 5:
            print("ERROR: not end of phase")
            return
        self.phase = 1
        self.log = []
        if self.turn > len(self.players) - 1:
            self.turn = 0
        return self.getTurn()  # change in js

    def rotatePhase(self):
        self.phase += 1
        if self.phase >= 4 and self.getTurn(True):
            if self.phase == 5:
                self.phase -= 1
            print("Player class:", self.getTurn(True), "has to maney cards")
            return {"numOfCards": len(self.getTurn(True).getHand()) - 7}

        if self.phase == 1:
            pass
        elif self.phase == 2:
            print("Player class: draws card for player")
            self.rotatePhase()
        elif self.phase == 3:
            print("Player class: draw or play")
        elif self.phase == 4:
            pass

        return self.phase

    def getTurn(self, object=False):
        return self.players[self.turn] if object else self.players[self.turn].getName()

    def getPhase(self):
        return self.phase

    def getPlayer(self, name):
        for i in self.players:
            if i.getName() == name:
                return i
        print("Player class: player not found")

    def getDeck(self):
        return self.deck

    def getDiscard(self):
        return self.discard


def main():
    game = Board(["a", "b"])
    c = game.drawFromDeck()
    print(c[0].name, "\n")


main()
