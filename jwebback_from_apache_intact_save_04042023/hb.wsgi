import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.append('Your Virtual Environment Packages')
sys.path.append('your directory')

from app import app as application
application.secret_key= "Add your key"


