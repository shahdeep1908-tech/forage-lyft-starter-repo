class Tire:
    def __init__(self, tire_wear_sensors=None):
        self.tire_wear_sensors = tire_wear_sensors

    def needs_service(self):
        raise NotImplementedError("Subclasses must implement needs_service method")
