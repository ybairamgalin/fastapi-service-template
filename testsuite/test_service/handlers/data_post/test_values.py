def test_schema(service):
    response = service.post('/data')
    assert response.status_code == 201
