import json

class File_Handler:
    def __init__(self,file_name):
        self.file_name = file_name

    def create_new_file(self):
        with open(self.file_name, 'w') as f:
            pass

    def append_json_data(self, json_data):
        with open(self.file_name, 'a') as f:
            json.dump(json_data, f)
            f.write('\n')

    def read_json_array(self):
        with open(self.file_name, 'r') as f:
            json_lines = f.readlines()

        json_array = []
        for line in json_lines:
            json_data = json.loads(line)
            json_array.append(json_data)

        return json_array
