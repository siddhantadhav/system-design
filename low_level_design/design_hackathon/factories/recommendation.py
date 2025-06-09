class RecommendationStrategyFactory:
    def get_recommended_questions(self, question: Question) -> List[Question]:
        raise NotImplementedError()