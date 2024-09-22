from datetime import datetime
from csv import writer
from Hotel import Hotel

# # Define the start and end dates in ddmmyyyy format
# start_date = "10012024"  # 1st January 2024
# end_date = "01012024"    # 10th January 2024
# date = "05012024"

# # Convert the strings to datetime objects using ddmmyyyy format
# start_date_obj = datetime.strptime(start_date, '%d%m%Y')
# end_date_obj = datetime.strptime(end_date, '%d%m%Y')
# date_obj = datetime.strptime(date, '%d%m%Y')
# # Calculate the number of nights
# if (date_obj - start_date_obj).days<0 and (date_obj - end_date_obj).days>0:
#     print("yes")
# else :
#     print("no")
# print((date_obj - start_date_obj).days)
# print((date_obj - end_date_obj).days)
# file = open('data/bookings.csv', 'w', newline='')
# Writer = writer(file)
# list = [1,2,451,"21102023","22102023"]
# Writer.writerow(list)
# file.close()

# start_date = str(input("Please enter your start date in 'DDMMYYYY' format (digits only): "))
# end_date = str(input("Please enter your end date in 'DDMMYYYY' format (digits only): "))
# available_rooms = Hotel.available_rooms(start_date,end_date)
# for room in available_rooms:
#     print(f"Room Number = {int(room.room_number)},\tRoom Type = {room.room_type},\tPrice per night = {room.price}")

# list = None
# for i in range(0,1,2):
#     print(i)

file = open('data/room_info.csv', 'a', newline='')
Writer = writer(file)
line = [451,"super deluxe",1000]
Writer.writerow(line)
line = [452,"elite",200]
Writer.writerow(line)
file.close()