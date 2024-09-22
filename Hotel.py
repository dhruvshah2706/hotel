from csv import writer
from pandas import read_csv
from Room import Room
from openpyxl import load_workbook

class Hotel:
    def __init__(self, room_obj):
        self.name = "Hotel California"       
        self.rooms = room_obj        
        self.bookings = None   

    def add_room(self):
        file = open('data/room_info.csv', 'a', newline='')
        self.rooms.room_number = int(self.rooms.room_number)
        self.rooms.price = float(self.rooms.price)
        Writer = writer(file)
        line = ["Room Number","Room Type","Price per night","Booked Dates"]
        Writer.writerow(list)
        line = [self.rooms.room_number, self.rooms.room_type, self.rooms.price]
        Writer.writerow(line)
        file.close()
    
    def available_rooms(start_date, end_date):
        df = read_csv('data/room_info.csv')
        df = df.values.tolist()
        available = []
        for line in df:
            room = Room(line[0])
            if room.is_available(start_date,end_date):
                available.append(room)
        return available
    
    def make_booking(self,customer_obj,start_date, end_date):
        booking_id = 1
        # if(read_csv('data/bookings.csv')):
        #     df = read_csv('data/bookings.csv')
        #     df = df.values.tolist()
        #     booking_id = int(df[len(df)-1][0]) + 1
        # else:
            # booking_id = 1
        self.bookings = customer_obj.add_booking(booking_id, self.rooms,start_date,end_date)
        self.rooms.booked_dates.extend([start_date, end_date])

        #adds the booked_dates to room_info.csv
        df = read_csv('data/room_info.csv')
        df = df.values.tolist()
        file = open('data/room_info.csv', 'w', newline='')
        Writer = writer(file)
        line = ["Room Number","Room Type","Price per night","Booked Dates"]
        Writer.writerow(line)
        for line in df:
            if(int(line[0]) == self.rooms.room_number):
                line = line[:1] + self.bookings.booked_dates
            Writer.writerow(line)
            # list.append(line)
        file.close()


        #adds info to customer.csv
        df = read_csv('data/customer_info.csv')
        df = df.values.tolist()
        file = open('data/customer_info.csv', 'w', newline='')
        Writer = writer(file)
        line = ["Customer ID","Name","email","phone number"]
        Writer.writerow(line)
        customer_exists = False
        for line in df:
            if line[1] == customer_obj.name and line[2] == customer_obj.email and line[3] == customer_obj.phone_number:
                customer_exists = True
                line.append(booking_id)
            Writer.writerow(line)
                
        if not customer_exists:
            customer_id = int(df[len(df)-1][0]) + 1
            line = [customer_id,customer_obj.name,customer_obj.email,customer_obj.phone_number,booking_id]
            Writer.writerow(line)
        file.close()

        #adds the booking to bookings.csv
        file = open('data/bookings.csv', 'a', newline='')
        Writer = writer(file)
        line = ["Booking ID","Customer ID","Room Number","Start Date","End Date","Total Price"]
        Writer.writerow(line)
        line = [booking_id,customer_id,self.rooms.room_number,start_date,end_date,self.bookings.total_price]
        Writer.writerow(line)
        file.close()

        #generates excel file
        wb = load_workbook("data/booking_info.xlsx")
        ws = wb.active
        data = [customer_obj.name, customer_obj.email,customer_obj.phone_number,self.rooms.room_number,
                self.rooms.room_type,start_date,end_date,self.bookings.total_price]
        ws.append(data)
        wb.save("data/booking_info.xlsx")
        



        
        

    
