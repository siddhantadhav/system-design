import pytest
from models.question import Question, QuestionDifficulty

def test_question_creation():
    q = Question("Sample question?", ["tag1", "tag2"], QuestionDifficulty.MEDIUM, 10)
    assert q.description == "Sample question?"
    assert q.tags == ["tag1", "tag2"]
    assert q.difficulty == QuestionDifficulty.MEDIUM
    assert q.score == 10
    assert q.like_count == 0
    assert q.solved_count == 0
    assert q.average_time_to_solve == 0.0

def test_like_question():
    q = Question("Sample question?", [], QuestionDifficulty.EASY, 5)
    q.like("contestant_1")
    assert q.like_count == 1

def test_record_solve_and_average_time():
    q = Question("Sample question?", [], QuestionDifficulty.EASY, 5)
    q.record_solve(20)
    q.record_solve(40)
    assert q.solved_count == 2
    assert q.total_time_taken == 60
    assert q.average_time_to_solve == 30.0
