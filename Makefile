.PHONY: rst check build install upload 

rst:
	pandoc --from=markdown --to=rst --output=README.rst README.md

check:
	python setup.py check

build:
	python setup.py bdist_wheel --universal

install:
	sudo python setup.py install

upload:
	twine upload dist/*


