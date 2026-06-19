from pydantic import BaseModel


class BookingCreate(BaseModel):
    customer_id: int
    tour_id: int
    pax: int
    status: str