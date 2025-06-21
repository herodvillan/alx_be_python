class Book:
    def __init__(self, title, author, year):  # fix: should be __init__
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):  # fix: should be __str__
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):  # fix: should be __repr__
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):  # fix: should be __del__
        print(f"Deleting {self.title}")

