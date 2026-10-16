class MovieBooking:
    def __init__(self, available_seats=5):
        self.available_seats = available_seats
        self.booked_seats = 0

    def book_ticket(self, quantity=1):
        if quantity < 1:
            raise ValueError("Quantity must be at least 1")

        if quantity > self.available_seats:
            return False

        self.available_seats -= quantity
        self.booked_seats += quantity
        return True
