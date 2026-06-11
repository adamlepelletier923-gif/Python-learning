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

    def _is_valid_log_dict(
            self, data: dict[Any, Any]) -> bool:
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


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print("Testing Numeric Processor...")
    print("Trying to validate input '42':", numeric.validate(42))
    print("Trying to validate input 'Hello':", numeric.validate("Hello"))

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")  # type: ignore[arg-type]
    except ValueError as exc:
        print("Got exception:", exc)

    print("Processing data:", [1, 2, 3, 4.5])
    numeric.ingest([1, 2, 3, 4.5])
    print("Extracting 4 values...")
    for _ in range(4):
        rank, value = numeric.output()
        print(f"Numeric value {rank}: {value}")

    print("Testing Text Processor...")
    print("Trying to validate input '42':", text.validate(42))
    print("Processing data:", ["Hello", "Nexus", "World"])
    text.ingest(["Hello", "Nexus", "World"])
    print("Extracting 3 values...")
    for _ in range(3):
        rank, value = text.output()
        print(f"Text value {rank}: {value}")

    print("Testing Log Processor...")
    print("Trying to validate input 'Hello':", log.validate("Hello"))
    logs = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print("Processing data:", logs)
    log.ingest(logs)
    print("Extracting 2 values...")
    for _ in range(2):
        rank, value = log.output()
        print(f"Log entry {rank}: {value}")


if __name__ == "__main__":
    main()
