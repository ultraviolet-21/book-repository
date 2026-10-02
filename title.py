#lookup by title
import os
API_KEY = os.getenv("ISBNDB_API_KEY")
    

import requests

def lookup_by_title(title, author):

    parsed_title = "%20".join(title.split())

    url = f"https://api2.isbndb.com/books/{parsed_title}"

    headers = {
        "Authorization": API_KEY
    }

    params = {
        "author": author
    }

    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    response.raise_for_status()

    data = response.json()

    print(len(data))

    return data["books"]


def select_book(books):
    for i in range(len(books)):
        book = books[i]
        print(f'{i+1}. Title: {book["title"]}')
        for k in ["Authors", "Publisher", "Edition"]:
            if k.lower() in book:
                print(f'{k}: {book[k.lower()]}')
        
        print(f'ISBN: {book["isbn"]}')

    n = int(input("Which book do you want? "))
    isbn = books[n-1]["isbn"]
    return int(isbn)
