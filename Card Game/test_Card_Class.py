from unittest import TestCase
from Card_Class import Card


class TestCard(TestCase):
    # Instantiating objects of the tested class - Card:
    def setUp(self):
        self.ace_of_diamond = Card(1, 1)
        self.ace_of_club = Card(1, 4)
        self.king_of_club = Card(13, 4)
        self.ten_of_heart = Card(10, 3)

    # Checks that __init__ sets the correct attributes to the card object upon instantiation
    def test__init__valid(self):
        self.assertTrue(type(self.ace_of_diamond) == Card)
        self.assertEqual(self.ace_of_diamond.value, 1)  # Min value
        self.assertEqual(self.ace_of_diamond.suit, 1)  # Min suit
        self.assertEqual(self.king_of_club.value, 13)  # Max value
        self.assertEqual(self.king_of_club.suit, 4)  # Max suit

    # Check invalid cases of the __init__ method
    def test__init__invalid(self):
        with self.assertRaises(TypeError):
            self.invalid_value_type_card = Card('test', 2)
        with self.assertRaises(TypeError):
            self.invalid_suit_type_card = Card(2, 'test')
        with self.assertRaises(ValueError):
            self.invalid_value_range_card = Card(14, 2)
        with self.assertRaises(ValueError):
            self.invalid_suit_range_card = Card(1, 5)



