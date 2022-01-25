# We stick with importing the csv module as it is in standard library
# Check here fro a module free version:
# https://github.com/dominikb1888/refactoring_exercise/blob/no_modules/python/funding_raised.py
import csv


class FundingRaised:
    # The original class does not contain a proper init function ("Constructor")
    # The alternative to this would be having a separate _read_csv() function
    # However, the interface is cleaner like this
    # ATTENTION: You need to change the test.py for this to accomodate to the new
    # object being generated
    def __init__(self, path="../startup_funding.csv"):
        # We can have a standard attribute on the path variable to direct to our path
        self.path = path
        with open(self.path, "rt") as csvfile:
            # most of what the original code did is actually reduce to this line
            # It reads a CSV and transforms to a DICT csv.DictReader() is doing this
            self.data = [row for row in csv.DictReader(csvfile)]

    def _filter_dict(data, options):
        if options:
            # The second thing the original script did was to filter variables and return either
            # all results (where()) or just results from the first occurence (find_by())
            # In fact this function handles this all and allows us to only expose where & find_by.
            # WHAT HAPPENS HERE:
            # We are recursing through the keys of the options passed in by the user
            # deleting the option after processing it to filter the data
            # If the key yielded a result it is appended to the result
            # Recursion stops if options.keys() are empty and result is passed back.
            key = list(options.keys())[0]
            result = [row for row in data if row[key] == options[key]]
            del options[key]

        return FundingRaised._filter_dict(result, options) if options else result

    def where(self, options={}):
        return FundingRaised._filter_dict(self.data, options)

    def find_by(self, options):
        result = FundingRaised._filter_dict(self.data, options)
        return result[0]


class RecordNotFound(Exception):
    pass
