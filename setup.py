from setuptools import find_packages, setup

setup(
    name="spritetools",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    entry_points="""
        [console_scripts]
        spritetools=spritetools:cli
    """,
)
