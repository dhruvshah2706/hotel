from datetime import datetime

class Booking:
    def __init__(self, booking_id, customer_obj, room_obj, start_date, end_date):
        self.booking_id = booking_id              # Unique booking ID
        self.customer = customer_obj                 # Customer object
        self.room = room_obj                        # Room object
        self.start_date = start_date              # Start date of the booking
        self.end_date = end_date                  # End date of the booking
        self.total_price = None                    # Will be calculated later

    def calc_price(self):
        self.start_date = datetime.strptime(self.start_date, "%d%m%Y")
        self.end_date = datetime.strptime(self.end_date, "%d%m%Y")
        nights = (self.end_date-self.start_date).days
        self.total_price = (self.room.price*nights)