from .interface import OutputStrategy


class ConsoleOutputStrategy(OutputStrategy):
    def output(self, data: list[dict]):
        for row in data:
            print(row)
