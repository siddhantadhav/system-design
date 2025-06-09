from models.question import Question
from managers.question_library import QuestionLibrary
from typing import List

class RecommendationStrategyFactory:
    def get_recommended_questions(self, question: Question) -> List[Question]:
        raise NotImplementedError()


class MostLikedByTag(RecommendationStrategyFactory):
    def get_recommended_questions(self, question: Question) -> List[Question]:
        qlib = QuestionLibrary.get_instance()
        related_questions = [
            q for q in qlib.get_questions(filters={"tags": question.tags})
            if q.question_id != question.question_id
        ]
        return sorted(related_questions, key=lambda q: q.like_count, reverse=True)[:5]