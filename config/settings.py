from __future__ import annotations

import os
from dataclasses import dataclass


class ConfigurationError(ValueError):
    """Raised when required runtime configuration is missing or invalid."""


@dataclass(frozen=True)
class Settings:
    environment: str
    log_level: str
    max_input_records: int
    measurement_limit: float
    default_target_cpk: float

    @classmethod
    def from_env(cls) -> "Settings":
        required = {k: os.getenv(k) for k in ("MQA_ENVIRONMENT", "MQA_LOG_LEVEL")}
        missing = [k for k,v in required.items() if not v]
        if missing:
            raise ConfigurationError(f"Missing required environment variables: {', '.join(missing)}")
        try:
            max_records = int(os.environ["MQA_MAX_INPUT_RECORDS"])
            limit = float(os.environ["MQA_MEASUREMENT_LIMIT"])
            target = float(os.environ["MQA_DEFAULT_TARGET_CPK"])
        except KeyError as exc:
            raise ConfigurationError(f"Missing required environment variable: {exc.args[0]}") from exc
        except ValueError as exc:
            raise ConfigurationError("Numeric runtime configuration contains an invalid value") from exc
        if max_records < 1 or limit <= 0 or target <= 0:
            raise ConfigurationError("Numeric runtime configuration must be positive")
        return cls(required["MQA_ENVIRONMENT"], required["MQA_LOG_LEVEL"], max_records, limit, target)
