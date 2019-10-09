init:
	pip3 install --no-cache-dir -r  requirements.txt

clean-deps:
	pip3 uninstall -y --no-cache-dir  -r requirements.txt

build:
	python3 setup.py build

install:
	python3 setup.py install

test:
	nosetests tests