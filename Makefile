all:
	rm -rf build dist eve_*
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
	git add .
	git commit -m "chore: increment version"
	git push 
