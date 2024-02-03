from project import get_username, story_text, start, images, letter_print
import pytest
from climage import convert


def test_get_username():
    assert get_username("  CS50  ")[0] == """[BOOTING SYSTEMS]
Main Power
    \x1b[38;5;196m<OFFLINE>\x1b[0m
Backup Power
    \x1b[38;5;196m<OFFLINE>\x1b[0m
Coms
    \x1b[38;5;196m<OFFLINE>\x1b[0m
----------------------------------------
[URGENT] CS50, main power control panel is inaccessible, human intervention required.
[URGENT] Backup power control panels inaccessible, human intervention required.
[URGENT] Airlocks inaccessible, human intervention required.
[SYSTEM] Air flow inhibited, possible threat.
    <Conclusion reach from shifting of weight.>
"""

# even though it just print's test letter by letter,
# I still have a end variable to test
def test_letter_print():
    assert letter_print("hello CS50") == print("hello CS50")
    assert letter_print("hello CS50", end="") == print("hello CS50", end="")
    assert letter_print("hello CS50", end=", Goodbye CS50") == print("hello CS50, Goodbye CS50")


def test_start():
    assert start("yes") == None
    assert start("y") == None
    with pytest.raises(SystemExit):
        start("no")
    with pytest.raises(SystemExit):
        start("n")
    with pytest.raises(SystemExit):
        start("CS50")

def test_story_text():
    assert story_text("part1") == open("text/story.txt").read()
    assert story_text("bridge") == open("text/story1.txt").read()


def test_image_database():
    assert images(0) == convert("images/image0.png", is_unicode=True,
                                is_256color=False, is_truecolor=True)
    assert images(1) == convert("images/image1.png", is_unicode=True,
                                is_256color=False, is_truecolor=True)
