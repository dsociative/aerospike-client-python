# -*- coding: utf-8 -*-

import pytest
import sys
import cPickle as pickle

try:
    import aerospike
except:
    print "Please install aerospike python client."
    sys.exit(1)
        
def handler(level, func, myfile, line):
    assert 1 == 1

class TestLog(object):

    def test_set_log_level_correct(self):
        """
        Test log level with correct parameters
        """

        response = aerospike.set_log_level(aerospike.LOG_LEVEL_DEBUG)

        assert response == 0

    def test_set_log_handler_correct(self):
        """
        Test log handler with correct parameters
        """

        response = aerospike.set_log_level(aerospike.LOG_LEVEL_DEBUG)

        aerospike.set_log_handler(handler)

        config = {
                "hosts": [("127.0.0.1", 3000)]
                }
        client = aerospike.client(config).connect()

        assert response == 0
        client.close()

    def test_set_log_level_None(self):
        """
        Test log level with log level as None
        """
        with pytest.raises(Exception) as exception:
            response = aerospike.set_log_level(None)

        assert exception.value[0] == -2
        assert exception.value[1] == 'Invalid log level'

    def test_set_log_level_incorrect(self):
        """
        Test log level with log level incorrect
        """
        response = aerospike.set_log_level(9)

        assert response == 0

    def test_set_log_handler_extra_parameter(self):
        """
        Test log handler with extra parameter
        """

        aerospike.set_log_level(aerospike.LOG_LEVEL_DEBUG)

        def handler(level, func, myfile, line):
            print "Level is: %d" % level

        def extrahandler(level, func, myfile, line):
            print "Level is: %d" % level

        with pytest.raises(TypeError) as typeError:
            aerospike.set_log_handler(handler, extrahandler)

        assert "setLogHandler() takes at most 1 argument (2 given)" in typeError.value
