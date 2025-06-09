import pytest
from models.contestant import Contestant

def test_contestant_solve_and_like():
    contestant = Contestant("id1", "Alice", "alice@example.com", "CS", "password123")
    
    # Initially no solved questions and score 0
    assert contestant.score == 0.0
    assert contestant.get_solved_questions() == []

    contestant.solve_question("q1", 15)
    assert "q1" in contestant.solved_questions
    assert contestant.solved_questions["q1"] == 15
    assert contestant.get_solved_questions() == ["q1"]

    # Like question
    assert not contestant.has_liked("q1")
    contestant.liked_questions.add("q1")
    assert contestant.has_liked("q1")
