def get_tuple(string):
    t1 = str(string).split('(')
    t1[1] = t1[1].replace(")", "")
    return tuple(t1)


def create_dictionary(my_dict):
    with open('Lab8\movie_list.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            word_list = line.split(',')
            actor = word_list[0]
            for word in word_list[1:]:
                word = word.strip()
                movie_year_tuple = get_tuple(word)
                if movie_year_tuple not in my_dict:
                    my_dict[movie_year_tuple] = set()
                my_dict[movie_year_tuple].add(actor)

    return my_dict


def menu(my_dict):
    while True:
        movies = input("Please enter two movies as 'name (year)' separated by"
                       "the appropriate operator (&, |, -), or enter '.' to quit:")

        if movies == ".":
            break

        if "&" in movies:
            (movie1, year1) = get_tuple(movies.split(" & ")[0])
            (movie2, year2) = get_tuple(movies.split(" & ")[1])

            try:
                print(my_dict[(movie1, year1)].intersection(my_dict[(movie2, year2)]))
            except KeyError:
                print("Movies not in the dictionary")

        if "|" in movies:
            (movie1, year1) = get_tuple(movies.split(" | ")[0])
            (movie2, year2) = get_tuple(movies.split(" | ")[1])

            try:
                print(my_dict[(movie1, year1)].union(my_dict[(movie2, year2)]))
            except KeyError:
                print("Movies not in the dictionary")

        if "-" in movies:
            (movie1, year1) = get_tuple(movies.split(" - ")[0])
            (movie2, year2) = get_tuple(movies.split(" - ")[1])

            try:
                print(my_dict[(movie1, year1)].difference(my_dict[(movie2, year2)]))
            except KeyError:
                print("Movies not in the dictionary")


def main():
    my_dict = {}
    create_dictionary(my_dict)
    menu(my_dict)


main()