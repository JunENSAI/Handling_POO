class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_str):
        d, m, y = map(int, date_str.split("-"))
        return cls(d, m, y) 

    @staticmethod
    def is_valid_date(date_str):
        return "-" in date_str and len(date_str) == 10

date_eg = "19-12-2025"


if Date.is_valid_date(date_eg):
    my_date = Date.from_string(date_eg)
    print(f"Year: {my_date.year}")