"""Setup Configuration File."""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="victor_smart_kill",
    version="1.1.1",
    author="Tore Amundsen",
    author_email="tore@amundsen.org",
    description="A simple unofficial async Python wrapper for Victor Smart-Kill API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/toreamun/victor-smart-kill",
    packages=["victor_smart_kill"],
    package_data={"victor_smart_kill": ["py.typed"]},
    keywords=[
        "API",
        "Victor Smart-Kill",
        "VictorPest.com",
        "trap",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "httpx~=0.20",
        "marshmallow~=3.8",
        "marshmallow-dataclass[enum,union]~=8.1",
    ],
)
