# Reference: https://oclif.io/docs/flags
import re
from enum import Enum
from typing import Any
from pathlib2 import Path
from abc import abstractmethod, ABC


class Flag(ABC):
    def __init__(self, flag: str, char: str = None, description: str = '', required: bool = False, default: Any = None):
        self.flag = flag
        if char is not None and (len(char) != 1 or re.match(r'^\d$', char)):
            raise ValueError(f"char: {char} must be a single character")
        self.char = char
        self._value = default
        self.description = description
        self.required = required

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_val: Any):
        self._value = new_val

    @abstractmethod
    def parse(self):
        raise NotImplementedError


class IntegerFlag(Flag):
    def parse(self):
        return int(self.value)


class BooleanFlag(Flag):
    def __init__(self, flag: str, allow_no: bool = False, **kwargs):
        self.allow_no = allow_no
        super(BooleanFlag, self).__init__(flag, **kwargs)

    def parse(self):
        return bool(self.value)


class FloatFlag(Flag):
    def parse(self):
        return float(self.value)


class PathFlag(Flag):
    def __init__(self, flag: str, exists: bool = False, **kwargs):
        self.exists = exists
        super(PathFlag, self).__init__(flag, **kwargs)

    def parse(self) -> Path:
        path = Path(self.value).absolute()
        if self.exists and not path.exists():
            raise ValueError(f"Path {path} doesn't exist")
        return path


class DirectoryFlag(PathFlag):
    def parse(self) -> Path:
        path = super().parse()
        if not path.is_dir():
            raise ValueError(f"{self.value} is not a directory")
        return path


class FileFlag(PathFlag):
    def parse(self) -> Path:
        path = super().parse()
        if not path.is_file():
            raise ValueError(f"{self.value} is not a file")
        return path


class StringFlag(Flag):
    def parse(self) -> str:
        return self.value


class EnumFlag(Flag):
    def __init__(self, flag: str, enum: Enum = None, **kwargs):
        assert enum is not None, "enum should not be None"
        self.enum = enum
        super(EnumFlag, self).__init__(flag, **kwargs)

    def parse(self):
        return self.value


class Flags:
    @staticmethod
    def string(self, flag: str, **kwargs) -> StringFlag:
        return StringFlag(flag, **kwargs)

    @staticmethod
    def boolean(self, flag: str, allow_no: bool = False, **kwargs) -> BooleanFlag:
        # allowNo: boolean; e.g. --no-force
        return BooleanFlag(flag, allow_no, **kwargs)

    # @staticmethod
    # def custom(self):
    #     pass

    @staticmethod
    def directory(self, flag: str, exists: bool = False, **kwargs) -> DirectoryFlag:
        return DirectoryFlag(flag, exists, **kwargs)

    @staticmethod
    def enum(self, flag: str, enum: Enum, **kwargs) -> EnumFlag:
        return EnumFlag(flag, enum, **kwargs)

    @staticmethod
    def file(self, flag: str, exists: bool = False, **kwargs) -> FileFlag:
        return FileFlag(flag, exists, **kwargs)

    @staticmethod
    def path(self, flag: str, exists: bool = False, **kwargs) -> PathFlag:
        return PathFlag(flag, exists, **kwargs)

    # @staticmethod
    # def help(self):
    #     pass

    @staticmethod
    def integer(self, flag: str, **kwargs) -> IntegerFlag:
        return IntegerFlag(flag, **kwargs)

    @staticmethod
    def float(self, flag: str, **kwargs) -> FloatFlag:
        return FloatFlag(flag, **kwargs)

    # @staticmethod
    # def option(self):
    #     pass

    # @staticmethod
    # def url(self):
    #     pass

    # @staticmethod
    # def version(self):
    #     pass


if __name__ == "__main__":
    # iflag = IntegerFlag('c', '')
    # iflag.value = '1'
    # print(iflag.parse())
    # print(iflag.char)

    path_flag = PathFlag('root', exists=True)
    path_flag.value = '/home'
    print(path_flag.parse())

    file_flag = FileFlag('file', exists=True, default='/Users/huakun/Documents/Dev/ooarg/LICENSE')
    print(file_flag.parse())

    dir_flag = DirectoryFlag('dir', exists=True, default='/Users/huakun/Documents/Dev/ooarg')
    print(dir_flag.parse())
