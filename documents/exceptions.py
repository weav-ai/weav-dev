class DocumentProcessingException(Exception):
    def __init__(self, status_code, message, response_data=None):
        self.status_code = status_code
        self.message = message
        self.response_data = response_data
        super().__init__(f"Error {status_code}: {message}")
        super().__init__(f"{response_data}")
