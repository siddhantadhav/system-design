import pytest
from hackathon.hackathon import Hackathon
from managers.question_library import QuestionLibrary
from managers.contestant_manager import ContestantManager
from models.question import Question, QuestionDifficulty
from models.contestant import Contestant
from strategies.score_strategy import BasicScoreStrategy

@pytest.fixture
def setup_hackathon():
    # Setup QuestionLibrary and ContestantManager with data
    qlib = QuestionLibrary()
    qlib.question_library.clear()

    clib = ContestantManager()
    clib.all_contestants.clear()
    clib.email_to_id.clear()

    # Add questions
    q1 = Question("Q1", ["tag1"], QuestionDifficulty.EASY, 10)
    q2 = Question("Q2", ["tag2"], QuestionDifficulty.MEDIUM, 20)
    qlib.add_question(q1)
    qlib.add_question(q2)

    # Add contestants
    c1 = clib.add_contestant("Alice", "alice@example.com", "CS", "pwd")
    c2 = clib.add_contestant("Bob", "bob@example.com", "IT", "pwd")

    strategy = BasicScoreStrategy()
    hackathon = Hackathon(strategy)
    return hackathon, qlib, clib, q1, q2, c1, c2

def test_solve_and_leader(setup_hackathon):
    hackathon, qlib, clib, q1, q2, c1, c2 = setup_hackathon

    recs = hackathon.solve(c1.contestant_id, q1.question_id, 15)
    assert q1.solved_count == 1
    assert c1.score > 0

    leader = hackathon.get_leader()
    assert leader[0] == c1.name

def test_get_average_time_and_solved_count(setup_hackathon):
    hackathon, qlib, clib, q1, q2, c1, c2 = setup_hackathon
    hackathon.solve(c1.contestant_id, q1.question_id, 10)
    hackathon.solve(c2.contestant_id, q1.question_id, 20)

    avg_time = hackathon.get_average_time(q1.question_id)
    solved_count = hackathon.get_solved_user_count(q1.question_id)

    assert avg_time == 15.0
    assert solved_count == 2
