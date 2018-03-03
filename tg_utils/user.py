class User(object):
    def __init__(self, json=None, id=None, is_bot=None, first_name=None, last_name=None, username=None, language_code=None):
        if (id != None) and (is_bot != None):
            self.__id = id
            self.__is_bot = is_bot
            self.__first_name = first_name
            self.__last_name = last_name
            self.__username = username
            self.__language_code = language_code
        if json != None:
            self.json_init(json)
    
    def json_init(self, json=None):
        self.__id = json.pop('id', None)
        self.__is_bot = json.pop('is_bot', None)
        self.__first_name = json.pop('first_name', None)
        self.__last_name = json.pop('last_name', None)
        self.__username = json.pop('username', None)
        self.__language_code = json.pop('language_code', None)

    @property
    def id(self):
        return self.__id

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def username(self):
        return self.__username

    @property
    def language_code(self):
        return self.__language_code
