from models.question import Question

class ScoreStrategyFactory:
    def reward_score(self, question: Question, time_taken: int) -> float:
        raise NotImplementedError()


class BasicScoreStrategy(ScoreStrategyFactory):
    def reward_score(self, question: Question, time_taken: int) -> float:
        return question.score