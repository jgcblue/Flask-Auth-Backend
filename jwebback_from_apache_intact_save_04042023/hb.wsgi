import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.append('/var/www/hb/venv/lib/python3.10/site-packages')
sys.path.append('/var/www/hb')

from app import app as application
application.secret_key= "Add your key"


