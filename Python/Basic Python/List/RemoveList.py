# Remove list item
F = ["a", "b", "c"]
F.remove("b")
print(F)

# Remove Specified index
A = ["Table", "Chair", "Salong"]
A.pop(2)
print(A)

# Favorite movie
fav_movie = ["Sad man", "Ant man", "Hulk"]
print(fav_movie[1])

# Make the list of your favorite numbers and print the fist number
fav_number = ["3", "8", "17"]
print(fav_number[0])

# List: Add, insert, delete
movie = ["Iron man","Tinfy", "china"]
print(len(movie))
movie.append("Thor")
print(len(movie))
print(movie)
movie.insert(2,"Bad man")
print(movie)
del(movie[1])
print(movie)
del(movie[1:4])
print(movie)