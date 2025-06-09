class ScoreStrategyFactory:
    def reward_score(self, question: Question, time_taken: int) -> float:
        raise NotImplementedError()