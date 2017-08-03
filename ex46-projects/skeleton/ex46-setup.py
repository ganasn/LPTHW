#Exercise 46 - setting up a project
#setup.py

try: 
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = {
    'description':'LPTHW',
    'author':'GN',
    'url':'https://github.io/ganasn/LPTHW.git',
    'download_url':'https://github.io/ganasn/LPTHW.git',
    'version':'0.1',
    'scripts':[],
    'name':'projectname'
}

setup(**config)