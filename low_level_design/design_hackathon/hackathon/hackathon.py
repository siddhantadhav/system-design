from strategies.score_strategy import ScoreStrategyFactory
from strategies.recommendation_strategy import RecommendationStrategyFactory
from typing import Dict, List, Tuple
from models.contestant import Contestant
from models.question import Question
from managers.contestant_manager import ContestantManager
from managers.question_library import QuestionLibrary

class Hackathon:
    def __init__(self, strategy: ScoreStrategyFactory, recommender: RecommendationStrategyFactory):
        self.contestant_question_solved: Dict[str, List[Tuple[str, int]]] = {}
        self.question_contestant_solved: Dict[str, List[Tuple[str, int]]] = {}
        self.contestant_scores: Dict[str, float] = {}
        self.strategy = strategy
        self.recommender = recommender

    def solve(self, contestant: Contestant, question: Question, time_taken: int) -> List[Question]:
        contestant.solve_question(question.question_id, time_taken)
        question.record_solve(time_taken)

        self.contestant_question_solved.setdefault(contestant.contestant_id, []).append((question.question_id, time_taken))
        self.question_contestant_solved.setdefault(question.question_id, []).append((contestant.contestant_id, time_taken))

        score = self.strategy.reward_score(question, time_taken)
        self.contestant_scores[contestant.contestant_id] = self.contestant_scores.get(contestant.contestant_id, 0) + score
        contestant.score += score

        return self.recommender.get_recommended_questions(question)

    def get_leader(self, contestant_manager: ContestantManager) -> Tuple[str, str]:
        if not self.contestant_scores:
            return ("", "")
        
        leader_id = max(self.contestant_scores, key=self.contestant_scores.get)
        leader = contestant_manager.get_contestant_by_id(leader_id)

        if leader:
            return (leader.name, leader.department)
        return ("", "")

    def get_average_time(self, question_id: str) -> float:
        if question_id not in self.question_contestant_solved:
            return 0.0
        total_time = sum(t for _, t in self.question_contestant_solved[question_id])
        count = len(self.question_contestant_solved[question_id])
        return total_time / count

    def get_solved_user_count(self, question_id: str) -> int:
        return len(self.question_contestant_solved.get(question_id, []))

    def get_top_liked_problems_by_tag(self, tag: str, n: int) -> List[Question]:
        qlib = QuestionLibrary.get_instance()
        questions = qlib.get_questions(filters={"tags": [tag]})
        return sorted(questions, key=lambda q: q.like_count, reverse=True)[:n]