import pytest

@pytest.mark.smoke
def test_login():
  print("Running smoke test: Login")
  assert True

@pytest.mark.regression
def test_checkout():
  print("Runnning Regression Test: Checkout")
  assert True
