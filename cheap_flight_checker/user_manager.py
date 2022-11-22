import requests

HEADER = {"Authorization": f"Bearer sdkfhskdhfksadkfsdkfhkj"}
PUT_URL = "https://api.sheety.co/357df803cdf8a30e2c5b639060f7bf96/flightDeals/users/"
GET_URL = "https://api.sheety.co/357df803cdf8a30e2c5b639060f7bf96/flightDeals/users"


class UserManager:
    def __init__(self):
        self.first_name = input("Welcome to FLIGHT CLUB.\n\nWhat is your first name?\n")
        self.last_name = input("What is your last name?\n")
        self.email = input("Type your email.\n")
        self.email_confirmation = input("Type your email again.\n")
        self.user_info = {"first_name": self.first_name,
                          "last_name": self.last_name,
                          "email": self.email,
                          "email_confirmation": self.email_confirmation}

    def check_user(self):
        response = requests.get(url=GET_URL, headers=HEADER)
        user_data = response.json()
        for user in user_data["users"]:
            last_user_id = int(user["id"])
            if user["email"] == self.user_info["email"]:
                print("You are User of these app already.")
            else:
                self.add_user(self.user_info, last_user_id)

    def add_user(self, user_info, last_user_id):
        last_user_id += 1
        new_user_id = str(last_user_id)
        parameters = {"user": {"firstName": user_info["first_name"].title(),
                               "lastName": user_info["last_name"].title(),
                               "email": user_info["email_confirmation"]}}
        print(parameters)
        if self.user_info["email"] == self.user_info["email_confirmation"]:
            response = requests.put(url=f"{PUT_URL}{new_user_id}", json=parameters)
            response.raise_for_status()
            print("Success your email has been added.")

        else:
            print("We are sorry but emails are not match.")



