from unittest import TestCase
from CardGame import CardGame


class TestCardGame(TestCase):
    # Set a global object of the class for the tests
    def setUp(self):
        # CardGame object that the number of cards is default
        self.cardgame = CardGame("Raz", "Itamar")
        # CardGame object that the number of cards is 10
        self.cardgame_10_cards = CardGame("Raz", "Itamar", 10)
