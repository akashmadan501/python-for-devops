# Virtual Environment
Virtual Envirnment is an isolated workspace for specific Python projects.

- It allows us to -
    - Install project-specific libraries without affecting other projects.
    - Avoid version conflicts between dependencies.
    - Reduce unneccesary golbal packages usage.


### How to create Virtual Environment

- cmd 
```
python3.14 -m venv env_for_project1
```

- To activate environment
```
source env_for_project1/bin/activate
```

- To deactivate 
```
deactivate
```

# DATA STRUCTURE
A data structure is a way of organizing and storing data so it can be used efficiently.

## Lists
List is an ordered(have index), mutable collection that can store multiple values in a single variable. Allows duplicate values. Can store different data types together int, float, str, bool.
```
a = [100, 0.63, True, 'aws']
```

- Accessing element
```
print(a[2])
```

- Adding element
```
a.appent("devops")
```

##### Iteratin a list 
```
for i in a:
    print(i)
```

## Dictionary
A dictionay is a mutable data structure in Python that stores data as key-value pairs for fast and efficient lookup.Keys must be unique.
```
student = {
    "name" : "akash",
    "age" : 19,
    "course" : "devops"
}
```

- Accessing value
```
print(student["name"])
```

- Removing items
```
student.pop("course")
```

##### Iterating a dict
```
for key,value in student.itmes():
    print(key,value)
```

## Set
A set is an unordered collection of unique elements. It automatically removes duplicates.
```
nums = {1, 2, 3, 3, 4}
```

- Adding element
```
nums.add(5)
```
- Check membership
```
print(3 in nums)   # True
```

## Tuples
A tuple is an ordered, immutable collection of elements. Immutable means once created, it cannot be changed. It allows duplicates.  
```
data = (10, 20, 30)
```

##### Python has four main built-in data structures:
-List: ordered and mutable
-Tuple: ordered and immutable
-Set: unordered and unique
-Dictionary: key-value pairs with fast lookup

### Comparison of Python Data Structures

| Feature               | List `[]`            | Tuple `()`           | Set `{}`              | Dictionary `{key: value}`      |
|-----------------------|----------------------|----------------------|-----------------------|--------------------------------|
| Ordered               | ✅ Yes               | ✅ Yes               | ❌ No                 | ✅ Yes (Python 3.7+)           |
| Mutable               | ✅ Yes               | ❌ No                | ✅ Yes                | ✅ Yes                         |
| Allows Duplicates     | ✅ Yes               | ✅ Yes               | ❌ No                 | ❌ Keys No (Values Yes)        |
| Indexed Access        | ✅ Yes               | ✅ Yes               | ❌ No                 | ❌ No (Access by key)          |
| Stores Key-Value?     | ❌ No                | ❌ No                | ❌ No                 | ✅ Yes                         |
| Syntax                | `[1,2]`              | `(1,2)`              | `{1,2}`               | `{"a":1}`                      |
| Use Case              | General collection   | Fixed data           | Unique items          | Structured data                |



## API - Application Programming Interface
An API is a set of rules that allows one application to interact with another application through requests and response.
```
Internet
   ↓
HTTP (communication protocol)
   ↓
Web API (uses HTTP)
   ↓
REST API (follows REST rules)
```
#### REST API
A REST API is a type of Web API that follows a set of architectural rules called REST(Representational State Transfer)

- RULES
    - Client Server Separation
        - client send req, display res  && Server process req and send res.

    - Stateless
        -   Server does not remember previous requests. Each req carries token/session info. This makes it Scalable.

    - Use HTTP Methods properly
    

        | Method  | Purpose              | Example Endpoint     | What It Does                          |
        |----------|----------------------|----------------------|----------------------------------------|
        | GET      | Fetch data           | `GET /users`         | Get list of all users                 |
        | GET      | Fetch single item    | `GET /users/1`       | Get details of user with ID 1         |
        | POST     | Create new data      | `POST /users`        | Create a new user                     |
        | PUT      | Replace full data    | `PUT /users/1`       | Replace all details of user ID 1      |
        | PATCH    | Update partial data  | `PATCH /users/1`     | Update specific fields of user ID 1   |
        | DELETE   | Remove data          | `DELETE /users/1`    | Delete user with ID 1                 |

    - Use Standard HTTP Status Codes

        - REST APIs must return proper HTTP status codes to indicate the result of a request.

        | Code | Meaning        | When It Is Used Example                          |
        |------|---------------|--------------------------------------------------|
        | 200  | OK            | `GET /users/1` successful                        |
        | 201  | Created       | `POST /users` new user created                   |
        | 400  | Bad Request   | Invalid JSON or missing required fields          |
        | 401  | Unauthorized  | No token or invalid authentication token         |
        | 403  | Forbidden     | Logged in but not allowed to access resource     |
        | 404  | Not Found     | `GET /users/99` user does not exist              |
        | 500  | Server Error  | Something broke on server side                   |

        *** 2xx → Success ***, 
        *** 4xx → Client mistake ***, 
        *** 5xx → Server mistake *** 


    - Data Representation usually in JSON
        - JavaScript Object Notation - key value pair - type(dict)

```
import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url=url)

print(response)
print(response.json())
```




