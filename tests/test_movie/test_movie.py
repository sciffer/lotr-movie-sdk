"""Tests for movie SDK."""
import json

import pytest

from lotr_movie_sdk.movie import Movie


def test_movie_list(response_mock):
    """Movie test with parametrization."""
    content = [{"_id": "fakeid1", "name": "movie1name"}, {"_id": "fakeid2", "name": "movie2name"}]
    response = json.dumps({"docs": content, "total": 2})
    with response_mock(f"GET http://mock.test/v1/movie -> 200 :{response}", bypass=False):
        m = Movie("mocktestkey", "http://mock.test/v1/")
        assert m.list() == content


@pytest.mark.parametrize(
    ("id", "expected"),
    [
        ("123abc", {"_id": "123abc", "name": "movie1name"}),
        ("234sdf", {"_id": "234sdf", "name": "movie2name"}),
    ],
)
def test_movie(id, expected, response_mock):
    """Movie test with parametrization."""
    response = json.dumps({"docs": expected, "total": 1})
    with response_mock(f"GET http://mock.test/v1/movie/{id} -> 200 :{response}", bypass=False):
        m = Movie("mocktestkey", "http://mock.test/v1/")
        assert m.get(id) == expected


@pytest.mark.parametrize(
    ("id", "expected"),
    [
        ("123abc", [{"_id": "45t45t", "quote": "move 1 quote 1"}, {"_id": "34r34r", "quote": "move 1 quote 2"}]),
        ("234sdf", [{"_id": "erg2342", "quote": "move 2 quote 1"}, {"_id": "34r34r4", "quote": "move 2 quote 2"}]),
        ("3f33rf", []),
    ],
)
def test_movie_quotes(id, expected, response_mock):
    """Movie test with parametrization."""
    response = json.dumps({"docs": expected, "total": len(expected)})
    with response_mock(f"GET http://mock.test/v1/movie/{id}/quote -> 200 :{response}", bypass=False):
        m = Movie("mocktestkey", "http://mock.test/v1/")
        assert m.quotes(id) == expected
