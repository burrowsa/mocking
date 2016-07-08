from mocking.conferencedelegate2 import ConferenceDelegate
from unittest.mock import sentinel, patch


def test_delegate_tweets_if_message_contains_twitter_handle():
    sut = ConferenceDelegate(sentinel.credentialsfile)
    
    with patch("mocking.conferencedelegate2.tweet") as mock_tweet:
        sut.speakto("Hi, why not follow me on twitter @manahltech")
    
    mock_tweet.assert_called_once_with("Amazing talk from @manahltech", sentinel.credentialsfile)


def test_delegate_does_not_tweet_if_message_contains_no_twitter_handle():
    sut = ConferenceDelegate(sentinel.credentialsfile)
    
    with patch("mocking.conferencedelegate2.tweet") as mock_tweet:
        sut.speakto("Nice hat")
    
    assert not mock_tweet.called
