.PHONY: check lint format

check:
	uv run ruff check .
	uv run ruff format --check .

lint:
	uv run ruff check .

format:
	uv run ruff check . --fix
	uv run ruff format .