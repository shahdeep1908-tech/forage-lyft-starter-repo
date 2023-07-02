class Battery:
    def __init__(self, last_service_date=None, current_date=None):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        raise NotImplementedError("Subclasses must implement needs_service method")
