"""
-Enter 'a' to add your movies, 'l' to see your movies, 'f' to find your movies and
 'q' to quit your movies

-Add movies
-See movies
-Find a movie
-Stop running the programs

"""

movies = []


def menu():
    user_input = input(
        "Enter 'a' to add your movies, 'l' to see your movies, 'f' to find your movies and 'q' to quit your movies: ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movie(movies)
        elif user_input == 'f':
            find_movie()
        else:
            print("Unknown command-please try again")

        user_input = input(
            "\nEnter 'a' to add your movies, 'l' to see your movies, 'f' to find your movies and 'q' to quit your movies: ")


def add_movie():
    name = input('Enter the movie name: ')
    director = input('Enter the movie director name: ')
    year = input('Enter the movie released year: ')

    movies.append({
        'name': name,
        'director': director,
        'year': year
    })


def show_movie(movies_list):
    for movie in movies_list:
        show_movie_details(movie)


def show_movie_details(movie):
    print(f"Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}")


def find_movie():
    find_by = input('What property of the movie are you looking for? Name, Director or Year.')
    looking_for = input('What value are you searching for?')
    found_movies = find_by_attribute(movies, looking_for, lambda x: x[find_by])

    show_movie(found_movies)


def find_by_attribute(items, expected, finder):
    found = []

    for i in items:
        if finder(i) == expected:
            found.append(i)

    return found


menu()
