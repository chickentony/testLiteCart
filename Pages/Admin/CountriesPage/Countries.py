class Countries:

    def __init__(self, driver) -> None:
        self.driver = driver
        self.URL: str = 'http://localhost/LiteCart/admin/?app=countries&doc=countries'
