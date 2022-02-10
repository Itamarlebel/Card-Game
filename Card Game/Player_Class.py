from Card_Class import Card
from DeckOfCard_Class import DeckOfCards
import random


class Player:
    # Player constructor:
    def __init__(self, name: str, num_of_cards=26):
        if type(name) != str:
            raise TypeError("Name must be str type!")
        if type(num_of_cards) != int:
            raise TypeError("Number of cards must be an integer!S")
        if num_of_cards < 10 or num_of_cards > 26:
            num_of_cards = 26
        self.name = name
        self.num_of_cards = num_of_cards
        self.cards = []

    # return the name of the player
    def __str__(self):
        return f"{self.name}"