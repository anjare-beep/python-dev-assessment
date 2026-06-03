import requests

def fetch_and_display_users(num_users, url='https://jsonplaceholder.typicode.com/users'):
    #url = f'https://jsonplaceholder.typicode.com/users' 

    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            return None
        
        users = response.json()
        for user in users[:num_users]:
            name = user["name"]
            email = user["email"]
            city = user["address"]["city"]
            print(f"Name: {name}, Email: {email}, City: {city}")
            

    
    
    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")
        return None
    except KeyError as e:
        print(f"Error: Missing expected key {e} in the JSON response data.")
        return None   
    
fetch_and_display_users(3)
fetch_and_display_users(3, 'https://jsonplaceholder.typicode.com/users/invalid')  # This will cause a TypeError due to incorrect argument
fetch_and_display_users(3, "https://this-url-does-not-exist.com/users")  
fetch_and_display_users(5)