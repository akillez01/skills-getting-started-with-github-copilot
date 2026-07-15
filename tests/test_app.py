from fastapi.testclient import TestClient

from src.app import app, activities


client = TestClient(app)


def test_unregister_participant_removes_email():
    activity_name = "Chess Club"
    email = "newstudent@example.com"
    original_participants = activities[activity_name]["participants"][:]

    try:
        signup_response = client.post(f"/activities/{activity_name}/signup?email={email}")
        assert signup_response.status_code == 200

        unregister_response = client.delete(f"/activities/{activity_name}/signup?email={email}")
        assert unregister_response.status_code == 200
        assert email not in activities[activity_name]["participants"]
        assert "Removed" in unregister_response.json()["message"]
    finally:
        activities[activity_name]["participants"] = original_participants
