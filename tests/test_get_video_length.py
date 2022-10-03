#!/usr/bin/env python

"""Tests for `get_video_length` package."""

#import pytest


from get_video_length.get_video_length import gvl


# normal_url = "https://www.youtube.com/watch?v=H0dqSl3epvg"

# @pytest.fixture
# def response(self):
#     """Sample pytest fixture.

#     See more at: http://doc.pytest.org/en/latest/fixture.html
#     """
#     # import requests
#     # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


# def test_content(self,response):
#     """Sample pytest test function with the pytest fixture as an argument."""
#     # from bs4 import BeautifulSoup
#     # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_url_validty():
    assert gvl._check_online_video_id_validity(
        "https://www.youtube.com/watch?v=H0dqSl3epvg"
    )
