def test_admin_service_is_running(host):
    if host.ansible.get_variables()['inventory_hostname'] == 'kerberos-cluster-master':
        service = host.service("krb5-admin-server")
        assert service.is_running
        assert service.is_enabled

def test_kdc_service_is_running(host):
    service = host.service("krb5-kdc")
    assert service.is_running
    assert service.is_enabled

def test_kpropd_service_is_running(host):
    if host.ansible.get_variables()['inventory_hostname'] == 'kerberos-cluster-replica':
        service = host.service("krb5-kpropd")
        assert service.is_running
        assert service.is_enabled
