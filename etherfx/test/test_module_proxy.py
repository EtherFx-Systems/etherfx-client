import etherfx

def test_import_proxy_module():
    import ether.fakemodule
    assert ether.fakemodule.is_proxy()