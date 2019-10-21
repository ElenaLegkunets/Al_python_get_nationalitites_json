import json

handle = open("nationalities.csv", "r")
list_of_dicts = []

for line in handle:
    splitted_string = line.split(";")
    country = splitted_string[0]
    nationality = splitted_string[1]
    icao_code = splitted_string[2]

    dict = {}
    dict['country'] = country
    dict['nationality'] = nationality
    dict['icao'] = icao_code

    list_of_dicts.append(dict)

handle.close()

final_json = {}
final_json["nationality"] = list_of_dicts
#print (json.dumps(final_json, indent = 2))

handle2 = open("result_nationalities.json", "w")
handle2.write(json.dumps(final_json, indent = 4))
handle2.close()
