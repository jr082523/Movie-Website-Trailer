import media
import fresh_tomatoes
"""Here we are creating different movie objects
and calling the movie constructor in the media.py
file to initialize the movie objects"""
toy_story = media.Movie(
                       "Toy Story",
                       "A story of a boy and his toys that come to life",
                       "img/toystory.jpg",
                       "https://www.youtube.com/watch?v=vwyZH85NQC4"
                       )
baaghi_2 = media.Movie(
                        "Baaghi 2",
                        "A battle-hardened army officer squares off against..",
                        "img/baaghi21.jpg",
                        "https://www.youtube.com/watch?v=F2lN25IayH8"
                        )
sonu_ki_teetu = media.Movie(
                 "Sonu ki teetu",
                 "New age version of the same belief..",
                 "img/sonu.jpg",
                 "https://www.youtube.com/watch?v=M2q64UowX9g"
                 )

Avengers = media.Movie(
                       "Avengers",
                       "When Thor's evil brother,Loki, gains access..",
                       "img/avengers1.jpg",
                       "https://www.youtube.com/watch?v=6ZfuNTqbHE8"
                        )
october = media.Movie(
                        "October",
                        "Varun DHawan is living the life of any carefree..",
                        "img/october.jpg",
                        "https://www.youtube.com/watch?v=XyP4cW-mtqo"
                       )
Veere_Di_Wedding = media.Movie(
                    "VeereDiWedding",
                    "VEEREDIWEDDING is a high spirited and upbeat..",
                    "img/Veerediwedding.jpg",
                    "https://www.youtube.com/watch?v=IZODr96ZRCc"
                )

"""Here we are passing the movies array
to the function open_movies_page in tomatoes.py file
to call the function."""
movies =
[toy_story, baaghi_2, sonu_ki_teetu, Avengers, october, Veere_Di_Wedding]
fresh_tomatoes.open_movies_page(movies)
