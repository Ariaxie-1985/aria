import code
import unittest
from alembic.util import status
from utils.util import assert_equal, form_post, get_requests, json_post
import requests
import pytest
from api_script_xm.requests_test_cancellation import get_requests_json, get_requests_html, post_requests_json, \
    post_requests_form


def test_get_requests_json():
    r = get_requests_json()
    if r['hello'] == 'world':
        assert True


def test_post_requests_json():
    r = post_requests_json()
    assert_equal(1, r['state'], '接口调用成功')


def test_post_requests_form():
    r = post_requests_form()
    assert_equal(1, r['state'], '接口调用成功')


def test_get_requests_html():
    r = get_requests_html()
    if code == 200:
        assert True
