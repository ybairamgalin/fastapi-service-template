def test_schema(service):
    response = service.get('/data')
    assert response.status_code == 200
