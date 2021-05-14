
# JsonSearch
[![](https://img.shields.io/badge/pypi-jsonsearch-brightgreen)](https://pypi.org/project/jsonsearch/)


JsonSearch is a simple, yet effcient python library for searhing specific elements in json data.

```
>>> from jsonsearch import JsonSearch
>>> test_data = {
...     "store": {
...         "book": [
...             {
...                 "category": "reference",
...                 "author": "Nigel Rees",
...                 "title": "Sayings of the Century",
...                 "price": 8.95
...             },
...             {
...                 "category": "fiction",
...                 "author": "Evelyn Waugh",
...                 "title": "Sword of Honour",
...                 "price": 12.99
...             },
...             {
...                 "category": "fiction",
...                 "author": "Herman Melville",
...                 "title": "Moby Dick",
...                 "isbn": "0-553-21311-3",
...                 "price": 8.99
...             },
...             {
...                 "category": "fiction",
...                 "author": "J. R. R. Tolkien",
...                 "title": "The Lord of the Rings",
...                 "isbn": "0-395-19395-8",
...                 "price": 22.99
...             }
...         ],
...         "bicycle": {
...             "color": "red",
...             "price": 19.95
...         }
...     },
...     "expensive": 10
... }
>>> jsondata = JsonSearch(object=test_data, mode='j')
>>> jsondata.search_all_value(key='title')               
['Sayings of the Century', 'Sword of Honour', 'Moby Dick', 'The Lord of the Rings']
>>> jsondata.search_all_path(key='title')       
[['store', 'book', 0, 'title'], ['store', 'book', 1, 'title'], ['store', 'book', 2, 'title'], ['store', 'book', 3, 'title']]
>>> jsondata.search_first_value(key='title')           
'Sayings of the Century'
>>> jsondata.search_first_path(key='title')      
['store', 'book', 0, 'title']
```

When json data have nested objects, JsonSearch allows you to find specific elements in json data easily.

Take the program above as an example, if you want to get the first `'title'` value in data, you don't need to use `test_data['store']['book'][0]['title']` anymore, you can just use `jsondata.search_first_value(key='title')`.


# Install 

JsonSearch is available on PyPI:

```
 pip install jsonsearch
```

or 

```
pip install --index-url https://pypi.org/simple/ jsonsearch
```








