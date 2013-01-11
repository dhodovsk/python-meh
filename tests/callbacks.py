# -*- coding: utf-8 -*-

from tests.baseclass import BaseTestCase
from meh import Config, ConfigError

def callback1():
    return "This was generated by the callback1"

def callback2():
    return "This was generated by the callback2"

def callback3():
    raise RuntimeError("Testing callback raising exception")

class Callbacks_TestCase(BaseTestCase):
    def runTest(self):
        conf = Config(programName="CallbacksTest",
                      programVersion="1.0",
                      callbackDict={"callback1": callback1,
                                    "callback2": callback2})

        # another way to register callback
        conf.register_callback("callback3", callback3)

        # callback with given item name already registered
        with self.assertRaises(ConfigError):
            conf.register_callback("callback3", callback2)

        # should not raise exception
        dump = self.dump(conf, None)

        self.assertIn("callback1:\nThis was generated by the callback1\n",
                      dump)
        self.assertIn("callback2:\nThis was generated by the callback2\n",
                      dump)
        self.assertIn("callback3: Caused error", dump)


