import pytest
from movie_booking import MovieBooking


def test_book_one_ticket():
    booking = MovieBooking(5)
    assert booking.book_ticket(1) is True
    assert booking.available_seats == 4


def test_book_multiple_tickets():
    booking = MovieBooking(5)
    assert booking.book_ticket(3) is True
    assert booking.available_seats == 2


def test_cannot_book_more_than_available():
    booking = MovieBooking(2)
    assert booking.book_ticket(3) is False
    assert booking.available_seats == 2


def test_quantity_must_be_positive():
    booking = MovieBooking()
    with pytest.raises(ValueError):
        booking.book_ticket(0)
