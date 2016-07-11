import webbrowser


class Movie():
    """
    This is a class for movie objects that can store information about the
    title, synopsis, movie poster and a link to the trailer
    """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, movie_director,
                 movie_year, poster_image, youtube_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.director = movie_director
        self.year = movie_year
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer
        print("Generating instance of " + self.title)


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)