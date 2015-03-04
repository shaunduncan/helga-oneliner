from mock import patch

import helga_oneliner as oneliner


@patch('helga_oneliner.RESPONSES', {'foo': 'bar'})
def test_find_response_finds_none():
    assert oneliner.find_response('do not match') is None


@patch('helga_oneliner.RESPONSES', {'foo': ('bar', 'baz')})
def test_find_response_returns_random_item():
    assert oneliner.find_response('foo') in ('bar', 'baz')


@patch('helga_oneliner.RESPONSES', {'foo': 'bar'})
def test_find_response():
    assert oneliner.find_response('foo') == 'bar'
