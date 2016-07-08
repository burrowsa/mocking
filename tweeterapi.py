class Tweeter(object):
    def __init__(self, username, password):
        """Tweeter constructor
    
        Args:
            username (str): The username to use when connecting.
            password (str): The password to use when connecting.
        """
        self.username = username
        self.password = password
    
    def tweet(self, msg):
        """Sends a tweet
    
        Args:
            msg (str): The message to be tweeted.
    
        Returns:
            bool: The return value. True for success, False otherwise.
        """
        ...
        return True
