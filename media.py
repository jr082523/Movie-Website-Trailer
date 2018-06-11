"""Defines the Movie class that contains the details of a movie."""
import webbrowser


class Movie():
    """This class provides a way to store movie related information.
    Attributes:
    title: A string to store title of the movie.
    storyline: A string to store basic plot of the movie.
    poster_image_url: A string to store url of the movie poster.
    youtube_trailer_url: A string to store url of the movie trailer.
   """
    def __init__
    (self, movie_title, movie_storyline, poster_image, trailer_youtube):
                """Initializes movie class instance variables"""
    self.title = movie_title
    self.storyline = movie_storyline
    self.poster_image_url = poster_image
    self.trailer_youtube_url = trailer_youtube


def show_trailer(self):
    """Plays the movie trailer in the web browser"""
    webbrowser.open(self.trailer_youtube_url)
