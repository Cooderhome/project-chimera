setup:
	poetry install --no-root

test:
	pytest tests/

spec-check:
	@echo "Spec check not yet implemented."
