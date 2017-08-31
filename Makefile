.PHONY: rst check build install upload 

rst:
	pandoc --from=markdown --to=rst --output=README.rst README.md

check:
	python setup.py check

build: clean
	python setup.py bdist_wheel --universal

upload: build
	twine upload dist/*

install:
	sudo python setup.py install

uninstall:
	sudo python setup.py install --record=/tmp/filelist
	cat /tmp/filelist | sudo xargs rm -rf

clean:
	rm -rf dist/*

distclean:
	sudo rm -rf build dist youdao_simple.egg-info

