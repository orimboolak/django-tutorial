import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTY1NzgwMTQwLCJqdGkiOiIwZmMxOTE5NjU4MzI0MDgzYTAwNTRhODI0ZGRjMjI1MSIsInVzZXJfaWQiOjF9.zgbkuD_8yDZ1QZsm8nr8---J8fWkHlrqWzTIfKoFr38'

request = requests.get("http://127.0.0.1:8000/paradigms", headers)

print(request)