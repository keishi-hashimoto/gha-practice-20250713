from typing import Self, Any
from dataclasses import dataclass
from pathlib import Path
import json
import warnings


@dataclass
class DBClient:
    host: str
    port: int
    username: str
    password: str

    def __str__(self) -> str:
        dummy_password = "********"
        return f"{self.__class__.__name__}(host={self.host!r}, port={self.port!r}, username={self.username!r}, password={dummy_password!r})"

    @classmethod
    def from_config_file(cls, config_file_path: Path) -> Self:
        conf: dict[str, Any] = json.loads(config_file_path.read_text())
        host = conf.get("host")
        port = conf.get("port")
        username = conf.get("username")
        password = conf.get("password")
        if not host or not port or not username or not password:
            warnings.warn("Some parameters are empty")

        return cls(host=host, port=port, username=username, password=password)  # type: ignore


def main():
    client = DBClient.from_config_file(Path("./sample.json"))
    print(client)


if __name__ == "__main__":
    main()
