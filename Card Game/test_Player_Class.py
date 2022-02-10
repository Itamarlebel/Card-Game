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

    # Checks __init__ method valid functionality
    def test__init__valid(self):
        self.assertEqual(self.player1.name, "Raz")  # Player gets expected name
        self.assertEqual(self.player1.num_of_cards, 10)  # Player gets expected num_of_cards
        self.assertEqual(self.player1.cards, [])  # A Player starts with an empty hand upon creation
        self.assertTrue(self.player3.num_of_cards == 26)  # Not enough cards - resets to 26
        self.assertTrue(self.player4.num_of_cards == 26)  # Too many cards - resets to 26
        self.assertTrue(self.player5.num_of_cards == 26)  # Gets default num of cards - 26

    # Checks that error is raised when name is not of type str or num_of_card is not type int
    def test__init__invalid(self):
        with self.assertRaises(TypeError):
            self.invalid_name_type_player = Player(2, 10)
        with self.assertRaises(TypeError):
            self.invalid_num_of_cards_type_player = Player('test', 'invalid')


