from setuptools import setup

setup (
    name='snapshot',
    version='0.1',
    author='Brad Craigen',
    author_email="brad@bjc.com.au",
    description="this is a summary",
    packages=['shotty'],
    url="https://bjc.com.au",
    install_requires=[
        'click',
        'boto3'
        ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
        ''',
    )