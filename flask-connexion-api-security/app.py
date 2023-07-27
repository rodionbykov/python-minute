from pathlib import Path

import connexion

PASSWD = {"admin":"secret"}

# define those functions before initializing app
def check_basic_auth(username, passwd):
    if PASSWD.get(username) == passwd:
        # use JWT registered claim 'sub'
        return {"sub": username}
    return None

# on successful authorization, Flask will call this function with named argument 'user'
def get_basic_secret_info(user) -> str:
    return f"You are '{user}' accessing information protected by basic authentication"

app = connexion.FlaskApp(__name__)
app.add_api("openapi.yaml")

if __name__ == "__main__":
    app.run()
