from mocking.conferencedelegate3 import ConferenceDelegate
from unittest.mock import MagicMock
import pytest


def test_delegate_can_rate_a_talk():
    number_of_kitten_pics = MagicMock(name="number_of_kitten_pics")
    usefulness_of_content = MagicMock(name="usefulness_of_content")
    clarity_of_presentation = MagicMock(name="clarity_of_presentation")
    
    delegate = ConferenceDelegate()
    
    result = delegate.rate_talk(number_of_kitten_pics, usefulness_of_content, clarity_of_presentation)
    
    assert result is number_of_kitten_pics.__mul__.return_value
    assert number_of_kitten_pics.mock_calls == [('__mul__', (usefulness_of_content.__add__.return_value,))]
    assert usefulness_of_content.mock_calls == [('__add__', (clarity_of_presentation,))]


@pytest.mark.parametrize("number_of_kitten_pics,"
                         "usefulness_of_content,"
                         "clarity_of_presentation,"
                         "expected_rating",
                         [(1, 1, 1, 2), # ticks all the boxes
                          (0, 1, 1, 0), # no cats no points
                          (1, 0, 1, 1), # lacking content
                          (1, 1, 0, 1), # lacking clarity
                          (10, 0, 1, 10), # loadz of cats
                          (10, 1, 0, 10), # loadz of cats
                          (1, 10, 1, 11), # great content
                          (1, 1, 10, 11), # great delivery
                          ])
def test_delegate_can_rate_a_talk_no_mocks(number_of_kitten_pics, usefulness_of_content, clarity_of_presentation, expected_rating):
    delegate = ConferenceDelegate()
    assert expected_rating == delegate.rate_talk(number_of_kitten_pics, usefulness_of_content, clarity_of_presentation)
