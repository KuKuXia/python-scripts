from random import choice


def random_name_generator(first, second, x):
    """
        Generates random names.
        Arguments:
         - list of first names
         - list of last names
         - number of random names
    """
    names_list = []
    for i in range(x):
        names_list.append("{0} {1}".format(choice(first), choice(second)))
    return set(names_list)


first_names = ["Drew", "Mike", "Landon", "Jeremy", "Tyler", "Tom", "Avery"]
last_names = ["Smith", "Jones", "Brighton", "Taylor"]
names = random_name_generator(first_names, last_names, 5)
print('\n'.join(names))
