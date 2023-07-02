class Engine:
    def __init__(self, last_service_mileage=None, current_mileage=None):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self):
        raise NotImplementedError("Subclasses must implement needs_service method")
