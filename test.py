import unittest
from auction_house import *


class TestAuctionHouse(unittest.TestCase):

    def test_random_item_s123(self):
        """
        Testing basic functions of auction_house
        """
        # Add item s123
        s123 = Item("s123", 'random item', 300)
        self.assertTrue(s123.available is True)
        self.assertTrue(s123.bid_active is False)
        # Starting bid
        s123.start_bid()
        self.assertTrue(s123.bid_active is True)
        # Submitting a bid
        s123.submit_bid(25, 'Charlie')
        self.assertTrue(s123.bid_value == 25)
        self.assertTrue(s123.highest_bidder == 'Charlie')
        # Making sure lower bid does not change instance state
        s123.submit_bid(10, 'Joe')
        self.assertTrue(s123.bid_value == 25)
        self.assertTrue(s123.highest_bidder == 'Charlie')
        # Making sure higher bid does change state
        s123.submit_bid(50, 'Frankie')
        self.assertTrue(s123.bid_value == 50)
        self.assertTrue(s123.highest_bidder == 'Frankie')
        # Calling the auction call
        s123.auction_call()
        self.assertTrue(s123.available is False)
        self.assertTrue(s123.is_success == 'Failure')
        self.assertTrue(s123.bid_active is False)
        # Starting bid on sold item
        self.assertTrue(s123.start_bid() == 'Item no longer available.')
        # Calling auction call on sold item
        self.assertTrue(s123.auction_call() == 'Bid is already inactive.')
        # Bidding on sold item
        self.assertTrue(s123.submit_bid(500, 'Feliks') == 'Item has been sold, and is no longer available.')

    def test_query(self):
        """
        Testing the query
        """
        a123 = Item("a123", 'random item', 300)
        self.assertTrue(get_item('a123') == a123)
        # Get_item returns None if item does not exist
        self.assertTrue(get_item('b123') == "Id not found.")

    def test_duplicate(self):
        """
        Asserting a duplicate key raises an error
        """
        f13 = Item("f13", 'book', 20)
        # Test the error if another a duplicate is submitted
        self.assertRaises(NameError, Item, 'f13', 'book', 40)
        # Make sure original item instance was not changed
        self.assertTrue(f13.price == 20)

if __name__ == "__main__":
    unittest.main()