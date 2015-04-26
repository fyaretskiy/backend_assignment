"""
Auction House Module

Use:
Create an instance of an item:  id = Item('id', 'name', price)
Id: satisfies the following condition, first character must be a letter
Name: string, description of item
price: int

Methods:
Item.start_bid()
Item.submit_bid()
Item.auction_call()
Item.get_info(value, name): Value is the bid price, int. Name is the string
"""


# Global container object stores Item instances in the form of {id: object}
container = {}


def store_item(id_, obj):
    """
    Takes id and obj and links id to the obj in container dict object. This additional step makes sure duplicate id's
    are not generated.
    """
    if id_ in container:
        raise NameError('Id already exists')
    else:
        container[id_] = obj


def get_item(id_):
    """
    Method for querying items.
    """
    if id_ in container:
        return container[id_]
    else:
        return output("Id not found.")


def output(a_string):
    """
    For testing and stdout.
    """
    if __name__ == "__main__":
        print(a_string)
    # For unittests
    if __name__ != "__main__":
        return a_string


class Item:
    def __init__(self, id_, name, price):
        store_item(id_, self)
        self.id = id_  # string
        self.name = name  # string
        self.price = price  # int
        self.bid_value = 0  # int
        self.bid_active = False  # takes type True/False
        self.available = True  # takes type True/False
        self.is_success = None  # Takes string Success/Failure
        self.highest_bidder = None  # takes string name

    def start_bid(self):
        """
        Starts bid on item. Modifies self.bid_active.
        """
        if self.bid_active:
            return output("Bid is already active.")
        elif not self.available:
            return output("Item no longer available.")
        elif not self.bid_active is True and self.available:
            self.bid_active = True

    def auction_call(self):
        """
        Stops bid on item. Establishes item availability, auction success and bid activity.
        """
        # Calling auction call before starting bid:
        if self.available and not self.bid_active:
            return output("Bidding has not yet started.")
        # For active bid
        if self.bid_active:
            self.bid_active = False
            # For condition bid equals price, consider success
            if self.bid_value >= self.price:
                self.is_success = "Success"
            elif self.bid_value < self.price:
                self.is_success = "Failure"
            # Item no longer available
            self.available = False
        # For finished bid
        else:
            return output("Bid is already inactive.")

    def submit_bid(self, value, name):
        """
        Takes a bid value, and the bidders name. Updates item current bid value and highest bidder.
        """
        # Check availability
        if not self.available:
            return output("Item has been sold, and is no longer available.")
        # Check bid
        if not self.bid_active:
            return output("Bid not active.")
        # Check integer
        try:
            value = int(value)
        except ValueError:
            return output("Integer necessary")
        # Check positive integer
        try:
            assert(value > 0)
        except AssertionError:
            return output("Positive integer required")
        if value > self.bid_value:
            self.bid_value = value
            self.highest_bidder = name
        elif value <= self.bid_value:
            return output("Proposed value needs to be greater than current bid.")

    def get_info(self):
        """
        Returns a dictionary object of the current item state.
        """
        return {"id": self.id,
                "name": self.name,
                "latest bid value:": self.bid_value,
                "bid active:": self.bid_active,
                "Bid successful:": self.is_success,
                "Highest bidder:":  self.highest_bidder,
                "Item available:": self.available
                }


