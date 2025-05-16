import os
from dotenv import load_dotenv
import requests
from io import BytesIO

load_dotenv()

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

def map_generator(lat, lon):

    url = (f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lon}&zoom=17&size=200x200&maptype=satellite&markers=color:blue%7C{lat},{lon}&key={GOOGLE_MAPS_API_KEY}")

    response = requests.get(url)

    return BytesIO(response.content)