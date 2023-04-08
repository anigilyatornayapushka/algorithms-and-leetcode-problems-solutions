import typing as t
import json
import os


class Redis:
    """Custom redis. Working

    with text files."""

    _AllowedType = str | int | float | bool

    def __init__(self, name: str) -> None:
        """Initialization."""
        self.name: str = name+'.txt'
        if not os.path.isfile(self.name):
            open(self.name, 'w+')

    @property
    def ping(self) -> None:
        """Returns pong :)."""
        print('pong')
        return True

    @property
    def length(self) -> int:
        """Length of database."""
        with open(self.name, 'r') as f:
            count: int = f.read().count('$KEY$')
        return count

    def check_err_val_and_key(self, key: t.Any, val: t.Any) -> bool:
        """Check if there forbidden words
        
        ``$KEY$`` ``$VAL$`` in key and value."""
        if '$VAL$' in key or '$VAL$' in val:
            return True
        if '$KEY$' in key or '$KEY$' in val:
            return True
        return False

    def convert_lines_to_dict(self, lines) -> dict:
        """Convert string to dict."""
        lines: list[str] = lines.split('$KEY$ ')[1:]

        i: int
        for i in range(len(lines)):
            lines[i] = lines[i].split('$VAL$ ')

        data: dict = {}
        k: str
        v: str
        for k, v in lines:
            data[k[:-1]] = v[:-1]

        return data

    def convert_dict_to_lines(self, data) -> str:
        """Convert dict to string."""
        lines: str = ""
        for key in data:
            lines += f'$KEY$ {key}\n'
            lines += f'$VAL$ {data[key]}\n'
        return lines

    def set(self, key: t.Any, val: t.Any) -> None:
        """Set string value by key."""
        key: str = str(key)
        val: str = str(val)

        if self.check_err_val_and_key(key, val):
            return

        with open(self.name, 'r') as f:
            lines: str = f.read()

        data: dict = self.convert_lines_to_dict(lines)
        data[key] = val
        lines: str = self.convert_dict_to_lines(data)

        with open(self.name, 'w') as f:
            f.write(lines)

    def get(self, key: t.Any, typ: _AllowedType = str) -> _AllowedType:
        """Get value by key."""
        key: str = str(key)

        if typ not in (str, int, float, bool):
            raise TypeError('type muse be bool | int | float | str')

        with open(self.name, 'r') as f:
            lines: str = f.read()

        data: dict = self.convert_lines_to_dict(lines)
        return typ(data.get(key))

    def json_set(self, key: t.Any, maps: dict) -> None:
        """Set json by key."""
        key: str = str(key)

        with open(self.name, 'r') as f:
            lines: str = f.read()

        data: dict = self.convert_lines_to_dict(lines)
        maps = json.dumps(maps)

        if self.check_err_val_and_key(key, maps):
            return

        data[key] = maps
        lines: str = self.convert_dict_to_lines(data)

        with open(self.name, 'w') as f:
            f.write(lines)

    def json_get(self, key: t.Any) -> dict:
        """Get json by key."""
        key: str = str(key)

        with open(self.name, 'r') as f:
            lines: str = f.read()

        data: dict = self.convert_lines_to_dict(lines)
        ret = data.get(key)
        return json.loads(ret)

    def delete(self, key: t.Any = None) -> None:
        """Delete db or field."""
        if key is None:
            open(self.name, 'w')
            return

        with open(self.name, 'r') as f:
            lines: str = f.read()

        data: dict = self.convert_lines_to_dict(lines)
        if data.get(key):
            del data[key]
        lines: str = self.convert_dict_to_lines(data)

        with open(self.name, 'w') as f:
            f.write(lines)
