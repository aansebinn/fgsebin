import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import pytest

from Pages.Login import *

def test_login():
    login()
    print("login success")

