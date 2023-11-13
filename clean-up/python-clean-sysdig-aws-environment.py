import requests

# Replace these URLs with the actual API endpoints
get_users_url = "https://us2.app.sysdig.com/api/users"
delete_user_url = "https://us2.app.sysdig.com/api/user/"

# Replace 'your_bearer_token' with your actual bearer token
bearer_token = "<SYSDIG-API-TOKEN>"

# Define the headers with the bearer token
headers = {
    "Authorization": f"Bearer {bearer_token}"
}

# Make a GET request to retrieve the list of users with the bearer token
response = requests.get(get_users_url, headers=headers)

if response.status_code == 200:
    users = response.json().get("users", [])
    for user in users:
        if isinstance(user, dict):
            team_roles = user.get("teamRoles", [])
            admin_role = False
            for role in team_roles:
                if role.get("teamName") == "workshop-student":
                    if role.get("admin"):
                        admin_role = True
                    user_id = user.get("id")
            if not admin_role:
                # Make a DELETE request to delete the user with the bearer token
                delete_response = requests.delete(f"{delete_user_url}{user_id}", headers=headers)
                if delete_response.status_code == 204 or delete_response.status_code == 200:
                    print(f"User with ID {user_id} has been deleted.")
                else:
                    print(f"Failed to delete user with ID {user_id}. Status Code: {delete_response.status_code}")
else:
    print(f"Failed to retrieve the list of users. Status Code: {response.status_code}")

