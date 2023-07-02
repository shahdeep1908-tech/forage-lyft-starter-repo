from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, tire_wear_sensors: list):
        super().__init__(tire_wear_sensors)

    def needs_service(self):
        return sum(self.tire_wear_sensors) >= 0.9
