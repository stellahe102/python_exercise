# the previous version works generally, but the test requires output to be a string
# so made modifiction
# add a list to store the key+value string
# sort the dictionary by key to match the test result in hackerrank
# write a function to return the city name and rainfall amount via user input
# when user presses enter, stop the prompt and print out the result
# result need to be a string in format of:
#   Boston: 7
#   Toronto: 9
def get_rainfall():
    # initiate an empty dictionary
    rain_dict = dict()
    # initiate an empty list to store the output
    output = list()
    while True:
        city_name = input('enter the name of city here:')
        # normalize the string input
        city_name = city_name.upper()
        # if the user presses enter when prompted with city name input
        # exit the loop
        if city_name == '':
            break
        rainfall = input('enter the amount of rainfall in millimeter here:')
        # put the city name and accumulated rainfall in the dictionary
        rain_dict[city_name] = rain_dict.get(city_name, 0) + int(rainfall)
        rain_dict = dict(sorted(rain_dict.items()))
    for key, value in rain_dict.items():
        output.append(key + ': ' + str(value))
        final_output = '\n'.join(output)
    return f'_________________________________\nA summary of all entries is: \n\n{final_output}'
print(get_rainfall())
