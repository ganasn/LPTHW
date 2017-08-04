from nose.tools import *
import ex47.game import Room #Project name

def test_room():
    gold = Room('GoldRoom', 'This room is the Gold Room, Gold In Name Only')
    assert_equal(gold.name, 'GoldRoom')
    assert_equal(gold.paths, {})
    return 0

def test_room_paths():
    center = Room('Center','Test room in the center')
    north = Room('North', 'Test room in the north')
    
    south = Room('South', 'Test room in the south')
    center.add_paths({'north':north, 'south':south})
    assert_equal(center.go('north'),north)
    assert_equal(center.go('south'),south)
    return 0

def test_map():
    start = Room('Start','You\'re starting the game')
    west = Room('Trees','Go east or you run into the trees')
    down = Room('Dungeon', 'Go up to get some light')
    
    start.add_paths({'west':west, 'down':down})
    west.add_paths({'east':start})
    down.add_paths({'up':start})
    
    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)

#def setup():
#    print 'within setup()'
#
#def teardown():
#    print 'teardown()'
#    
#def test_basic():
#    print 'execute'