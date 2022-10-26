from main import hello, goodbye


def test_hello():
    assert "hi" == hello()


def test_goodbye():
    assert "bye" == goodbye()
