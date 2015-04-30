#Imports python's builtin webbrowser utility which allows the user of web browser in program
import webbrowser

#Creates a class call Movie, that takes 4 arguments to create instances/objects of the class
class Movie():
    #Creates the instance/object with the given parameters
    def __init__(self, movie_title, movie_storyline, poster_image,
               trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #Creates a function that will open url of the instance class
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
