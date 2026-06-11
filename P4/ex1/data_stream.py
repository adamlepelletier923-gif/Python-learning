from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[str] = []
        self._processed_count: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No data available in processor")
        rank = self._processed_count - len(self._storage)
        value = self._storage.pop(0)
        return (rank, value)

    def remaining(self) -> int:
        return len(self._storage)

    def total_processed(self) -> int:
        return self._processed_count


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if isinstance(data, list):
            return all(
                isinstance(item, (int, float))
                and not isinstance(item, bool)
                for item in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._storage.append(str(item))
                self._processed_count += 1
        else:
            self._storage.append(str(data))
            self._processed_count += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self._storage.append(item)
                self._processed_count += 1
        else:
            self._storage.append(data)
            self._processed_count += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return self._is_valid_log_dict(data)
        if isinstance(data, list):
            return all(
                isinstance(item, dict)
                and self._is_valid_log_dict(item)
                for item in data)
        return False

    def _is_valid_log_dict(self, data: dict[Any, Any]) -> bool:
        if set(data.keys()) != {"log_level", "log_message"}:
            return False
        return isinstance(
            data["log_level"], str) and isinstance(data["log_message"], str)

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for item in data:
                self._storage.append(
                    f"{item['log_level']}: {item['log_message']}")
                self._processed_count += 1
        else:
            self._storage.append(f"{data['log_level']}: {data['log_message']}")
            self._processed_count += 1


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            handled = False
            for processor in self._processors:
                if processor.validate(element):
                    processor.ingest(element)
                    handled = True
                    break
            if not handled:
                print(
                    f"DataStreamerror-Can't processelementinstream: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for processor in self._processors:
            print(
                f"{processor.__class__.__name__}: "
                f"total {processor.total_processed()} items processed, "
                f"remaining {processor.remaining()} on processor"
            )


def main() -> None:
    print("=== Code Nexus - Data Stream ===")

    ds = DataStream()
    ds.print_processors_stats()

    numeric = NumericProcessor()
    print("Registering Numeric Processor")
    ds.register_processor(numeric)

    batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING", "log_message": "Telnetaccess!Usessh"},
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]

    print("Send first batch of data on stream:", batch)
    ds.process_stream(batch)
    ds.print_processors_stats()

    print("Registering other data processors")
    text = TextProcessor()
    log = LogProcessor()
    ds.register_processor(text)
    ds.register_processor(log)

    print("Send the same batch again")
    ds.process_stream(batch)
    ds.print_processors_stats()

    print("Consumesomeelementsfromthedataprocessors:Numeric3,Text2,Log 1")
    for _ in range(3):
        print("Numeric:", numeric.output())
    for _ in range(2):
        print("Text:", text.output())
    for _ in range(1):
        print("Log:", log.output())

    ds.print_processors_stats()


if __name__ == "__main__":
    main()
