import setuptools
with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

__version__="0.0.0"
REPO_NAME = "Portfolio-Projects"
AUTHOR_USER_NAME="riteshpatil310197"
SRC_REPO = "Portfolio-Projects"
AUTHOR_EMAIL = "patil.ritesh311@gmail.com"

setuptools.setup(name=SRC_REPO,
    author=AUTHOR_USER_NAME,
    version=__version__,
    author_email=AUTHOR_EMAIL,
    description="A small Python Package",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url=f"https://www.github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker" : f"https://www.github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where = "src"))
