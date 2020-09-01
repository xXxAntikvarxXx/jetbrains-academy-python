class Movie:
    # create class here

    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year


# objects of the class Movie
titanic = Movie("Titanic", "James Cameron", 1997)
star_wars = Movie("Star Wars", "George Lucas", 1977)
fight_club = Movie("Fight Club", "David Fincher", 1999)
