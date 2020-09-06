import setuptools

setuptools.setup(
    name="aioowm",
    version="1.0.0",
    author="vladislavkovalskyi",
    description="async OWM",
    url="https://github.com/vladislavkovalskyi/aioowm",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "aiohttp~=3.6.2",
        "pydantic~=1.6.1"
    ]
)
