import random
from app.models import Book
from datetime import datetime, timedelta
from icecream import ic as iprint

today = datetime.today().date()
date_choices = [(today + timedelta(days=offset)).strftime('%Y-%m-%d') for offset in range(-3, 4)]
language_choices = ["English", "Hindi", "French", "Spanish", "Italian"]

books_data = [
    {"title": "The Great Adventure", "author": "John Smith", "pages": 320, "publication_date": "2023-05-01", "language": "English"},
    {"title": "Mystery of the Moon", "author": "Sara Lee", "pages": 250, "publication_date": "2022-08-12", "language": "English"},
    {"title": "Journey Through Time", "author": "Andrew Turner", "pages": 280, "publication_date": "2021-03-19", "language": "English"},
    {"title": "The Hidden Treasure", "author": "Laura James", "pages": 330, "publication_date": "2020-11-22", "language": "English"},
    {"title": "Dreams of Tomorrow", "author": "Michael Walker", "pages": 150, "publication_date": "2023-01-10", "language": "English"},
    {"title": "Escape from Reality", "author": "Emily Davis", "pages": 220, "publication_date": "2019-07-15", "language": "English"},
    {"title": "The Lost City", "author": "David Clark", "pages": 400, "publication_date": "2018-09-05", "language": "English"},
    {"title": "In the Shadow of Giants", "author": "Olivia Taylor", "pages": 450, "publication_date": "2020-02-20", "language": "English"},
    {"title": "The Secret Vault", "author": "James Wilson", "pages": 350, "publication_date": "2022-10-11", "language": "English"},
    {"title": "Beneath the Surface", "author": "Sophia Moore", "pages": 270, "publication_date": "2023-04-30", "language": "English"},
    {"title": "Whispers of the Wind", "author": "Jack Harris", "pages": 320, "publication_date": "2017-06-03", "language": "English"},
    {"title": "The Final Hour", "author": "Isabella Martinez", "pages": 290, "publication_date": "2021-12-25", "language": "English"},
    {"title": "The Ancient Code", "author": "Thomas Lee", "pages": 500, "publication_date": "2022-01-09", "language": "English"},
    {"title": "Under the Stars", "author": "Ethan Robinson", "pages": 410, "publication_date": "2020-04-15", "language": "English"},
    {"title": "Fury of the Storm", "author": "Ava Wilson", "pages": 330, "publication_date": "2019-11-20", "language": "English"},
    {"title": "Path of the Wanderer", "author": "Benjamin Scott", "pages": 370, "publication_date": "2021-07-08", "language": "English"},
    {"title": "Through the Looking Glass", "author": "Charlotte Baker", "pages": 320, "publication_date": "2023-02-17", "language": "English"},
    {"title": "Echoes of the Past", "author": "Liam Green", "pages": 390, "publication_date": "2022-03-29", "language": "English"},
    {"title": "The Final Countdown", "author": "Ella Adams", "pages": 280, "publication_date": "2020-10-30", "language": "English"},
    {"title": "Rising Sun", "author": "Lucas Carter", "pages": 310, "publication_date": "2021-01-14", "language": "English"},
    {"title": "The Lost Legend", "author": "Zoe Fisher", "pages": 240, "publication_date": "2023-07-25", "language": "English"},
    {"title": "Whispers of the Past", "author": "Joshua Harris", "pages": 330, "publication_date": "2022-09-19", "language": "English"},
    {"title": "Tides of Change", "author": "Megan Evans", "pages": 260, "publication_date": "2021-05-12", "language": "English"},
    {"title": "The Hidden Key", "author": "Alexander King", "pages": 350, "publication_date": "2020-03-17", "language": "English"},
    {"title": "Stolen Secrets", "author": "Victoria Allen", "pages": 390, "publication_date": "2019-12-10", "language": "English"},
    {"title": "Shadows in the Night", "author": "Samuel Wright", "pages": 420, "publication_date": "2022-11-23", "language": "English"},
    {"title": "Rise of the Fallen", "author": "Grace Walker", "pages": 500, "publication_date": "2021-06-01", "language": "English"},
    {"title": "Beyond the Horizon", "author": "Adam Stone", "pages": 450, "publication_date": "2020-08-04", "language": "English"},
    {"title": "Labyrinth of Shadows", "author": "Daisy Reed", "pages": 300, "publication_date": "2023-09-16", "language": "English"},
    {"title": "The Last Wish", "author": "Peter Miles", "pages": 275, "publication_date": "2021-03-21", "language": "English"},
    {"title": "Guardians of the Light", "author": "Ivy Grant", "pages": 350, "publication_date": "2022-05-12", "language": "English"},
    {"title": "Ocean's Whisper", "author": "Sean Ford", "pages": 290, "publication_date": "2019-11-08", "language": "English"},
    {"title": "The Desert Mirage", "author": "Eva Brooks", "pages": 330, "publication_date": "2023-10-22", "language": "English"},
    {"title": "The Silver Phoenix", "author": "Dylan Snow", "pages": 420, "publication_date": "2020-01-19", "language": "English"},
    {"title": "City of Glass", "author": "Riley Shaw", "pages": 250, "publication_date": "2018-07-31", "language": "English"},
    {"title": "Land of Secrets", "author": "Olive Bennett", "pages": 375, "publication_date": "2021-09-11", "language": "English"},
    {"title": "The Forsaken Path", "author": "Chris Fields", "pages": 330, "publication_date": "2022-02-25", "language": "English"},
    {"title": "Broken Mirrors", "author": "Taylor Hughes", "pages": 310, "publication_date": "2020-11-15", "language": "English"},
    {"title": "Echo of Silence", "author": "Jordan Rose", "pages": 460, "publication_date": "2023-05-20", "language": "English"},
    {"title": "Wings of Destiny", "author": "Morgan Lane", "pages": 280, "publication_date": "2019-04-07", "language": "English"},
    {"title": "The Lost Artifact", "author": "Casey Hill", "pages": 300, "publication_date": "2021-10-12", "language": "English"},
    {"title": "Valley of Hope", "author": "Payton Woods", "pages": 380, "publication_date": "2017-06-02", "language": "English"},
    {"title": "The Crystal Labyrinth", "author": "Alex Morgan", "pages": 340, "publication_date": "2020-08-18", "language": "English"},
    {"title": "Heart of the Forest", "author": "Dakota Webb", "pages": 310, "publication_date": "2021-05-27", "language": "English"},
    {"title": "Dawn of the New Era", "author": "Sawyer Reid", "pages": 430, "publication_date": "2019-01-23", "language": "English"},
    {"title": "The Enchanted Isles", "author": "Harper Knox", "pages": 255, "publication_date": "2022-07-15", "language": "English"},
    {"title": "Empire of Gold", "author": "Skylar Lane", "pages": 370, "publication_date": "2023-02-09", "language": "English"},
    {"title": "The Whispering Trees", "author": "Charlie Sinclair", "pages": 300, "publication_date": "2018-12-11", "language": "English"},
    {"title": "Beyond the Veil", "author": "Rowan Jordan", "pages": 315, "publication_date": "2020-09-27", "language": "English"},
    {"title": "Flames of War", "author": "Drew Logan", "pages": 490, "publication_date": "2021-03-03", "language": "English"}
]


def run():
    Book.objects.all().delete()
    for book_data in books_data:
        book = Book(
            title=book_data["title"],
            author=book_data["author"],
            pages=book_data["pages"],
            publication_date=random.choice(date_choices),
            language=random.choice(language_choices)
        )
        book.save()
        iprint(f"Created: {book.title} by {book.author}")
    iprint("Book creation script.")

# Run the script only if this file is called directly
if __name__ == "__main__":
    run()