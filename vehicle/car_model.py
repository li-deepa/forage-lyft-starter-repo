from datetime import datetime

from car_engine import WilloughbyEngine,CapuletEngine,SternmanEngine

from car_battery import Nubbin ,Spindler


class Calliope(CapuletEngine,Nubbin):
    def engine_needs_service(self):
       
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.capulet_engine_should_be_serviced():
            return True
        else:
            return False
    def battery_needs_service(self):     
        service_threshold_date_battery = self.last_service_date.replace(year=self.last_service_date.year + 3)
        if service_threshold_date_battery < datetime.today().date() or self.nubbin_battery_should_be_serviced():
            return True
        else:
            return False
        

class Glissade(WilloughbyEngine,Spindler):
    def engine_needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.willoughby_engine_should_be_serviced():
            return True
        else:
            return False
    
    def battery_needs_service(self):     
        service_threshold_date_battery = self.last_service_date.replace(year=self.last_service_date.year + 1)
        if service_threshold_date_battery < datetime.today().date() or self.spindler_battery_should_be_serviced():
            return True
        else:
            return False

class Palindrome(SternmanEngine,Spindler):
    def engine_needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.sternman_engine_should_be_serviced():
            return True
        else:
            return False
    
    def battery_needs_service(self):     
        service_threshold_date_battery = self.last_service_date.replace(year=self.last_service_date.year + 1)
        if service_threshold_date_battery < datetime.today().date() or self.spindler_battery_should_be_serviced():
            return True
        else:
            return False

class Rorschach(WilloughbyEngine,Nubbin):
    def engine_needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.willoughby_engine_should_be_serviced():
            return True
        else:
            return False
    
    def battery_needs_service(self):     
        service_threshold_date_battery = self.last_service_date.replace(year=self.last_service_date.year + 3)
        if service_threshold_date_battery < datetime.today().date() or self.nubbin_battery_should_be_serviced():
            return True
        else:
            return False

class Thovex(CapuletEngine,Nubbin):
    def engine_needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.capulet_engine_should_be_serviced():
            return True
        else:
            return False

    def battery_needs_service(self):     
        service_threshold_date_battery = self.last_service_date.replace(year=self.last_service_date.year + 3)
        if service_threshold_date_battery < datetime.today().date() or self.nubbin_battery_should_be_serviced():
            return True
        else:
            return False

