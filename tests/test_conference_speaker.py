from mocking import ConferenceSpeaker, ConferenceDelegate
from unittest.mock import Mock, call


def test_speaker_can_handle_an_empty_room():
    sut = ConferenceSpeaker("Andy Burrows", "andrewburrows")
    sut.greet([])


def test_speaker_greets_sole_delegate_no_mocks():
    sut = ConferenceSpeaker("Andy Burrows", "andrewburrows")

    class FakeDelegate(object):
        def __init__(self):
            self.calls = []
        def speakto(self, msg):
            self.calls.append(("speakto", msg)) 
    
    delegate = FakeDelegate()
    
    sut.greet([delegate])
    
    assert delegate.calls == [("speakto", "Hi my name is Andy Burrows, follow me on twitter @andrewburrows")]


def test_speaker_greets_sole_delegate():  
    # Arrange
    sut = ConferenceSpeaker("Andy Burrows", "andrewburrows")
    delegate = Mock()
    
    # Act
    sut.greet([delegate])
    
    # Assert
    delegate.speakto.assert_called_once_with("Hi my name is Andy Burrows, follow me on twitter @andrewburrows")


def test_speaker_greets_sole_delegate_v2():  
    # Arrange
    sut = ConferenceSpeaker("Andy Burrows", "andrewburrows")
    delegate = Mock()
    
    # Act
    sut.greet([delegate])
    
    # Assert
    delegate.mock_calls = [call.speakto("Hi my name is Andy Burrows, follow me on twitter @andrewburrows")]


def test_speaker_greets_sole_delegate_v3():  
    # Arrange
    sut = ConferenceSpeaker("Andy Burrows", "andrewburrows")
    delegate = Mock(spec=ConferenceDelegate)
    
    # Act
    sut.greet([delegate])
    
    # Assert
    delegate.speakto.assert_called_once_with("Hi my name is Andy Burrows, follow me on twitter @andrewburrows")


def test_speaker_greets_many_delegates():  
    # Arrange
    sut = ConferenceSpeaker("Andy Burrows", "andrewburrows")
    delegates = [ Mock(name=name) for name in ["Félix Bossuet", "Tchéky Karyo", "Margaux Chatelier", "Dimitri Storoge",
                                               "Andreas Pietschmann", "Urbain Cancelier", "Mehdi El Glaoui", "Paloma Palma",
                                               "Karine Adrover", "Loïc Varraut", "Jan Oliver Schroeder", "Tom Sommerlatte"
                                               "Andrée Damant", "Pasquale D'Inca", "Eric Soubelet"]]
    
    # Act
    sut.greet(delegates)
    
    # Assert
    for delegate in delegates:
        delegate.speakto.assert_called_once_with("Hi my name is Andy Burrows, follow me on twitter @andrewburrows")
    

if __name__=="__main__":
    print (Mock())
    print (Mock(name="My wonderful mock"))
    
    m = Mock()
    m.foo('hello')
    m.bar('world')
    x = m(0)
    x.hello(123)
    print(m.mock_calls)
    
    mock_delegate = Mock(spec=ConferenceDelegate)
    mock_delegate.snore(volume="LOUD")
    