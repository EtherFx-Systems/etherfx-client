def test_import_proxy_module():
    import ether.six
    assert ether.six.PY2 == False