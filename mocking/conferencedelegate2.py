import re
from simpletweeter import tweet


TWITTER_REGEX = re.compile(".*follow me on twitter @(\w+)")


class ConferenceDelegate(object):
    def __init__(self, credentialsfile):
        self.credentialsfile = credentialsfile
        
    def speakto(self, message):
        matched = TWITTER_REGEX.match(message)
        if matched:
            tweet("Amazing talk from @" + matched.groups()[0],
                  self.credentialsfile)
