import json
import yaml


class JsonStorage:
    def __init__(self, file):
        self.file = file

    def get_item(self, key):
        with open(self.file, "r") as read_file:
            data = json.load(read_file)
            return data.get(key, None)


class YamlStorage:
    def __init__(self, file):
        self.file = file

    def get_item(self, key):
        with open(self.file) as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            return data.get(key, None)


class StorageService:
    def __init__(self, storage):
        self.storage = storage

    def get(self, key):
        return self.storage.get_item(key)


json_storage = StorageService(JsonStorage('data.json'))
print(json_storage.get('user'))

yaml_storage = StorageService(YamlStorage('data.yaml'))
print(yaml_storage.get('user'))
