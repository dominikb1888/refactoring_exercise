import csv


class FundingRaised:
    def __init__(self, path="../startup_funding.csv"):
        self.path = path
        with open(self.path, "rt") as csvfile:
            file_data = csv.reader(csvfile, delimiter=",", quotechar='"')
            self.headers = next(file_data)
            self.data = [dict(zip(self.headers, i)) for i in file_data]

    def _filter_csv(data, options):
        if options:
            key = list(options.keys())[0]
            fltrd = [row for row in data if row[key] == options[key]]
            del options[key]

        return FundingRaised._filter_csv(fltrd, options) if options else fltrd

    def where(self, options={}):
        return FundingRaised._filter_csv(self.data, options)

    def find_by(self, options):
        result = FundingRaised.where(self, options=options)
        return result[0]


class RecordNotFound(Exception):
    pass
