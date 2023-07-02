import unittest
from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_mileage = 0
        last_service_mileage = 0

        car = CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.now().date()
        last_service_date = today.replace(year=today.year - 1)

        car = SpindlerBattery(last_service_date, today)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        car = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0

        car = CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_mileage = 0
        last_service_mileage = 0

        car = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.now().date()
        last_service_date = today.replace(year=today.year - 1)

        car = SpindlerBattery(last_service_date, today)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        car = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0

        car = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        warning_light_on = False

        car = SternmanEngine(warning_light_on)
        self.assertFalse(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.now().date()
        last_service_date = today.replace(year=today.year - 2)

        car = SpindlerBattery(last_service_date, today)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        warning_light_on = True

        car = SternmanEngine(warning_light_on)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_on = False

        car = SternmanEngine(warning_light_on)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.now().date()
        last_service_date = today.replace(year=today.year - 5)

        car = NubbinBattery(last_service_date, today)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.now().date()
        last_service_date = today.replace(year=today.year - 3)

        car = NubbinBattery(last_service_date, today)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        car = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0

        car = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(car.needs_service())


#
class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.now().date()
        last_service_date = today.replace(year=today.year - 5)

        car = NubbinBattery(last_service_date, today)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.now().date()
        last_service_date = today.replace(year=today.year - 3)

        car = NubbinBattery(last_service_date, today)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        car = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0

        car = CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
