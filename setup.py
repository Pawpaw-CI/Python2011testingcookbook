# -*-coding:utf-8-*-
__author__ = "pawpawDu"
import sys
try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass
from setuptools import setup
setup(
    name="RegexPicker plugin",
    version="0.1",
    author="Greg L.Turnquist",
    author_email="Greg.LTurnquist@gmail.com",
    description="pick test methods based on a regular epression",
    License="Apache Server License 2.0",
    py_modules=["recipe13_plugin"],
    entry_points={
        'nose.plugins':['recipe13_plugin| = recipe13_plugin:RegexPicker']

    }
)
