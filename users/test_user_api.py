# python3 manage.py shell < users/test_user_api.py;            
# to run the test file use above command on terminal
from django.test import Client

client = Client()

# Step 1: Register
response_register = client.post('/api/register/', {
    'username': 'gautam3',  # 👈 Use a unique name
    'email': 'gautam3@example.com',
    'password': 'gautam12345'
}, content_type='application/json')
print("Register:", response_register.status_code, response_register.json())

#Login
response_login = client.post('/api/token/', {
    'username': 'gautam3',
    'password': 'gautam12345'
}, content_type='application/json')
print("Login:", response_login.status_code, response_login.json())

# Extract tokens
tokens = response_login.json()
access = tokens.get("access")
refresh = tokens.get("refresh")

#Access Protected API test
response_protected = client.get('/api/protected/', HTTP_AUTHORIZATION=f'Bearer {access}')
print("Protected Access:", response_protected.status_code, response_protected.json())

#Logout test
response_logout = client.post('/api/logout/', {
    "refresh": refresh
}, content_type='application/json', HTTP_AUTHORIZATION=f'Bearer {access}')
print("Logout:", response_logout.status_code, response_logout.json())
