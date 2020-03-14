def format_place(city, country, population = ''):
    """Neatly formats the city and country name in the form city, country."""
    if population:
        place = city + ", " + country + " - population " + str(population)
    else:
        place = city + ", " + country
    return place.title()