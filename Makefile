VERSION = 3.5

run:
	python$(VERSION) classy.py

test:
	python$(VERSION) -m unittest -v test/*.py