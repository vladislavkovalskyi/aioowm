python setup.py sdist bdist_wheel
python -m pip install --upgrade twine
python -m twine upload dist/*