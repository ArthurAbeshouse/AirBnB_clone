# AirBnB_clone

## Description
This is the first step towards building our first web application: an AirBnB clone. This part of the project is the backend of the AirBnB. Our task was to create a custom command-line interface for data management.

## Installation
```
git clone https://github.com/ArthurAbeshouse/AirBnB_clone.git
cd AirBnB_clone
```

## Usage
The console works both in interactive mode and non-interactive mode, it functions similarly to a Unix shell.

``` 	    	       	  	      	       
Run the console -------------------------------- ./console.py
Quit the console ------------------------------- (hbnb) quit
Display help for a command --------------------- (hbnb) help <command>
Create an object (and print its id) ------------ (hbnb) create <class>
Show an object --------------------------------- (hbnb) show <class> <id>/(hbnb) <class>.show(<id>)
Destroy an object ------------------------------ (hbnb) destroy <class> <id>/(hbnb) <class>.destroy(<id>)
Show all objects/all instances of a class ------ (hbnb) all/(hbnb) all <class>
Update attribute(s) of an object --------------- (hbnb) update <class> <id> <attribute name> "<attribute value>"/(hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")
```
An example of Non-interactive mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
```

## Models
All the classes used in this project are contained in the [models](./models/)  folder.

File | Description | Attributes
---- |-------------|-----------
[base_model.py](./models/base_model.py) | Defines all common attributes\methods for other classes | id, created_at, updated_at
[user.py](./models/user.py) | Holds information about future users | first_name, last_name, email, password
[amenity.py](./models/amenity.py) | Holds information about future amenities | name
[city.py](./models/city.py) | Holds information about future locations | state_id, name
[state.py](./models/state.py) | Holds information about what state the future BnB is located | name
[place.py](./models/place.py) | Holds information about future accommodations | city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids
[review.py](./models/review.py) | Holds information about future user/host reviews | place_id, user_id, text 

## File storage
[FileStorage](./models/engine/file_storage.py) serializes instances into a JSON file and deserializes a JSON file into instances.

The [__init__.py](./models/__init__.py) file holds the instantiation of the FileStorage class called storage, along with a call to the method reload() on that instance. This allows the storage to be reloaded automatically during initialization, which recovers serialized data.

## Tests
All unittest modules can be found in the [test_models](./tests/test_models/) folder.

## Authors
* **Arthur Abeshouse** - [artieabe99@gmail.com](https://github.com/ArthurAbeshouse)
*  **Anthony Huggins** - [huggins9000211@gmail.com](https://github.com/huggins9000211)