from status_checker.handle_error import check_status_code
from status_checker.handle_error import HttpStatusError
import requests

response = requests.get("google.com")

def verify_status(resp):
    try:
        check_status_code(resp.status_code , 200)
        return True
    except HttpStatusError as e:
        print(e)
        return False

if verify_status(response):
    print(response)
