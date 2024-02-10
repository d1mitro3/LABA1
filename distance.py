def distance(sites):
    distances = {}
    for city1, cord1 in sites.items():
        distances[city1] = {}
        for city2, cord2 in sites.items():
            if city1 != city2:
                distance = ((cord1[0] - cord2[0]) ** 2 + (cord1[1] - cord2[1]) ** 2) ** 0.5
                distances[city1][city2] = distance
    return distances
