import time
import pytest
from pages.test_lending_page import TestLanding


class TestLandingPage():
    def visit_home_page(self):
        self.test_open_my_page()
