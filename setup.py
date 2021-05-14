import setuptools


# get list of requirement strings from requirements.txt
def remove_whitespace(x):
    return "".join(x.split())


def sanitize(x):
    return not x.startswith("#") and x != ""


def requirements():
    with open("requirements.txt", "r") as f:
        r = f.readlines()
    map(remove_whitespace, r)
    filter(sanitize, r)
    return r


setuptools.setup(
    name="jsonsearch",
    version="0.0.2",
    author="sty945",
    author_email="sutaoyu@yeah.net",
    description="JsonSearch is a simple, yet effcient python library for searhing specific elements in json data.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sty945/jsonsearch",
    project_urls={
        "Bug Tracker": "https://github.com/sty945/jsonsearch/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    install_requires=requirements(),
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)