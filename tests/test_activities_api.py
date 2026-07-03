def test_get_activities_returns_all_activities_with_expected_shape(client):
    # Arrange
    required_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data

    for activity_name, details in data.items():
        assert isinstance(activity_name, str)
        assert required_fields.issubset(details.keys())
        assert isinstance(details["participants"], list)
