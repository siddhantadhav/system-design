from managers.question_library import QuestionLibrary
from managers.contestant_manager import ContestantManager
from models.question import Question, QuestionDifficulty
from hackathon.hackathon import Hackathon
from strategies.score_strategy import BasicScoreStrategy
from strategies.recommendation_strategy import MostLikedByTag

# ---------------- DRIVER ----------------
if __name__ == "__main__":
    # Setup
    qlib = QuestionLibrary.get_instance()
    manager = ContestantManager()

    # Add Questions
    q1 = Question("What is Python?", ["programming", "python"], QuestionDifficulty.EASY, 10)
    q2 = Question("What is polymorphism?", ["oop", "concepts"], QuestionDifficulty.MEDIUM, 20)
    q3 = Question("Explain Dijkstra's algorithm", ["graphs", "algorithms"], QuestionDifficulty.HARD, 30)

    qlib.add_question(q1)
    qlib.add_question(q2)
    qlib.add_question(q3)

    # Add Contestant
    contestant = manager.add_contestant("Siddhant", "isiddhantadhav@gmail.com", "EE", "pass123")

    # Hackathon Starts
    hackathon = Hackathon(BasicScoreStrategy(), MostLikedByTag())

    # Solve a Question
    recommended = hackathon.solve(contestant, q1, time_taken=15)
    print("Recommended Questions after solving Q1:")
    for r in recommended:
        print(f"- {r.description} [{r.like_count} likes]")

    # Like a question
    q1.like(contestant.contestant_id)

    # Show Leader
    leader_name, leader_department = hackathon.get_leader(manager)
    print(leader_name, leader_department)
    # Show average time
    print(f"Avg Time for Q1: {hackathon.get_average_time(q1.question_id)}s")
    print(f"Solved User Count for Q1: {hackathon.get_solved_user_count(q1.question_id)}")

    # Show top liked questions by tag
    top_liked = hackathon.get_top_liked_problems_by_tag("python", 3)
    print("\nTop liked questions with tag 'python':")
    for q in top_liked:
        print(f"- {q.description} ({q.like_count} likes)")
