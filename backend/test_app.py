import pytest
from app import db, Word
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

@pytest.fixture
def client():
    from app import create_app
    test_app = create_app("sqlite:///:memory:")
    with test_app.app_context():
        db.drop_all()
        db.create_all()
        db.session.add_all([
            Word(category="numbers",       indonesian="satu", english="one"),
            Word(category="basic phrases", indonesian="halo", english="hello"),
        ])
        db.session.commit()
        with test_app.test_client() as client:
            yield client

def test_health(client):
    res = client.get("/api/health")
    assert res.status_code == 200
    assert res.json["status"] == "ok"

def test_get_all_words(client):
    res = client.get("/api/words")
    assert res.status_code == 200
    assert len(res.json) == 2

def test_get_words_by_category(client):
    res = client.get("/api/words/numbers")
    assert res.status_code == 200
    assert len(res.json) == 1
    assert res.json[0]["indonesian"] == "satu"

def test_invalid_category_returns_empty(client):
    res = client.get("/api/words/invalid")
    assert res.status_code == 200
    assert res.json == []