# search reviewer notes

## Architecture
A minimal Python command-line application centered in `app.py`. The pure `greet()` function is separated from interactive input/output in `main()`, with behavior covered by `test_app.py` using the standard-library `unittest` framework. The repository intentionally has no third-party dependencies.

## Conventions
- Keep reusable behavior in functions and keep CLI interaction in `main()` (`app.py`); `greet()` returns a string while `main()` handles `input()` and `print()`.
- Use type annotations and concise docstrings for public functions, as shown by `greet(name: str = "World") -> str` and `main() -> None` in `app.py`.
- Preserve the executable entry-point guard: `if __name__ == "__main__": main()` in `app.py` so importing the module does not start the CLI.
- Tests use `unittest`, subclass `unittest.TestCase`, and name methods with `test_...` (`test_app.py`). Run them with `python -m unittest`.
- Keep the project standard-library-only. `requirements.txt` explicitly documents that no packages are required.
- The default name is `"World"` both in `greet()` and when blank input is normalized in `main()` (`app.py`).

## Intentional non-standard choices
- There is no package layout or installation metadata; the application is deliberately a single top-level `app.py` script (`README.md`).
- Tests import directly with `from app import greet` rather than using a package-qualified import (`test_app.py`).

## Watch out for
- Do not move input handling into `greet()` or make `greet()` print directly; tests and the current separation depend on it returning exactly `"Hello, {name}!"`.
- Preserve `.strip() or "World"` in `main()` so whitespace-only input receives the documented default.
- Avoid adding third-party dependencies or changing the documented commands in `README.md` and `requirements.txt`.
- Update tests if greeting punctuation, capitalization, or default behavior changes; current assertions require exact output (`test_app.py`).