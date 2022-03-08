import count_words
import unique_words
import stop_word_removal, stop_word_removal_with_set
import pytest

def test_no_words():
        assert count_words.count_words('test1.txt') == 43

def test_unique_words():
    assert unique_words.count_unique('test1.txt') == 29


def test_histogram():
    assert unique_words.create_histogram('This a a a',dict) == {'This':1,'a':3}


@pytest.mark.stopwordremoval
def test_stop_word_removal_with_spaces_in_punctuation():
    assert stop_word_removal.remove_words('test1.txt','noise1.txt') == 30

@pytest.mark.stopwordremoval
def test_stop_word_removal_without_spaces_in_punctuation():
    assert stop_word_removal.remove_words('test1.txt','noise2.txt' )== 30

def test_stop_word_removal_with_set():
    assert stop_word_removal_with_set.remove_words('test1.txt','noise1.txt' ) == 30