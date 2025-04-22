import os
import json
from datetime import datetime, timedelta

BASE_PATH = os.path.join(os.getcwd(), 'json')
class FilesControl:
    @property
    def file_path(self):
        return self.__file_path
    
    def __init__(self, *, file_name:str='register.json') -> None:
        if not file_name.endswith('.json'):
            file_name += '.json'
        if not os.path.exists(BASE_PATH):
            os.makedirs(BASE_PATH)
        self.__file_path = os.path.join(BASE_PATH, file_name)
        
        if not os.path.exists(self.file_path):
            self.__save({})
    
    def __save(self, data:dict) -> bool:
        with open(self.file_path, 'w', encoding='utf-8') as _file:
            json.dump(data, _file)
        return True
            
    def __load(self) -> dict:
        with open(self.file_path, 'r', encoding='utf-8') as _file:
            data = json.load(_file)
        return data
    
    def __delete(self, file:str) -> bool:
        data = self.__load()
        try:
            del data[file]
        except KeyError:
            return False
        self.__save(data)
        return True
    
    def register(self, file:str) -> bool:
        data = self.__load()
        try:
            if file in data:
                self.__delete(file)
        except:
            pass
        data[file] = datetime.now().isoformat()
        self.__save(data)
        return True
    
    def verify_file(self, file:str, *, time:timedelta=timedelta(hours=3), deleteIfTrue:bool=True) -> bool:
        data = self.__load()
        try:
            date = datetime.fromisoformat(data[file])
            if datetime.now() - date > time:
                if deleteIfTrue:
                    self.__delete(file)
                return True
        except KeyError:
            self.register(file)
            return False
        return False
    
    def limpar(self) -> bool:
        data = self.__load()
        for key, value in data.items():
            try:
                self.verify_file(key, time=timedelta(days=5), deleteIfTrue=True)
            except KeyError:
                pass
        return True
            
    
    
if __name__ == "__main__":
    bot = FilesControl()
    print(bot.verify_file('test1', time=timedelta(seconds=5)))
    
    