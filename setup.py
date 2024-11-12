import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


_version_ = "0.0.0"

Repo_Name = "Jotter.ai"
Author_Name = "Dakshyashree"
SRC_REPO = "textSummerizer"
Author_Email = "dakshyashreejamwal@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=_version_,
    author=Author_Name,
    author_email=Author_Email,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{Author_Name}/{Repo_Name}",
    project_urls={
        "Bug Tracker": f"https://github.com/{Author_Name}/{Repo_Name}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)