from enum import Enum
from typing import List
import uuid

class QuestionDifficulty(Enum):
    EASY = 'easy'
    MEDIUM = 'medium'
    HARD = 'hard'

# ---------------- Models ----------------
class Question:
    def __init__(self, description: str, tags: List[str], difficulty: QuestionDifficulty, score: int):
        self.question_id = str(uuid.uuid4())
        self.description = description
        self.tags = tags
        self.difficulty = difficulty  
        self.score = score
        self.like_count = 0
        self.total_time_taken = 0
        self.solved_count = 0

    @property
    def average_time_to_solve(self) -> float:
        if self.solved_count == 0:
            return 0.0
        return self.total_time_taken / self.solved_count

    def like(self, contestant_id: str) -> bool:
        self.like_count += 1
        return True

    def record_solve(self, time_taken: int):
        self.total_time_taken += time_taken
        self.solved_count += 1