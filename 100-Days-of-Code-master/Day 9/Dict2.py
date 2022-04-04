travel_log = [
    {
        "country": "France",
        "visited": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visited": 5,
        "cities": ["berlin", "hamburg", "stutt"]
    }
]


def add_new_country(country, visited, *cities):
    # first attempt
    # travel_log.append({"country" : country,"visited": visited,"cities": cities})
    new_country = {}
    new_country["country"] = country
    new_country["visited"] = visited
    new_country["cities"] = cities
    travel_log.append(new_country)


add_new_country("russia", 2, ["moscow", "saint", "lkgkg"])
print(travel_log)
