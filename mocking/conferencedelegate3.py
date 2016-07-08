class ConferenceDelegate(object):
    ...

    def rate_talk(self,
                  number_of_kitten_pics,
                  usefulness_of_content,
                  clarity_of_presentation
                  ):
        return number_of_kitten_pics * (usefulness_of_content + clarity_of_presentation)
