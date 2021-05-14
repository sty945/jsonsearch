import json
from typing import Any, List


class JsonSearch():
    def __init__(self, object, mode='j'):
        """[summary]

        Args:
            object ([type]): [The object that want to search]
            mode (str, optional): [Choose the object type, 'j' means a json object, 's' means a ``str``, ``bytes`` or ``bytearray`` instance
    containing a JSON document]. Defaults to 'j'.

        Raises:
            Exception: [Unexpected mode argument.Choose "j" or "s".]
        """
        self.json_object = None
        if mode == 'j':
            self.json_object = object
        elif mode == 's':
            self.json_object = json.loads(object)
        else:
            raise Exception('Unexpected mode argument.Choose "j" or "s".')
        self.value_result_list = []
        self.key_result_list = []

    def search_all_value(self, key: str) -> List:
        """[Search a key in a json data, return a list of values]


        Args:
            key ([str]): [The key that want to seach]

        Returns:
            [list]: [The list of values that meet the key]
        """
        self.value_result_list = []
        self.__search_value(self.json_object, key)
        return self.value_result_list

    def search_first_value(self, key: str) -> Any:
        """[Search a key in a json data, return the first value]

        Args:
            key ([type]): [The key that want to seach]

        Returns:
            [type]: [The first value that meet the key]
        """
        self.value_result_list = []
        self.__search_value(self.json_object, key)
        for result in self.value_result_list:
            return result

    def search_all_path(self, key: str) -> List:
        """[Search a key in a json data, return a list of paths to get value]

        Args:
            key (str): [The key that want to seach]

        Returns:
            List: [The list of paths to get value]
        """
        all_key_path = self.__search_key(self.json_object, [], key)
        return list(all_key_path)

    def search_first_path(self, key: str) -> List:
        """[Search a key in a json data, return the first path to get value]

        Args:
            key (str): [The key that want to seach]

        Returns:
            List: [The first path to get value]
        """
        all_key_path = self.__search_key(self.json_object, [], key)
        for key_path in all_key_path:
            return key_path
        return []

    def __search_value(self, json_object, key: str):
        for k in json_object:
            if k == key:
                self.value_result_list.append(json_object[k])
            if isinstance(json_object[k], dict):
                self.__search_value(json_object[k], key)
            if isinstance(json_object[k], list):
                for item in json_object[k]:
                    if isinstance(item, dict):
                        self.__search_value(item, key)
        return

    def __search_key(self, json_object, road_step: list, target: str):
        if isinstance(json_object, dict):
            key_value_iter = (x for x in json_object.items())
        elif isinstance(json_object, list):
            key_value_iter = (x for x in enumerate(json_object))
        else:
            return
        for key, value in key_value_iter:
            current_path = road_step.copy()
            current_path.append(key)
            if key == target:
                yield current_path
            if isinstance(value, (dict, list)):
                yield from self.__search_key(value, current_path, target)
