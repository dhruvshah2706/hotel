from Hotel import Hotel
from Customer import Customer
from Room import Room

name = input("Please enter your name: ")
email = input("Please enter your email: ")
phone_number = input("Please enter your phone number: ")
start_date = str(input("Please enter your start date in 'DDMMYYYY' format (digits only): "))
end_date = str(input("Please enter your end date in 'DDMMYYYY' format (digits only): "))
available_rooms = Hotel.available_rooms(start_date,end_date)
print("Available rooms : ")
for room in available_rooms:
    print(f"Room Number = {int(room.room_number)},\tRoom Type = {room.room_type},\tPrice per night = {room.price}")

room_number = 0
flag = False
while(not flag):
    room_number = int(input("Enter room number to proceed with booking:"))
    for room in available_rooms:
        if room_number == room.room_number:
            flag = True
            break
    if not flag:
        print("Invalid room number")

room_obj = Room(room_number)
customer_obj = Customer(name,email,phone_number)
hotel_obj = Hotel(room_obj)
hotel_obj.make_booking(customer_obj,start_date,end_date)



    
