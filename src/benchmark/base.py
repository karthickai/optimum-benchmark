from dataclasses import dataclass, MISSING
from abc import ABC, abstractmethod
from logging import getLogger
from typing import ClassVar


from src.input.base import InputGenerator
from src.backend.base import Backend

LOGGER = getLogger("benchmark")


@dataclass
class BenchmarkConfig(ABC):
    name: str = MISSING


class Benchmark(ABC):
    NAME: ClassVar[str]

    def __init__(self, model: str, task: str, device: str) -> None:
        self.model = model
        self.task = task
        self.device = device

    @abstractmethod
    def configure(self, config: BenchmarkConfig) -> None:
        raise NotImplementedError("Benchmark must implement configure method")

    @abstractmethod
    def populate(self, backend: Backend, input_generator: InputGenerator) -> None:
        raise NotImplementedError("Benchmark must implement populate method")