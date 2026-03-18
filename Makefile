.PHONY: typing lint

typing:
	mypy challenges/

lint:
	ruff check challenges/
