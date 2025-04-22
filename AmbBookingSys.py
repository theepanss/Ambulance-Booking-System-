import time
import uuid
from datetime import datetime

# In-memory storage for bookings
bookings = []

def generate_booking_id():
    return str(uuid.uuid4())[:8]

def request_ambulance():
    print("\n--- Ambulance Booking Form ---")
    name = input("Enter patient's name: ")
    age = input("Enter patient's age: ")
    contact = input("Enter contact number: ")
    location = input("Enter pickup location: ")
    
    booking_id = generate_booking_id()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    booking = {
        "id": booking_id,
        "name": name,
        "age": age,
        "contact": contact,
        "location": location,
        "time": timestamp
    }

    bookings.append(booking)
    print(f"\n✅ Ambulance booked successfully!")
    print(f"📄 Booking ID: {booking_id}")
    print(f"📍 Location: {location}")
    print(f"🕒 Time: {timestamp}\n")

def view_bookings():
    if not bookings:
        print("\n⚠ No bookings found.")
        return
    
    print("\n📋 All Bookings:")
    for b in bookings:
        print(f"[{b['id']}] {b['name']} ({b['age']} yrs) - {b['location']} at {b['time']}")

def main_menu():
    while True:
        print("\n====== Ambulance Booking System ======")
        print("1. Request Ambulance")
        print("2. View All Bookings")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            request_ambulance()
        elif choice == '2':
            view_bookings()
        elif choice == '3':
            print("👋 Exiting system. Stay safe!")
            break
        else:
            print("❌ Invalid option. Try again.")

# Corrected line here
if __name__ == "__main__":
    main_menu()
