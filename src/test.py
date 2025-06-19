"""
Unit tests for the main stock monitor module.
"""
from src import main

def test_get_stock_price_range():
    """
    Test that get_stock_price returns a value within the expected range.
    """
    for _ in range(10):
        price = main.get_stock_price("AAPL")
        assert 95 <= price <= 105

def test_monitor_stock_alerts(capsys):
    """
    Test that monitor_stock prints an alert when the threshold is low.
    """
    main.monitor_stock("AAPL", threshold=95, interval=0, checks=1)
    captured = capsys.readouterr()
    assert "ALERT" in captured.out
