# from pig_util import outputSchema

@outputSchema('word:chararray')
def country_full_name(initial):
    # dictionary with country initial as key and full country name as value
    countries = {
        "A": 'Austria',
        "G": 'Germany',
        "F": 'France',
        "E": 'England',
        "I": 'Italy',
        "R": 'Russia',
        "T": 'Turkey'
    }

    # return full country name from dictionary
    return countries.get(initial, initial)


def remove_quotes(str):
    # remove double quotes from initial
    return str.strip('"')
