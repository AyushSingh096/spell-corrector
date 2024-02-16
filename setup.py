from setuptools import setup

__version__ = "0.0.0"

AUTHOR_USER_NAME = "ayush"
SRC_REPO = "spell-corrector"
AUTHOR_EMAIL = "ayushsingh00112233@gmail.com"


setup(
    name = SRC_REPO,
    version= __version__
    description="A small package for spell-corrector that correcting the spelling and grammer"
    long_description=readme + "\n\n" + changelog,
    long_description_content_type="text/markdown",
    author=AUTHOR_USER_NAME
    author_email=AUTHOR_EMAIL
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    packages=packages,
    package_data={"symspellpy": ["frequency_dictionary_en_82_765.txt",
                                 "frequency_bigramdictionary_en_243_342.txt"]},
    package_dir={"symspellpy": "symspellpy"},
    include_package_data=True,
    python_requires=">=3.4",
    install_requires=requires,
)
