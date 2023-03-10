import os
from dotenv import load_dotenv

load_dotenv()

env = os.getenv("PYTHON_ENV") or "development"

jwt_secret_key = os.getenv("JWT_SECRET_KEY")

postgres = {
    "production": {
        "host": os.getenv("POSTGRES_PROD_HOST"),
        "database": os.getenv("POSTGRES_PROD_DATABASE"),
        "user": os.getenv("POSTGRES_PROD_USER"),
        "password": os.getenv("POSTGRES_PROD_PASSWORD"),
        "port": os.getenv("POSTGRES_PROD_PORT"),
    },
    "development": {
        "host": os.getenv("POSTGRES_DEV_HOST"),
        "database": os.getenv("POSTGRES_DEV_DATABASE"),
        "user": os.getenv("POSTGRES_DEV_USER"),
        "password": os.getenv("POSTGRES_DEV_PASSWORD"),
        "port": os.getenv("POSTGRES_DEV_PORT"),
    },
}

google_places_api_key = os.getenv("GOOGLE_PLACES_API_KEY")

aws = {"aws_api_user": os.getenv("AWS_API_USER"),
       "aws_api_key": os.getenv("AWS_API_KEY"),
       "aws_region": "us-west-2"}

keyword_list = [
    "airport",
    "amusement_park",
    "aquarium",
    "art_gallery",
    "bakery",
    "bank",
    "bar",
    "book_store",
    "bowling_alley",
    "bus_station",
    "cafe",
    "campground",
    "car_rental",
    "casino",
    "cemetery",
    "church",
    "city_hall",
    "clothing_store",
    "convenience_store",
    "courthouse",
    "dentist",
    "department_store",
    "doctor",
    "drugstore",
    "electronics_store",
    "embassy",
    "fire_station",
    "florist",
    "gas_station",
    "gym",
    "hardware_store",
    "hindu_temple",
    "hospital",
    "jewelry_store",
    "laundry",
    "library",
    "light_rail_station",
    "liquor_store",
    "locksmith",
    "lodging",
    "mosque",
    "movie_theater",
    "museum",
    "night_club",
    "park",
    "parking",
    "pet_store",
    "pharmacy",
    "police",
    "post_office",
    "restaurant",
    "rv_park",
    "school",
    "shoe_store",
    "shopping_mall",
    "spa",
    "stadium",
    "store",
    "subway_station",
    "supermarket",
    "synagogue",
    "taxi_stand",
    "tourist_attraction",
    "train_station",
    "travel_agency",
    "university",
    "zoo",
]
