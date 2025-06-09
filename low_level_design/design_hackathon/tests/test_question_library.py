import pytest
from models.question import Question, QuestionDifficulty
from managers.question_library import QuestionLibrary

def test_singleton_instance():
    lib1 = QuestionLibrary.get_instance()
    lib2 = QuestionLibrary.get_instance()
    assert lib1 is lib2

def test_add_and_get_question():
    lib = QuestionLibrary.get_instance()
    q = Question("Test?", ["tag1"], QuestionDifficulty.EASY, 10)
    added = lib.add_question(q)
    assert added is True
    fetched = lib.get_question_details(q.question_id)
    assert fetched == q

def test_get_questions_filter_and_sort():
    lib = QuestionLibrary.get_instance()
    lib.question_library.clear()

    q1 = Question("Q1", ["math"], QuestionDifficulty.EASY, 10)
    q2 = Question("Q2", ["math", "dp"], QuestionDifficulty.HARD, 50)
    q3 = Question("Q3", ["greedy"], QuestionDifficulty.MEDIUM, 30)

    lib.add_question(q1)
    lib.add_question(q2)
    lib.add_question(q3)

    # Filter by tag
    math_questions = lib.get_questions(filters={"tags": ["math"]})
    assert len(math_questions) == 2

    # Filter by difficulty
    easy_questions = lib.get_questions(filters={"difficulty": QuestionDifficulty.EASY})
    assert len(easy_questions) == 1
    assert easy_questions[0].difficulty == QuestionDifficulty.EASY

    # Sort by score ascending
    sorted_questions = lib.get_questions(sort_by="score", order="asc")
    assert sorted_questions[0].score <= sorted_questions[1].score <= sorted_questions[2].score
