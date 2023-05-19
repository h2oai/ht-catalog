run:
	./venv/bin/wave run src.app


.PHONY: format
format:
	./venv/bin/black ./src


.PHONY: lint
lint:
	./venv/bin/flake8 ./src
