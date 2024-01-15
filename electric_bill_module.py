class ElectricBill:
    def __init__(self, customer_name, customer_address, units_consumed, rate_per_unit=5):
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.units_consumed = units_consumed
        self.rate_per_unit = rate_per_unit

    def calculate_bill(self):
        total_bill = self.units_consumed * self.rate_per_unit
        return total_bill
