import logging
from rich.table import Table
from rich.prompt import Prompt

logger = logging.getLogger(__name__)


class Exercise_Group:
    table_columns = ["#", "Name", "Start", "Finish", "Status", "Duration"]

    def __init__(self, name, exercises, table_cols=None) -> None:
        self.name = name
        self.status = "to do"
        self.exercises = exercises
        self.current_exercise = None
        if table_cols:
            self.table_cols = table_cols
        else:
            self.table_cols = ["#", "Name", "Start", "Finish", "Status", "Duration"]

    def __str__(self) -> str:
        return self.name

    def make_table(self, complete_ex_only=False) -> Table:
        table = Table(title=self.name, title_justify="left")
        for col in self.table_columns:
            table.add_column(col)
        for e in self.exercises:
            if not complete_ex_only or e.is_done:
                e.add_to_table(table)
        return table

    def is_done_with_all_exercises(self) -> bool:
        for e in self.exercises:
            if not e.is_done:
                return False
        return True

    def is_done_with_any_exercises(self) -> bool:
        for e in self.exercises:
            if e.is_done:
                return True
        return False

    def prompt_exercise(self) -> int:
        choices = []
        for i, e in enumerate(self.exercises):
            if e.status == "to do":
                choices.append(str(i + 1))
        if len(choices) >= 1:
            selection = Prompt.ask(
                "Select an exercise (q to quit): ",
                default=choices[0],
                choices=(choices + ["q"]),
            )
            if selection.upper() == "Q":
                return 0
            return int(selection)
        Prompt.ask("On the last exercise, press enter to continue")
        return 0

    def run_group(self, console) -> None:
        logger.info(f"{self.name} start")
        while not (self.is_done_with_all_exercises()):
            console.print(self.make_table())
            selection = self.prompt_exercise()
            if selection == 0:
                break
            if self.current_exercise:
                self.current_exercise.complete()
            self.current_exercise = self.exercises[selection - 1]
            self.current_exercise.start()

        # clean-up last exercise
        if self.current_exercise:
            self.current_exercise.complete()

        console.print(f"Done with {self.name}")
        console.print()
        logger.info(f"{self.name} complete")
