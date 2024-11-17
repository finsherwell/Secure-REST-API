# Encapsulates logic for processing incoming requests
# Extracts headers, query parameters, body and method
import json

class Request:
    def __init__(self):
        test_string = '{"Name": "Suezen", "age": 23, "Course": "DSA"}'
        test_string2 = json.loads(test_string)
        print(test_string2['Name'])