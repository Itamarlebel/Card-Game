from unittest import TestCase, mock
from unittest.mock import patch
from Player_Class import Player
from Card_Class import Card
from DeckOfCard_Class import DeckOfCards


class TestPlayer(TestCase):
    def setUp(self):
        self.deck_of_cards = DeckOfCards()
        self.player1 = Player("Raz", 10)
        self.player2 = Player("Itamar", 10)
        self.player3 = Player("Beni", 4)
        self.player4 = Player("Dani", 30)
        self.player5 = Player("Dan")
