from report_out import parse_logs

from datetime import datetime, timedelta
import os
from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Confirm
from rich.table import Table


console = Console()

yesterday = datetime.today() + timedelta(days=-1)
day_of_year = yesterday.timetuple().tm_yday
yesterday_formatted = yesterday.__str__()[:10]

history = parse_logs()

hello = f"# Log for {yesterday_formatted} ({day_of_year}/365)"

console.print(Markdown(hello))

class Question:
    def __init__(self, quest_text):
        self.quest_text = quest_text
        self.answer = None
        self.all_answers = history[quest_text]

    def ask(self):
        self.answer = Confirm.ask(self.quest_text)
        self.all_answers.append(self.answer_to_str())

    def answer_to_str(self):
        if self.answer is None:
            return ""
        if self.answer:
            return "Y"
        return "N"

    def add_row(self, table):
        if self.answer is None:
            return
        history = ""
        yes_count = 0
        for ans in self.all_answers:
            if ans == "Y":
                history += ":star:"
                yes_count += 1
            else:
                history += ":x:"
        history_w_summary = f"{history} ({yes_count}/{len(self.all_answers)})"
        table.add_row(self.quest_text, self.answer_to_str(), history_w_summary)

    def log(self, f):
        f.write(f"{yesterday_formatted} -- {self.quest_text} = {self.answer_to_str()}\n")

questions = [
    Question("Practice Piano?"),
    Question("Get some exercise?"),
    Question("Avoid Late Night Snacking? :cake:"),
]

answer_table = Table(title="Today's Answers")
answer_table.add_column("Question")
answer_table.add_column("Answer")
answer_table.add_column("History")

with open("data/matt.log", "a") as f:
    for q in questions:
        q.ask()
        q.log(f)

for q in questions:
    q.add_row(answer_table)

console.print(answer_table)

if not os.path.exists("data"):
    os.mkdir("data")


console.print("Answers saved, see you next time :wave:")
