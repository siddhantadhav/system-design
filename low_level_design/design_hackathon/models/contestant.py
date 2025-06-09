from typing import Set, List, Dict
import uuid

class Contestant:
    def __init__(self, name: str, email: str, department: str, password: str):
        self.contestant_id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.department = department
        self.password = password
        self.solved_questions: Dict[str, int] = {}
        self.score: float = 0
        self.liked_questions: Set[str] = set()

    def solve_question(self, question_id: str, time_taken: int):
        self.solved_questions[question_id] = time_taken

    def get_solved_questions(self) -> List[str]:
        return list(self.solved_questions.keys())

    def has_liked(self, question_id: str) -> bool:
        return question_id in self.liked_questions