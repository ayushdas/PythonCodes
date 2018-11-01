from nose.tools import *
from NAME.game import Room

# def setup():
#     print('Setup')

# def teardown():
#     print('Tear Down')

def test_basic():
    print('I ran')


def test_room():
    gold = Room("Gold Room",'This is the gold room')
    assert_equal(gold.name,"Gold Room")
    assert_equal(gold.paths,[])    