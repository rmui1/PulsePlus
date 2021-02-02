#!/user/bin/python3
import sys
sys.path.insert(0, "/var/www/PulsePlus/")
sys.path.insert(0, "/var/www/PulsePluse/app/")

import logging
logging.basicConfig(stream=sys.stderr)

from app import app as application
