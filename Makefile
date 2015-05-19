develop:
	python setup.py develop

install:
	python setup.py install

test:
	py.test tests/

build:
	python setup.py sdist

upload: build
	scp ./dist/rmock-0.0.6.tar.gz 114:
	scp ./dist/rmock-0.0.6.tar.gz ali:
