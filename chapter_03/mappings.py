from typing import Any


class DefaultDict(dict):
    def __contains__(self, key: Any) -> bool:
        return key in self.keys() or str(key) in self.keys()

    def __missing__(self, key: Any):
        # This check is crucial to avoid endless loop from __getitem__()
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key: Any, default=None):
        try:
            return self[key]
        except KeyError:
            return default
