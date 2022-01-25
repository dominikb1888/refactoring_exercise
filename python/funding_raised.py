import csv


class FundingRaised:
    def __init__(self, path="../startup_funding.csv"):
        self.path = path
        with open(self.path, "rt") as csvfile:
            self.data = [row for row in csv.DictReader(csvfile)]

    def _filter_csv(data, options):
        if options:
            # We are recursing through the keys of the options passed in by the user
            # deleting the option after processing it to filter the data
            # If the key yielded a result it is appended to the result
            # Recursion stops if options.keys() are empty and result is passed back.
            key = list(options.keys())[0]
            result = [row for row in data if row[key] == options[key]]
            del options[key]

        return FundingRaised._filter_csv(result, options) if options else result

    def where(self, options={}):
        return FundingRaised._filter_csv(self.data, options)

    def find_by(self, options):
        result = FundingRaised.where(self, options=options)
        return result[0]


class RecordNotFound(Exception):
    pass
