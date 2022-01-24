import csv


class FundingRaised:
    @staticmethod
    def where(options={}):
        with open("../startup_funding.csv", "rt") as csvfile:
            data = csv.reader(csvfile, delimiter=",", quotechar='"')
            csv_data = []
            for row in data:
                csv_data.append(row)

        headers = csv_data[0]
        csv_data = csv_data[1:]

        # permalink,company_name,number_employees,category,city,state,funded_date,raised_amount,raised_currency,round
        column_order = {
            "company_name": 1,
            "city": 4,
            "state": 5,
            "round": 9,
        }

        for column_name, column_number in column_order.items():
            if column_name in options:
                result = []
                for row in csv_data:
                    if row[column_number] == options[column_name]:
                        result.append(row)
                csv_data = result

        output = []
        for row in csv_data:
            mapped = dict(zip(headers, row))
            output.append(mapped)

        return output

    @staticmethod
    def find_by(options):
        with open("../startup_funding.csv", "rt") as csvfile:
            data = csv.reader(csvfile, delimiter=",", quotechar='"')
            # skip header
            next(data)
            csv_data = []
            for row in data:
                csv_data.append(row)

        if "company_name" in options:
            for row in csv_data:
                if row[1] == options["company_name"]:
                    mapped = {}
                    mapped["permalink"] = row[0]
                    mapped["company_name"] = row[1]
                    mapped["number_employees"] = row[2]
                    mapped["category"] = row[3]
                    mapped["city"] = row[4]
                    mapped["state"] = row[5]
                    mapped["funded_date"] = row[6]
                    mapped["raised_amount"] = row[7]
                    mapped["raised_currency"] = row[8]
                    mapped["round"] = row[9]
                    return mapped

        if "city" in options:
            for row in csv_data:
                if row[4] == options["city"]:
                    mapped = {}
                    mapped["permalink"] = row[0]
                    mapped["company_name"] = row[1]
                    mapped["number_employees"] = row[2]
                    mapped["category"] = row[3]
                    mapped["city"] = row[4]
                    mapped["state"] = row[5]
                    mapped["funded_date"] = row[6]
                    mapped["raised_amount"] = row[7]
                    mapped["raised_currency"] = row[8]
                    mapped["round"] = row[9]
                    return mapped

        if "state" in options:
            for row in csv_data:
                if row[5] == options["state"]:
                    mapped = {}
                    mapped["permalink"] = row[0]
                    mapped["company_name"] = row[1]
                    mapped["number_employees"] = row[2]
                    mapped["category"] = row[3]
                    mapped["city"] = row[4]
                    mapped["state"] = row[5]
                    mapped["funded_date"] = row[6]
                    mapped["raised_amount"] = row[7]
                    mapped["raised_currency"] = row[8]
                    mapped["round"] = row[9]
                    return mapped

        if "round" in options:
            for row in csv_data:
                if row[9] == options["round"]:
                    mapped = {}
                    mapped["permalink"] = row[0]
                    mapped["company_name"] = row[1]
                    mapped["number_employees"] = row[2]
                    mapped["category"] = row[3]
                    mapped["city"] = row[4]
                    mapped["state"] = row[5]
                    mapped["funded_date"] = row[6]
                    mapped["raised_amount"] = row[7]
                    mapped["raised_currency"] = row[8]
                    mapped["round"] = row[9]
                    return mapped

        raise RecordNotFound


class RecordNotFound(Exception):
    pass
