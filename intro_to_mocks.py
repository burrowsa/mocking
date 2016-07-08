from unittest.mock import Mock

my_mock = Mock()
my_mock

my_mock = Mock(name="my_mock")
my_mock

my_mock.hello

my_mock()

my_mock.a_method(1, 2, 3)

from unittest.mock import Mock, MagicMock

my_magic_mock = MagicMock(name="my_magic_mock")

my_magic_mock + 1

my_magic_mock['hello']


