from unittest import TestCase, mock
from Player_Class import Player
from Card_Class import Card
from DeckOfCard_Class import DeckOfCards
from unittest.mock import patch


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
        self.assertEqual(self.player1.name, "Raz")
        self.assertEqual(self.player1.num_of_cards, 10)
        self.assertEqual(self.player1.cards, [])
        self.assertTrue(self.player3.num_of_cards == 26)
        self.assertTrue(self.player4.num_of_cards == 26)
        self.assertTrue(self.player5.num_of_cards == 26)

    # Checks that error is raised when name is not of type str or num_of_card is not type int
    def test__init__invalid(self):
        with self.assertRaises(TypeError):
            self.invalid_name_type_player = Player(2, 10)
        with self.assertRaises(TypeError):
            self.invalid_num_of_cards_type_player = Player('test', 'invalid')

    # Checks that the dealt card from the deck is in Player's hand
    @mock.patch('DeckOfCard_Class.DeckOfCards.deal_one', return_value=Card(10, 3))
    def test_set_hand_valid_card(self, mock_deal_one):
        self.player1.set_hand(self.deck_of_cards)
        self.assertIn(self.deck_of_cards.deal_one(), self.player1.cards)

    # Checks that the player gets the amount of cards he has to get from the deck, according to num_of_cards attribute
    def test_set_hand_valid_num_of_cards(self):
        self.player1.set_hand(self.deck_of_cards)
        self.assertEqual(len(self.player1.cards), self.player1.num_of_cards)

    # Checks that set_hand method raises TypeError when it gets a parameter not of type DeckOfCards
    def test_set_hand_invalid_deck_type(self):
        with self.assertRaises(TypeError):
            self.player2.set_hand('deck')

    # Checks that set_hand method does not hand out the same card more than once to a player:
    def test_set_hand_invalid_add_card_already_in(self):
        with patch('DeckOfCard_Class.DeckOfCards.deal_one') as mock_deal_one:
            mock_deal_one.return_value = Card(1, 2)
            deck = DeckOfCards()
            self.player1.set_hand(deck)
            self.assertEqual(self.player1.cards, [Card(1, 2)])
            self.assertIn(mock_deal_one.return_value, self.player1.cards)

    # Checks that ValueError is raised when trying to set hand bigger than the used deck
    def test_set_hand_invalid_deck_len(self):
        self.deck_of_cards.deck = []
        with self.assertRaises(ValueError):
            self.player3.set_hand(self.deck_of_cards)


