import re
import simpletweeter


TWITTER_REGEX = re.compile(".*follow me on twitter @(\w+)")


class ConferenceDelegate(object):
    def __init__(self, credentialsfile):
        self.credentialsfile = credentialsfile
        
    def speakto(self, message):
        matched = TWITTER_REGEX.match(message)
        if matched:
            simpletweeter.tweet("Amazing talk from @" + matched.groups()[0],
                                self.credentialsfile)
