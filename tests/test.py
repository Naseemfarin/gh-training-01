import src.main as main

def test_get_stock_price_range():
    for _ in range(10):
        price = main.get_stock_price("AAPL")
        assert 95 <= price <= 105

def test_monitor_stock_alerts(capsys):
    main.monitor_stock("AAPL", threshold=95, interval=0, checks=1)
    captured = capsys.readouterr()
    assert "ALERT" in captured.out