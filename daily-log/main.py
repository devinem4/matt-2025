from datetime import datetime, timedelta
import os
from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Confirm, Prompt
from rich.table import Table


console = Console()

yesterday = datetime.today() + timedelta(days=-1)
day_of_year = yesterday.timetuple().tm_yday
yesterday_formatted = yesterday.__str__()[:10]

hello = f"# Log for {yesterday_formatted} ({day_of_year}/365)"

console.print(Markdown(hello))

class Question:
    def __init__(self, quest_text, quest_type):
        self.quest_text = quest_text
        self.quest_type = quest_type
        self.answer = None

    def ask(self):
        if self.quest_type == "yn":
            self.answer = Confirm.ask(self.quest_text)
        else:
            self.answer = Prompt.ask(self.quest_text)

    def answer_to_str(self):
        if self.answer is None:
            return ""
        if self.quest_type == "yn":
            if self.answer:
                return "Y"
            return "N"
        return self.answer

    def add_row(self, table):
        if self.answer is None:
            return
        table.add_row(self.quest_text, self.answer_to_str())

    def log(self, f):
        f.write(f"{yesterday_formatted} -- {self.quest_text} = {self.answer_to_str()}\n")

questions = [
    Question("Practice Piano?", "yn"),
    Question("Get some exercise?", "yn"),
    Question("Late Night Snacking? :cake:", "yn"),
]

answer_table = Table(title="Today's Answers")
answer_table.add_column("Question")
answer_table.add_column("Answer")

for q in questions:
    q.ask()

for q in questions:
    q.add_row(answer_table)

console.print(answer_table)

if not os.path.exists("data"):
    os.mkdir("data")

with open("data/matt.log", "a") as f:
    for q in questions:
        q.log(f)

console.print("Answers saved, see you next time :wave:")
