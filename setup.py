import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open(".VERSION", "r") as ver:
    version = ver.readlines()[-1]
    print(version)

setuptools.setup(
    name="eve_optimizer", 
    version=version,
    author="Ajay Uppili Arasanipalai",
    author_email="ajayuppili@gmail.com",
    description="The EVer Evolving Optimizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iyaja/eve",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
