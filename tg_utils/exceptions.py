class APIExceptions(Exception):
    def __init__(self, json):
        self.error_code = json.pop('error_code', None)
        self.description = json.pop('description', None)
