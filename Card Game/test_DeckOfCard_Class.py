from unittest import TestCase
from DeckOfCard_Class import DeckOfCards
from Card import Card


class TestDeckOfCards(TestCase):
    # Set a global object of the class for the tests
    def setUp(self):
        self.deck_of_cards = DeckOfCards()
