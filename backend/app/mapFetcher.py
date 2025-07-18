import os
from dotenv import load_dotenv
import requests
from io import BytesIO

#Get Key
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

def map_generator(lat, lon):

    url = (f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lon}&zoom=17&size=200x200&maptype=satellite&markers=color:blue%7C{lat},{lon}&key={GOOGLE_MAPS_API_KEY}")

    response = requests.get(url)

    return BytesIO(response.content)