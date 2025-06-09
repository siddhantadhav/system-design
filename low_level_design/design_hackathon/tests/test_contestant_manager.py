import pytest
from managers.contestant_manager import ContestantManager

def test_add_and_login_contestant():
    manager = ContestantManager.get_instance()

    # Clear data for test isolation if possible
    manager.all_contestants.clear()
    manager.email_to_id.clear()

    c = manager.add_contestant("Bob", "bob@example.com", "IT", "pass123")
    assert c.email == "bob@example.com"

    logged_in = manager.login("bob@example.com", "pass123")
    assert logged_in.name == "Bob"

    with pytest.raises(ValueError):
        manager.login("bob@example.com", "wrongpass")
