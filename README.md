# League of Legends Login

This is a Python script for automating the login process for League of Legends. It allows users to select an account from a list and automatically log in to the League of Legends client.

## Requirements

- Python 3.x
- Required Python libraries (install using `pip install [library_name]`):
- keyboard==0.13.5
- PyAutoGUI==0.9.53
- PyGetWindow==0.0.9


## Usage

1. Clone or download this repository to your local machine.

2. Install the required Python libraries by running:
pip install -r requirements.txt

3. Add your League of Legends accounts to the `Accounts.json` file in the following format:
```json
{
  "accounts": {
    "username1": {
      "username": "your_username",
      "password": "your_password"
    },
    "username2": {
      "username": "your_username",
      "password": "your_password"
    },
  }
}
```
Run the main.py script
