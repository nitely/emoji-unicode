clean:
	rm -fr dist/ build/ *.egg-info/

docs:
	cd docs && make clean && make html

test:
	python runtests.py

gen:
	python ./build.py

bench:
	python ./benchmark.py

sdist: test clean
	python setup.py sdist

release: test clean
	python setup.py sdist upload

.PHONY: clean test sdist release docs gen bench
