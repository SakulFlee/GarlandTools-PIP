"""
Tests for Author being correctly set in __init__.py
"""

from garlandtools import __author__

def test_version():
    """
    Tests for Author being correctly set in __init__.py
    """
    assert __author__ == "Lukas Weber"
