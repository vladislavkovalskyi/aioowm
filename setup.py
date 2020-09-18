import setuptools

setuptools.setup(
		name="aioowm",
		version="1.0.1",
		author="vladislavkovalskyi",
		description="Async OpenWeatherMap API!",
		url="https://github.com/vladislavkovalskyi/aioowm",
		license="MIT",
		packages=setuptools.find_packages(),
		author_email="v.darknesssb@gmail.com",
		classifiers=[
			"Programming Language :: Python :: 3.6",
			"Programming Language :: Python :: 3.7",
			"Operating System :: OS Independent",
		],
		install_requires=["aiohttp", "pydantic"]
)
