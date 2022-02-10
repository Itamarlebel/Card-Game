from unittest import TestCase
from Card_Class import Card


class TestCard(TestCase):
    # Instantiating objects of the tested class - Card:
    def setUp(self):
        self.ace_of_diamond = Card(1, 1)
        self.ace_of_club = Card(1, 4)
        self.king_of_club = Card(13, 4)
        self.ten_of_heart = Card(10, 3)
