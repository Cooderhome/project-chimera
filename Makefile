setup:
	poetry install --no-root

test:
	poetry run pytest tests/

spec-check:
	@echo "Spec check not yet implemented."
