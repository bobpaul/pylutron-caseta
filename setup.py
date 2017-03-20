#!/usr/bin/python

from distutils.core import setup

setup(
    name="pylutron_caseta",
    version="0.2.3",
    license="Apache",
    description="""Provides an API to the Lutron Smart Bridge""",
    author="gurumitts",
    author_email="",
    maintainer="guumitts",
    maintainer_email="",
    platforms=["Linux"],
    url="https://github.com/gurumitts/pylutron-caseta",
    download_url="https://github.com/gurumitts/pylutron-caseta",
    packages=["pylutron_caseta"], requires=['paramiko']
)

