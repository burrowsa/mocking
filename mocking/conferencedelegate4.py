from simpletweeter import tweet

class ConferenceDelegate(object):
    ...
    
    def smalltalk(self, delegate):
        if delegate.speakto("Hello.") in ("hello", "hi"):
            if delegate.speakto("Good conference?") in ("yes", "yup", "not bad", "yeah"):
                best_bit = delegate.speakto("What has been your favourite part?")
                delegate.speakto("Really, I didn't go to that.")
                delegate.speakto("Nice chatting with you, gotta go.")
                
                tweet("Absolutely loved " + best_bit)
