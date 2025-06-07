import requests
import os
from dotenv import load_dotenv

load_dotenv()

def search_books(keyword="mental health"):
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {"q": keyword, "maxResults": 3}
    response = requests.get(url, params=params)

    if response.status_code != 200:
        return ["❌ Error pulling book data."]

    results = response.json().get("items", [])
    books = []

    for item in results:
        volume = item["volumeInfo"]
        title = volume.get("title", "Unknown Title")
        authors = ", ".join(volume.get("authors", ["Unknown Author"]))
        link = volume.get("infoLink", "#")

        books.append(f"📘 **{title}** by {authors}\n[More info →]({link})")

    return books
