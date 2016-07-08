from mocking.conferencedelegate4 import ConferenceDelegate
from unittest.mock import Mock, patch
from mockextras import when


def test_unsuccessful_conversation():
    stranger = Mock(name="stranger")
    when(stranger.speakto).called_with("Hello.").then("go away")
    
    delegate = ConferenceDelegate()
    with patch("mocking.conferencedelegate4.tweet") as mock_tweet:
        delegate.smalltalk(stranger)
        
    assert stranger.speakto.called_once_with("hello")
    assert not mock_tweet.called    


def test_successful_conversation():
    stranger = Mock(name="stranger")
    when(stranger.speakto).called_with("Hello.").then("hi")
    when(stranger.speakto).called_with("Good conference?").then("not bad")
    when(stranger.speakto).called_with("What has been your favourite part?").then("a brilliant talk on mocks")
    when(stranger.speakto).called_with("Really, I didn't go to that.").then("shame, it was amazing")
    when(stranger.speakto).called_with("Nice chatting with you, gotta go.").then("laters")
    
    delegate = ConferenceDelegate()
    with patch("mocking.conferencedelegate4.tweet") as mock_tweet:
        delegate.smalltalk(stranger)
        
    mock_tweet.assert_called_once_with("Absolutely loved a brilliant talk on mocks")  


def test_successful_conversation_using_side_effect():
    stranger = Mock(name="stranger")

    def stranger_speakto(msg):
        if msg == "Hello.":
            return "hi"
        elif msg == "Good conference?":
            return "not bad"
        elif msg == "What has been your favourite part?":
            return "a brilliant talk on mocks"
        elif msg == "Really, I didn't go to that.":
            return "shame, it was amazing"
        elif msg == "Nice chatting with you, gotta go.":
            return "laters"
    
    stranger.speakto.side_effect = stranger_speakto
    
    delegate = ConferenceDelegate()
    with patch("mocking.conferencedelegate4.tweet") as mock_tweet:
        delegate.smalltalk(stranger)
        
    mock_tweet.assert_called_once_with("Absolutely loved a brilliant talk on mocks")  
