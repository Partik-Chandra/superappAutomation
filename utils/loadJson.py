import json
class laodjson:
    
    def __init__(self, file_path):
        self.file_path =file_path

    def load_users(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)