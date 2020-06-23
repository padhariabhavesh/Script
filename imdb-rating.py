# Programmer - Bhavesh Padharia
#find imdb rating of any movies or series


import imdb

ia = imdb.IMDb()
code = "8946378"
movie = ia.get_movie(code)
rating = movie.data['rating']

print(movie)
print(rating)

