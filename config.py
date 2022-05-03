import os
from dotenv import load_dotenv

# ABSOLUTE PATH TO CURRENT DIRECTORY
basedir = os.path.abspath(os.path.dirname(__name__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
                        # PASS IN VARIABLES FOR FLASK FROM .ENV
    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')