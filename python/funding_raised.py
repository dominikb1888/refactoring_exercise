class FundingRaised:
    def filter_csv(csv_data, options):
        if options:
            key = list(options.keys())[0]
            fltrd = [row for row in csv_data if row[key] == options[key]]
            del options[key]

        return FundingRaised.filter_csv(fltrd, options) if options else fltrd

    def where(options={}):
        with open("../startup_funding.csv", "rt") as csvfile:
            lines = [line.rstrip() for line in csvfile]
            csv_data = []
            header = lines[0].split(",")
            for line in lines[1:]:
                words = line.split(",")
                csv_data.append(dict(zip(header, words)))

        return FundingRaised.filter_csv(csv_data, options)

    def find_by(options):
        result = FundingRaised.where(options)
        return result[0]


class RecordNotFound(Exception):
    pass
