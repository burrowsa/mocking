from simpletweeter import tweet, _read_credentials
from unittest.mock import mock_open, patch, sentinel, call
import pytest


@patch('tweeterapi.Tweeter')
@patch('simpletweeter._read_credentials', return_value=(sentinel.username, sentinel.password))
def test_tweet(mock_read_credentials, mock_tweeter):
        tweet(sentinel.message, sentinel.credentials_file)
        
        mock_read_credentials.assert_called_once_with(sentinel.credentials_file)
        
        mock_tweeter.mock_calls = [call(sentinel.username, sentinel.password),
                                   call.tweet(sentinel.message)]
    

@patch('tweeterapi.Tweeter')
@patch('simpletweeter._read_credentials', return_value=(sentinel.username, sentinel.password))
def test_tweet_raises_exception_on_failure(_, mock_tweeter):
    mock_tweeter.return_value.tweet.return_value = False
    
    with pytest.raises(RuntimeError) as err:
        tweet(sentinel.message, sentinel.credentials_file)
        
    assert str(err.value) == "Unable to tweet"


@patch('tweeterapi.Tweeter', **{'return_value.tweet.return_value': False})
@patch('simpletweeter._read_credentials', return_value=(sentinel.username, sentinel.password))
def test_tweet_raises_exception_on_failure2(_, mock_tweeter):
    with pytest.raises(RuntimeError) as err:
        tweet(sentinel.message, sentinel.credentials_file)
        
    assert str(err.value) == "Unable to tweet"


@patch('tweeterapi.Tweeter')
@patch('simpletweeter._read_credentials', return_value=(sentinel.username, sentinel.password))
def test_tweet_retries_on_failure(_, mock_tweeter):
    mock_tweeter.return_value.tweet.side_effect =[False, False, True]
    
    tweet(sentinel.message, sentinel.credentials_file)
    
    mock_tweeter.mock_calls = [call(sentinel.username, sentinel.password),
                               call.tweet(sentinel.message),
                               call.tweet(sentinel.message),
                               call.tweet(sentinel.message)]


@patch('tweeterapi.Tweeter', **{'return_value.tweet.side_effect': [False, False, True]})
@patch('simpletweeter._read_credentials', return_value=(sentinel.username, sentinel.password))
def test_tweet_retries_on_failure2(_, mock_tweeter):
    tweet(sentinel.message, sentinel.credentials_file)
    
    mock_tweeter.mock_calls = [call(sentinel.username, sentinel.password),
                               call.tweet(sentinel.message),
                               call.tweet(sentinel.message),
                               call.tweet(sentinel.message)]
        

def test_read_credentials():
    with patch('simpletweeter.open', mock_open(read_data='andyburrows\nsup3rs3cr3t'), create=True) as mock_opn:
            username, password = _read_credentials(sentinel.credentials_file)
            
            mock_opn.assert_called_once_with(sentinel.credentials_file)
            
            assert username == "andyburrows"
            assert password == "sup3rs3cr3t"
