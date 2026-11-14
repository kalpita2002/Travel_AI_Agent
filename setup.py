
from setuptools import find_packages, setup
from typing import List


def get_requirements() -> List[str]:
    """
    This function returns a list of requirements.
    """

    requirement_list: List[str] = []

    try:
        # Open and read the requirements.txt file
        with open("requirements.txt", "r") as file:

            # Read all lines from the file
            lines = file.readlines()

            # Process each line
            for line in lines:

                # Strip whitespace and newline characters
                requirement = line.strip()

                # Ignore empty lines and editable install reference
                if requirement and requirement != "-e .":
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found.")

    return requirement_list


setup(
    name="Travel_AI_Agent",
    version="0.0.1",
    author="Kalpita Chakraborty",
    author_email="kalpita27.136@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)