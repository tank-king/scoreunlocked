from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="scoreunlocked",
    version="0.0.2",
    description="This is a simple package for using the ScoreUnlocked Leaderboard System running at scoreunlocked.pythonanywhere.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["scoreunlocked"],
    package_dir={
        "scoreunlocked": "src",
    },
    author="Tank King",
    author_email="tankking9833@gmail.com",
    url="https://github.com/tank-king/scoreunlocked",
    install_requires=[
        "requests",
    ],
)
