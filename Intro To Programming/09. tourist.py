destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]


def get_destination_index(destination):
    for place in destinations:
        if place == destination:
            destination_index = destinations.index(place) 
    return destination_index

def get_traveler_location(traveler):
    traveler_destination = test_traveler [1]
    return traveler_destination


# traveler_destination_index = get_destination_index(get_traveler_location("Erin Wilkes"))
# print (traveler_destination_index)

attractions = [[] for place in destinations]
# print (attractions)

def add_attraction(destination, attraction):
    # Find the index of the destination
    destination_index = get_destination_index(destination)
    
    # If the destination exists, add the attraction to the corresponding list
    if destination_index is not None:
        attractions_for_destination = attractions[destination_index]
        attractions_for_destination.append(attraction)
    else:
        print("Destination not found!")

# print (attractions)

add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction ("Los Angeles, USA",['Venice Beach', ['beach']])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# print (attractions)


def find_attractions (destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions [destination_index]
    attractions_with_interest = []
    for attraction in attractions_in_city:
        possible_attraction = attraction
        attraction_tags = possible_attraction [1]
        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append (possible_attraction[0])
    return attractions_with_interest

# la_arts = find_attractions ("Los Angeles, USA" ,['art'])
# print (la_arts)



def get_attractions_for_traveler (traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler [2]
    traveler_attractions = find_attractions (traveler_destination, traveler_interests)
    #print (traveler_attractions)
    interests_string = f"Hi {traveler[0]}, we think you'll like these places around {traveler_destination}: "
    #print (interests_string)

    # Use a flag to handle the comma
    has_previous_attraction = False
    
    for attraction in traveler_attractions:
        # Add a comma and space before the attraction if there is a previous attraction
        if has_previous_attraction:
            interests_string += ", "
        
        interests_string += attraction
        has_previous_attraction = True
    
    return interests_string

smills_france = get_attractions_for_traveler (['Dereck Smill', 'Paris, France', ['monument']])
print (smills_france)