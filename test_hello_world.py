"""
A unit test file to check the main functionalities of the application
"""


import hello_world


class TestHelloWorld:

    def test_hello_world():
        assert hello_world() == 'Hello world'
