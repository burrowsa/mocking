import tweeterapi
from os.path import expanduser


CREDENTIALS_FILE = expanduser("~/twittercredentials.cfg")


def _read_credentials(credentials_file):
    with open(credentials_file) as f:
        username, password = f.read().splitlines()[:2]
    return username, password


def tweet(msg, credentials_file=CREDENTIALS_FILE):
    """Sends a tweet using the login credentials supplied in a file and 
    retries up to 5 times in the even of a failure.

    Args:
        msg (str): The message to be tweeted.
        credentials_file (str): The path of the file containing the login credentials to use.
    """
    username, password = _read_credentials(credentials_file)

    t = tweeterapi.Tweeter(username, password)
    
    for _ in range(5):
        if t.tweet(msg):
            break
    else:
        raise RuntimeError("Unable to tweet")
