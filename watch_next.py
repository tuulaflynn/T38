import spacy
# Load the more advance language model "en_core_web_md"
# which finds similarities and difference better than the previously used "en_core_web_sm".
nlp = spacy.load("en_core_web_md")


def return_lines_movies_f():
    # Function returns a list of the lines from movies.txt database.
    with open("movies.txt", "r", encoding="utf-8-sig") as movies_f:
        lines = movies_f.readlines()
    return lines


def movies_dict():
    # Function returns a dictionary where the key is the movie title and the value is the movie description.
    # The data is from database movies.txt acquired from function return_lines_movies().
    movies_dictionary = {}
    for movie in return_lines_movies_f():
        title_description = movie.split(" :")
        movies_dictionary[title_description[1].strip("\n")] = title_description[0]
        # Removed new line character for each line (i.e. the end of each description) for readability.
    return movies_dictionary


def watch_next(seen_movie, seen_movie_description):
    """
    Function tells the user which movie to watch next. It finds which movie description in database movies.txt
    has the highest similarity to the users last seen movie description.
    :param seen_movie: title of the users last watched movie
    :param seen_movie_description: description of the users last watched movie
    :return: the movie title and description the user should next watch.
    """
    similarity_no = 0
    most_similar_title = None

    for movie_description in movies_dict().keys():
        movie_description = nlp(movie_description)

        if nlp(seen_movie_description).similarity(movie_description) > similarity_no:
            similarity_no = nlp(seen_movie_description).similarity(movie_description)
            most_similar_title = movies_dict()[f"{movie_description}"]
            most_similar_description = movie_description

    return f"The most similar film to your last watch, {seen_movie}, is {most_similar_title}, with synopsis..." \
           f"\n{most_similar_description}. "


user_movie_name = "Planet Hulk"
user_movie_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, " \
                        "the Illuminati trick Hulk into a shuttle and launch him into space to a plant " \
                        "where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where " \
                        "he is sold into slavery and trained as a gladiator."


print(watch_next(user_movie_name, user_movie_description))


