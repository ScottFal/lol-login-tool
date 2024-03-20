import json

accountFile = "Accounts.json"


class Account:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password


def getAllAccounts():
    try:
        with open(accountFile, 'r') as f:
            data = json.load(f)
            accountsData = data.get("accounts", {})
            summoners = []
            for name, info in accountsData.items():
                username = info.get("username", "")
                password = info.get("password", "")
                summoners.append(Account(name, username, password))
            return summoners
    except FileNotFoundError:
        print(f"File '{accountFile}' not found.")
        return []
    except Exception as e:
        print("An error occurred:", e)
        return []
