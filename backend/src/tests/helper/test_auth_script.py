# importing necessary modueles
from passlib.context import CryptContext
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import os
import sys

import logging
logging.getLogger("passlib").setLevel(logging.ERROR) # suppresing error from passlib 
# importing modules to test
dir_to_test = os.path.abspath("../../")
sys.path.append(dir_to_test)
from helper.auth_script import verify_password, get_password_hash
import unittest

# SECRET_KEY = str(os.environ.get("SECRET_KEY"))
# ALGORITHM = str(os.environ.get("ALGORITHM"))
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



class TestAuthScripts(unittest.TestCase):
    def setUp(self):
        self.secret_key = str(os.environ.get("SECRET_KEY"))
        self.alg = str(os.environ.get("ALGORITHM"))
        self.pwd_cntx = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.hashed_pwd = "$2b$12$78nr5lkjZglzgTzbYg0hweWgvAT7JD0yHvQye9EZWdYkPIAce8HUa"
        self.raw_password = "secret"
    
    def test_verify_password(self):
        result = self.pwd_cntx.verify(self.raw_password,self.hashed_pwd)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()