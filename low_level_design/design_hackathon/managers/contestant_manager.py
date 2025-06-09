from models.contestant import Contestant
from typing import Optional, Dict

class ContestantManager:
    def __init__(self):
        self.all_contestants: Dict[str, Contestant] = {}
        self.email_to_id: Dict[str, str] = {}

    def add_contestant(self, name, email, department, password) -> Contestant:
        contestant = Contestant(name, email, department, password)
        self.all_contestants[contestant.contestant_id] = contestant
        self.email_to_id[email] = contestant.contestant_id
        return contestant

    def login(self, email, password) -> Optional[Contestant]:
        contestant_id = self.email_to_id.get(email)
        if not contestant_id:
            return None
        contestant = self.all_contestants[contestant_id]
        return contestant if contestant.password == password else None

    def get_contestant_by_id(self, contestant_id) -> Optional[Contestant]:
        return self.all_contestants.get(contestant_id)