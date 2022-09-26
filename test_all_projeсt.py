
import time
import pytest
from .pages.test_lending_page import TestLandingPage


class TestLandingHomePage():
        def visit_home_page(self):
            self.test_open_my_page()
