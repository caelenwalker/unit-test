import unittest
import datetime

class TestProject(unittest.TestCase):
    def test_symbol(self):
        symbol = input("Enter a symbol to test: ")
        self.assertTrue(symbol.isupper())
        self.assertTrue(symbol.isalpha())

    def test_chart_type(self):
        chart_type = int(input("Enter either 1 or 2: "))
        self.assertTrue(chart_type.isnum())
        self.assertTrue(int(chart_type) == 1 or int(chart_type) == 2)

    def test_time_series(self):
        time_series = input("Enter a number 1-4: ")
        self.assertTrue(int(time_series), range(1, 5))
        
    def test_start_date(self):
        start_date = input("Enter a start date in the YYYY-MM-DD format: ")
        year = start_date.split("-")[0]
        month = start_date.split("-")[1]
        day = start_date.split("-")[2]
        self.assertTrue(len(year) == 4)
        self.assertTrue(len(month) == 2)
        self.assertTrue(int(month) <= 12 and int(month) > 0)
        self.assertTrue(len(day) == 2)
        self.assertTrue(int(day) <= 31 and int(day) > 0)
        
    def test_end_date(self):
        end_date = input("Enter an end date in the YYYY-MM-DD format: ")
        year = end_date.split("-")[0]
        month = end_date.split("-")[1]
        day = end_date.split("-")[2]
        self.assertTrue(len(year) == 4)
        self.assertTrue(len(month) == 2)
        self.assertTrue(int(month) <= 12 and int(month) > 0)
        self.assertTrue(len(day) == 2)
        self.assertTrue(int(day) <= 31 and int(day) > 0)

if __name__ == '__main__':
    unittest.main()
