"""
A unit test file to check the main functionalities of the application
"""


import hello_world


class TestHelloWorld:

    def test_hello_worldf(self):
        assert hello_world.hello_world() == 'Hello World'