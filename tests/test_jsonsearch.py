from jsonsearch import JsonSearch
import pytest



test_data =   {
  "_id": "609de1035f903a1e3ab340d8",
  "index": 0,
  "guid": "eb262ee3-984d-4dd6-84a4-25fe9174cbba",
  "isActive": "false",
  "balance": "$3,632.04",
  "picture": "http://placehold.it/32x32",
  "age": 26,
  "eyeColor": "green",
  "name": "Fisher Powers",
  "gender": "male",
  "company": "COMTRAIL",
  "email": "fisherpowers@comtrail.com",
  "phone": "+1 (870) 557-3875",
  "address": "363 Sumner Place, Fontanelle, Ohio, 3292",
  "about": "Sit aute ea esse non veniam enim cupidatat. Occaecat commodo voluptate elit incididunt nulla do adipisicing sint do sit. Tempor duis officia laboris ea irure enim. Ea commodo aliquip consectetur aliqua magna quis sunt irure ullamco laborum enim dolore veniam tempor. Laborum minim cillum voluptate laboris officia ex consequat id in esse cupidatat enim ullamco non. Ea nostrud qui nostrud occaecat enim voluptate.\r\n",
  "registered": "2017-02-06T08:20:18 -08:00",
  "latitude": -43.678469,
  "longitude": -112.738824,
  "build_version": {
    "model_name": "MacBook Pro",
    "build_version": {
      "processor_name": "Intel Core i7",
      "processor_speed": "2.7 GHz",
      "core_details": {
        "build_version": "4",
        "l2_cache(per_core)": "256 KB"
      }
    }
  },
  "tags": [
    "sunt",
    "magna",
    "fugiat",
    "occaecat",
    "dolor",
    "aute",
    "velit"
  ],
  "friends": [
    {
      "id": 0,
      "name": "Daugherty Carpenter"
    },
    {
      "id": 1,
      "name": "Carissa Steele"
    },
    {
      "id": 2,
      "name": "Stevens Skinner"
    }
  ],
  "greeting": "Hello, Fisher Powers! You have 9 unread messages.",
  "favoriteFruit": "apple"
}



def test_search_all_value():
    jsondata = JsonSearch(object=test_data, mode='j')
    name_value = jsondata.search_all_value(key='processor_name') 
    assert name_value == ['Intel Core i7']

def test_search_all_path():
    jsondata = JsonSearch(object=test_data, mode='j')
    name_value_path = jsondata.search_all_path(key='processor_name')   
    assert  name_value_path == [['build_version', 'build_version', 'processor_name']]

def test_search_first_value():
    jsondata = JsonSearch(object=test_data, mode='j')
    first_name_value = jsondata.search_first_value(key='processor_name')   
    assert first_name_value == 'Intel Core i7'

def test_search_first_path():
    jsondata = JsonSearch(object=test_data, mode='j')
    first_name_value_path = jsondata.search_first_path(key='processor_name')    
    assert first_name_value_path == ['build_version', 'build_version', 'processor_name']
