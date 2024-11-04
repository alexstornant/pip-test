from setuptools import setup

# Read requirements from requirements.txt
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="magnavision",
    version="0.1",
    packages=['logger'],
    install_requires=requirements,  # Add dependencies if needed
    description="desc: magnavision",
    author="Alex",
    author_email="stornant.alex@gmail.com",
    url="https://github.com/alexstornant/pip-test/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
