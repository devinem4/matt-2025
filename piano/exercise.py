import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class Exercise:
    def __init__(self, name) -> None:
        self.name = name
        self.is_done = False
        self.status = "to do"
        self.start_time = None
        self.end_time = None
        self.table_cols = ["#", "Name", "Start", "Finish", "Status", "Duration"]

    def __str__(self) -> str:
        return self.name

    def start(self) -> None:
        self.status = "in progress"
        self.start_time = datetime.now()
        logger.info(f"{self.name} start")

    def complete(self) -> None:
        self.status = "done"
        self.is_done = True
        self.end_time = datetime.now()
        logger.info(f"{self.name} complete")

    def add_to_table(self, table):
        start_pretty = "-"
        if self.start_time:
            start_pretty = self.start_time.strftime("%Y-%m-%d %H:%M:%S")

        end_pretty = "-"
        if self.end_time:
            end_pretty = self.end_time.strftime("%Y-%m-%d %H:%M:%S")

        duration = "tbd"
        if self.start_time and self.end_time:
            time_diff = self.end_time - self.start_time
            duration_secs = int(time_diff.total_seconds())
            duration = f"{duration_secs // 60}m{duration_secs % 60}s"

        status_emoji = ":question_mark:"
        if self.status == "to do":
            status_emoji = ":wave:"
        elif self.status == "in progress":
            status_emoji = ":construction:"
        elif self.status == "done":
            status_emoji = ":heavy_check_mark:"

        table.add_row(
            str(table.row_count + 1),
            self.name,
            start_pretty,
            end_pretty,
            status_emoji,
            duration,
        )
