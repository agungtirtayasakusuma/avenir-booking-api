from fastapi import FastAPI
from database import conn, cursor

app = FastAPI(
    title="Avenir Booking API"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Avenir Booking API"
    }


@app.get("/bookings")
def get_bookings():

    cursor.execute("""
        SELECT *
        FROM bookings
        ORDER BY booking_id
    """)

    data = cursor.fetchall()

    return data