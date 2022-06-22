from datetime import datetime

from car import Car

class Spindler(Car):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.last_service_date = last_service_date
        self.current_date = current_date

    def spindler_battery_should_be_serviced(self):
        return self.last_service_date - self.current_date > 2


class Nubbin(Car):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.last_service_date = last_service_date
        self.current_date = current_date

    def nubbin_battery_should_be_serviced(self):
        return self.last_service_date - self.current_date > 4