# Trailerinator

## About

This project is a submission for the Movie Trailer Website project in P1 of Udacity.com's Full Stack Nanodegree program.

A demo of the final result is available at [sean.sh/trailerinator](http://sean.sh/trailerinator/).

## Setup

1. [Install python](https://www.python.org/downloads/) 
2. `pip install lxml requests` (for scraping movie rating)
2. Run `python entertainment_center.py`
3. Open the generated HTML

## Usage

The list of movies is curated via some simple class instantiations inside of `entertainment_center.py`. Editing these values will affect the movies displayed on the generated HTML. The `Movie` class is in `media.py`.

To host your own movie website using this site as a template: 

1. Ensure steps 2 three 3 from the set up instructions are complete.
2. Copy the generated HTML to a public directory of your favorite web server.

## TODO

- add [imdb rating](http://www.imdb.com/plugins) widget to each movie
- Use web scraping/API's to compile the list of movies and automatically fetch the trailer url, poster, rating, et all.
- use python to update the year in meta tags (for seo)

## License

This software is licensed under the [WTFPL](http://www.wtfpl.net/txt/copying/).