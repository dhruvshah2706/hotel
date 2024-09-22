from pandas import read_csv
from datetime import datetime
from csv import writer

class Room:
    def __init__(self, room_number):
        self.room_number = room_number             
        df = read_csv('data/room_info.csv')
        df = df.values.tolist()
        for line in df:
            if room_number in line:
                self.room_type = line[1]
                self.price = line[2]
                if len(line)>4:
                    self.booked_dates = line[3:]
                else:
                    self.booked_dates = []
                    print(len(self.booked_dates))
        


    def is_available(self, start_date, end_date):
        start_date = datetime.strptime(start_date, '%d%m%Y')
        end_date = datetime.strptime(end_date, '%d%m%Y')
        for i in range(0,len(self.booked_dates),2):
            print(i)
            date1 = datetime.strptime(self.booked_dates[i], '%d%m%Y')
            date2 = datetime.strptime(self.booked_dates[i+1], '%d%m%Y')
            if not (((start_date - date1).days < 0 and (end_date - date1).days < 0) 
                    or ((start_date - date2).days > 0 and (end_date - date2).days > 0)):
                return False
        return True
    
    def add_booking(self, start_date, end_date): #this logic should be applied in customer.py
        self.booked_dates.extend([start_date, end_date])
        # self.room_number = int(self.room_number)
        # df = read_csv('data/room_info.csv', header=None)
        # df = df.values.tolist()
        # # list = []
        # file = open('data/room_info.csv', 'w', newline='')
        # Writer = writer(file)
        # for line in df:
        #     if(int(line[0]) == self.room_number):
        #         line.extend([self.bookings.start_date, self.bookings.end_date])
        #     Writer.writerow(line)
        #     # list.append(line)
        # file.close()
        # # print(list)
            
# Room.add_booking(444,"21012024","25052024")

    

# l = ["21012024","24012024","01022024","07022024","10022024","12022024"]
# start_date = "23012024"
# end_date = "25012024"
# print(Room.is_available(start_date,end_date,l))

        
