import csv


class FundingRaised:
    def __init__(self, filepath="../startup_funding.csv"):
        with open(filepath, "rt") as csvfile:
            self.data = [row for row in csv.DictReader(csvfile)]

    @staticmethod
    def _filter(data, options):
        return (row for row in data if row | options == row)

    def where(self, options={}):
        return list(FundingRaised._filter(self.data, options))

    def find_by(self, options={}):
        return next(FundingRaised._filter(self.data, options))
