from typing import Dict, Optional, List, Any
from models.question import Question

class QuestionLibrary:
    _instance = None

    def __init__(self):
        if type(self)._instance is not None:
            raise Exception("Singleton class should be initialized once.")
        self.question_library: Dict[str, Question] = {}

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def add_question(self, question: Question) -> bool:
        if question.question_id not in self.question_library:
            self.question_library[question.question_id] = question
            return True
        return False

    def get_question_details(self, question_id: str) -> Question:
        if question_id not in self.question_library:
            raise ValueError("Question not found in the library")
        return self.question_library[question_id]

    def get_questions(self, filters: Optional[Dict[str, Any]] = None, sort_by: Optional[str] = None, order: str = "desc") -> List[Question]:
        filters = filters or {}
        questions = list(self.question_library.values())
        for key, value in filters.items():
            if key == "tags":
                questions = [q for q in questions if any(tag in q.tags for tag in value)]
            elif hasattr(questions[0], key):
                questions = [q for q in questions if getattr(q, key) == value]

        if sort_by:
            reverse = order == "desc"
            if hasattr(questions[0], sort_by):
                questions.sort(key=lambda q: getattr(q, sort_by), reverse=reverse)

        return questions