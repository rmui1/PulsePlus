#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/PulsePlus/")
sys.path.append("/var/www/PulsePlus/app/")

from app import app as application
application.secret_key = 'Add your secret key'
