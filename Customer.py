import pandas as pd
from csv import writer
from openpyxl import Workbook
from Booking import Booking


class Customer:
    def __init__(self, name, email, phone_number):
        self.name = name                          
        self.email = email                        
        self.phone_number = phone_number          
        self.bookings = None             

    def add_booking(self, booking_id, room_obj, start_date, end_date):
        self.bookings = Booking(booking_id,self,room_obj,start_date,end_date)
        self.bookings.calc_price()
        return self.bookings
