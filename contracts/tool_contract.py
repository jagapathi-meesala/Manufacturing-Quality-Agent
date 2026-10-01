from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Mapping


class ToolValidationError(ValueError):
    """Raised when tool input violates the declared contract."""


@dataclass(frozen=True)
class ToolMetadata:
    name: str
    description: str
    input_schema: Mapping[str, Any]


@dataclass(frozen=True)
class ToolResult:
    ok: bool
    tool: str
    output: Mapping[str, Any] = field(default_factory=dict)
    error: str | None = None


class ToolContract(ABC):
    metadata: ToolMetadata

    def validate(self, inputs: Mapping[str, Any]) -> None:
        if not isinstance(inputs, Mapping):
            raise ToolValidationError("Tool input must be an object/map")

    @abstractmethod
    def execute(self, inputs: Mapping[str, Any]) -> ToolResult:
        raise NotImplementedError

    def run(self, inputs: Mapping[str, Any]) -> ToolResult:
        try:
            self.validate(inputs)
            result = self.execute(inputs)
            if not isinstance(result, ToolResult):
                raise TypeError("Tool implementation returned an invalid result")
            return result
        except ToolValidationError as exc:
            return ToolResult(False, self.metadata.name, error=f"validation_error: {exc}")
        except (TypeError, ValueError, KeyError) as exc:
            return ToolResult(False, self.metadata.name, error=f"execution_error: {exc}")
