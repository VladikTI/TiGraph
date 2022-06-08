from setuptools import setup

APP = ['основа.py']
DATA_FILES = ['t.png']
APP_NAME = "Tigrapg"

OPTIONS = {
'iconfile': 't.png'
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
