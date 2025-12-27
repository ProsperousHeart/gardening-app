# Makefile for Gardening App
# Uses uv for dependency and environment management

.PHONY: help lint format format-check test test-coverage clean install

help:
	@echo "Available commands:"
	@echo "  make install        - Install all dependencies with uv"
	@echo "  make lint           - Run flake8 linter on src/ and test/"
	@echo "  make format         - Format code with black"
	@echo "  make format-check   - Check code formatting without modifying"
	@echo "  make test           - Run pytest tests"
	@echo "  make test-coverage  - Run tests with coverage report"
	@echo "  make clean          - Remove cache and temporary files"

install:
	uv sync --all-groups

lint:
	uv run flake8 src/ tests/

format:
	uv run black src/ tests/

format-check:
	uv run black --check src/ tests/

test:
	uv run pytest tests/

test-v:
	uv run pytest -v tests/

test-coverage:
	uv run coverage run -m pytest tests/
	uv run coverage report
	uv run coverage html

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	rm -rf htmlcov/ .coverage 2>/dev/null || true
	@echo "Cleaned up cache and temporary files"
