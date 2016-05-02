import os

env = os.environ.get('ENV', 'development')

def debug(*kwargs):
    if env == 'development':
        print(' - '.join(kwargs))
