from dataclasses import dataclass


@dataclass
class Arg:
    name: str
    description: str
    required: bool


if __name__ == "__main__":
    arg = Arg(name="x", description="no description", required=True)
