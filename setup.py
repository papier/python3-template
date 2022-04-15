import setuptools

setuptools.setup(
    name="project",
    version="1.0.0",
    description="Python3 sample project",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
)
