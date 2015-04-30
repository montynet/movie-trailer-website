#Makes the fresh_tomatoes py program available to be used in this file
#File was shared in Udacity's Full Stack Web Developer nanodegree
import fresh_tomatoes
##Makes the media py progam available in this file. Located within the same
#directory
import media


#Creates an instance/object of Movie with specific film
schindlers_list = media.Movie("Schindler's List",
                        "A story of courage and history",
                        "http://upload.wikimedia.org/wikipedia/en/3/38/Schindler%27s_List_movie.jpg",
                        "https://www.youtube.com/watch?v=JdRGC-w9syA")

#Creates an instance/object of Movie with specific film
a_beautiful_mind = media.Movie("A Beautiful Mind","A genious with a mental illness",
                     "http://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg",
                     "https://www.youtube.com/watch?v=aS_d0Ayjw4o")

#Creates an instance/object of Movie with specific film
me_myself_irene = media.Movie("Me Myself & Irene",
                             "A story of a man with dual personalities",
                             "http://upload.wikimedia.org/wikipedia/en/0/02/Me%2C_Myself_and_Irene_Posters.jpg",
                             "https://www.youtube.com/watch?v=ssx_riw1Y9Y")

#Creates an instance/object of Movie with specific film
fight_club = media.Movie("Fight Club", "A story about fights",
                             "http://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                             "https://www.youtube.com/watch?v=SUXWAEX2jlg")


#Creates an instance/object of Movie with specific film
catch_me_if_you_can = media.Movie("Catch Me If You Can", "A never ending lie",
                          "http://upload.wikimedia.org/wikipedia/en/4/4d/Catch_Me_If_You_Can_2002_movie.jpg",
                          "https://www.youtube.com/watch?v=hFj3OXVL_wQ")

#Creates an array/list of the instances of Movie, used to pas
movies = [schindlers_list, a_beautiful_mind,me_myself_irene, fight_club, catch_me_if_you_can]

#Calls the open_movies_page method to actually make the html for us
fresh_tomatoes.open_movies_page(movies)
