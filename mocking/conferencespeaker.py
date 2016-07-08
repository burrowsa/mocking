class ConferenceSpeaker(object):
    def __init__(self, name, twitterhandle):
        self.name = name
        self.twitterhandle = twitterhandle
    
    def greet(self, delegates):
        for delegate in delegates:
            delegate.speakto("Hi my name is {0.name}, follow me on twitter @{0.twitterhandle}".format(self))
