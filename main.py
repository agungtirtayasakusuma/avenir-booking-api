from fastapi import FastAPI
from schemas import BookingCreate

app = FastAPI(
    title="Avenir Booking API"
)

# DATA SEMENTARA
bookings = [
    {
        "id": 1,
        "customer_id": 1,
        "tour_id": 1,
        "pax": 2,
        "status": "Pending"
    }
]

# HOME
@app.get("/")
def home():
    return {
        "message": "Welcome to Avenir Booking API"
    }


# GET BOOKINGS
@app.get("/bookings")
def get_bookings():
    return bookings


# CREATE BOOKING
@app.post("/booking")
def create_booking(booking: BookingCreate):

    booking_data = booking.model_dump()

    bookings.append(booking_data)

    return {
        "message": "Booking created",
        "data": booking_data
    }


# UPDATE BOOKING
@app.put("/booking/{booking_id}")
def update_booking(booking_id: int):

    for booking in bookings:

        if booking["id"] == booking_id:

            booking["status"] = "Paid"

            return {
                "message": "Booking updated",
                "data": booking
            }

    return {
        "message": "Booking not found"
    }


# DELETE BOOKING
@app.delete("/booking/{booking_id}")
def delete_booking(booking_id: int):

    for booking in bookings:

        if booking["id"] == booking_id:

            bookings.remove(booking)

            return {
                "message": "Booking deleted"
            }

    return {
        "message": "Booking not found"
    }
