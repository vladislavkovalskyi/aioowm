import setuptools

try:
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()
except UnicodeDecodeError:
    with open("README.md", "r") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ""

with open("aioowm/const/const.py") as f:
    exec(f.read())

setuptools.setup(
		name="aioowm",
		version=locals()["__version__"],
		author=locals()["__author__"],
		description="Async OpenWeatherMap API!",
		long_description=long_description,
		license="MIT",
		url="https://github.com/vladislavkovalskyi/aioowm",
		packages=setuptools.find_packages(),
		author_email="v.darknesssb@gmail.com",
		classifiers=[
			"Programming Language :: Python :: 3.6",
			"Programming Language :: Python :: 3.7",
			"Operating System :: OS Independent",
		],
		install_requires=["aiohttp", "pydantic"]
)
