from wordle import Colour, _validate_submission, _get_colour

# -- validation testing --

def test_length_validation():
    """Test that any submissions not 5 chars long are rejected"""
    assert _validate_submission("TOOLONG") == False
    assert _validate_submission("TOOS") == False
    assert _validate_submission("") == False
    assert _validate_submission("RIGHT") == True

def test_alphabetic_validation():
    """Test that any submissions not purely alphabetic are rejected"""
    assert _validate_submission("DOG12") == False
    assert _validate_submission("...//") == False
    assert _validate_submission("HELLO") == True

# -- evaluation testing --

def test_correct_colour():
    """Test that a single letter in the right place is marked green"""
    assert _get_colour(0, submission_word="DODGE", target_word="DEANS") == Colour.GREEN

def test_green_gets_used_up():
    """Test that any surplus matches are marked red"""
    assert _get_colour(0, submission_word="DODGE", target_word="DEANS") == Colour.GREEN
    assert _get_colour(2, submission_word="DODGE", target_word="DEANS") == Colour.RED

def test_yellow():
    """Test that a single letter in the wrong place is marked yellow"""
    assert _get_colour(0, submission_word="PRINT", target_word="TRIPE") == Colour.YELLOW

def test_yellow_gets_used_up():
    """Test that any surplus matches in the wrong place are marked red"""
    assert _get_colour(0, submission_word="PAPER", target_word="OPTIC") == Colour.YELLOW
    assert _get_colour(2, submission_word="PAPER", target_word="OPTIC") == Colour.RED


        