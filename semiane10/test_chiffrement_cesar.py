import pytest
from chiffrement_cesar import *

def test_chiffrer_abc():
    message_secret = "abc"
    message_chiffre_attendu = "def"
    assert chiffrer(message_secret) == message_chiffre_attendu

def test_chiffrer_zoo():
    message_secret = "zoo"
    message_chiffre_attendu = "crr"
    assert chiffrer(message_secret) == message_chiffre_attendu

def test_chiffrer_xyz():
    message_secret = "xyz"
    message_chiffre_attendu = "abc"
    assert chiffrer(message_secret) == message_chiffre_attendu

def test_dechiffrer_abc():
    message_secret = "abc"
    message_chiffre_attendu = "xyz"
    assert dechiffrer(message_secret) == message_chiffre_attendu