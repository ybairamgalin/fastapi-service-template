def test_schema(service):
    response = service.post('/data?name=some_name')
    assert response.status_code == 201
