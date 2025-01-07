from datetime import datetime
import logging
import os
from typing import List
from rich.console import Console
from rich.prompt import Prompt

from exercise_group import Exercise_Group

console = Console()
logger = logging.getLogger(__name__)


class Session:
    def __init__(self, groups: List[Exercise_Group]) -> None:
        self.session_name = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.groups = groups

    def show_session(self) -> None:
        console.print(f"[bold magenta]Session {self.session_name}[/bold magenta]")
        for group in self.groups:
            console.print(group.make_table())

    def save_session(self, path="data") -> None:
        if not os.path.exists(path):
            os.mkdir(path)

        file_path = f"{path}/{self.session_name}.log"

        with open(file_path, "w") as file:
            file_console = Console(file=file)
            file_console.print(
                f"[bold magenta]Session {self.session_name}[/bold magenta]"
            )
            for group in self.groups:
                if group.is_done_with_any_exercises():
                    file_console.print(group.make_table(complete_ex_only=True))

        logger.info(f"session saved to {file_path}")

    def run_session(self):
        logger.info("starting session")
        self.show_session()
        Prompt.ask("Press any key to continue (ctrl+z to abort)")
        for g in self.groups:
            g.run_group(console)

        console.print(":tada: All done! See you next time.")
        logger.info("session complete")
        self.show_session()
        self.save_session()
