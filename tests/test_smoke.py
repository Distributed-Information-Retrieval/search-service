import inspect

import search_service


def test_smoke() -> None:
    assert inspect.ismodule(search_service)
