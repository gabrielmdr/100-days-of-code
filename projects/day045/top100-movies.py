from bs4 import BeautifulSoup

with open("top100-movies.html") as top100file:
    content = top100file.read()

soup = BeautifulSoup(content, "html.parser")

movie_list = [movie.getText() for movie in soup.select("h3.jsx-2692754980")]

for index in range(len(movie_list)):
    if ")" in movie_list[index]:
        movie_list[index] = movie_list[index].split(") ")[1]

for index in range(len(movie_list)):
    print(f"{index + 1}. {movie_list[index]}")
