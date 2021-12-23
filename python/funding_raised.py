import pandas as pd


class FundingRaised:

    def where(options={}):
        # df = self.data
        df = pd.read_csv("../startup_funding.csv")
        for key, value in options.items():
            if key in df.columns.tolist():
                result = df[df[key] == value]

        return result.to_dict(orient="records")

    def find_by(options):
        return FundingRaised.where(options)[0]


class RecordNotFound(Exception):
    pass
