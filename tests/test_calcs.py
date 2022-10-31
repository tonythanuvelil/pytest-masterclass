from calcs import subtract


def setup_function(function):
    print(f"Running setup: {function.__name__}")
    function.x = 10


def teardown_function(function):
    print(f"Running teardown: {function.__name__}")
    del function.x


def test_calcs_subtract():
    assert subtract(test_calcs_subtract.x) == 9
