import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    # long_description = fh.read()
    long_description = "Long description"

setuptools.setup(
    name="Graph-Quest-madnug35",
    version="0.0.1",
    author="Mike Yannuzzi, Cherish, Nithin",
    author_email="madnug35@gmail.com",
    description="Graph Quest is a graph manipulation and visualization tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/myannuzzi/COSC-4353-Group-B.git",
    project_urls={
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)