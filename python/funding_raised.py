import csv


class FundingRaised:
    def filter_csv(csv_data, options):
        if options:
            key = list(options.keys())[0]
            fltrd = [row for row in csv_data if row[key] == options[key]]
            del options[key]

        return FundingRaised.filter_csv(fltrd, options) if options else fltrd

    def where(options={}):
        with open("../startup_funding.csv", "rt") as csvfile:
            file_data = csv.reader(csvfile, delimiter=",", quotechar='"')
            headers = next(file_data)
            csv_data = [dict(zip(headers, i)) for i in file_data]

        return FundingRaised.filter_csv(csv_data, options)

    def find_by(options):
        result = FundingRaised.where(options)
        return result[0]


class RecordNotFound(Exception):
    pass
