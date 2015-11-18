import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                  "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                  "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                  "tt0499549")

# print(toy_story.storyline)

avatar = media.Movie("Avatar", "A marine on an alien planet",
                "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                "tt0499549")

school_of_rock = media.Movie("School Of Rock", "Storyline",
                "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                "https://www.youtube.com/watch?v=3PsUJFEBC74",
                "tt0499549")

ratatouille = media.Movie("Ratatouille", "Storyline",
                "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                "https://www.youtube.com/watch?v=c3sBBRxDAqk",
                "tt0499549")

midnight_in_paris = media.Movie("Midnight In Paris", "Storyline",
                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                "https://www.youtube.com/watch?v=FAfR8omt-CY",
                "tt0499549")

hunger_games = media.Movie("Hunger Games", "Storyline",
                "https://upload.wikimedia.org/wikipedia/en/4/4b/Hunger_Games_Film_Poster.jpg",
                "https://www.youtube.com/watch?v=mfmrPu43DF8",
                "tt0499549")

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)
