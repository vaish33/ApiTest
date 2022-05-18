import requests

def test_get_employee_details_check_status_code_equals_200():
     response = requests.get("https://reqres.in/api/users?page=2")
     assert response.status_code == 200