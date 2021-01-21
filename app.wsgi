#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/legendary-bassoon/")
sys.path.append("/var/www/legendary-bassoon/app/")

from app import app as application
application.secret_key = 'Add your secret key'

