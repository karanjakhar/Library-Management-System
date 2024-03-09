class Checkout:
    def __init__(self, user_id, isbn):
        self.user_id = user_id
        self.isbn = isbn
        self.checkout_date = None
        self.return_date = None