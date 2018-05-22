# FYP API

> Mock API server for final year project

## Dependencies

- [Python](https://www.python.org/)
- [pip](https://pypi.org/project/pip/)

## Running

```
$ pip install -r requirements.txt
$ flask run
$ open http://localhost:5000/
```

## Endpoint

Return list of active classes under a specific lecturer

### URL
`/classes`

### Method
`GET`

### Params
- `email`: String

### Example

#### Request
http://localhost:5000/classes?email=teckminc@sunway.edu.my

#### Response
```json
{
    "email": "teckminc@sunway.edu.my",
    "semester": "2018-03-26",
    "subjects": [
        {
            "code": "NET3204",
            "classes": [
                {
                    "category": "Lecture",
                    "group": 1,
                    "students": [
                        "15011909",
                        "10023222",
                        "14099916"
                    ]
                },
                {
                    "category": "Practical",
                    "group": 1,
                    "students": [
                        "15011909",
                        "10023222"
                    ]
                },
                {
                    "category": "Practical",
                    "group": 2,
                    "students": [
                        "14099916"
                    ]
                }
            ]
        }
    ]
}
```

### Data Types
- `email`: String
- `semester`: String
- `subjects`: Array of Object
- `code`: String
- `classes`: Array of Object
- `category`: String
- `group`: Integer
- `students`: Array of String
