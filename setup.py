import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="test_user", # Replace with your own username
    version="0.0.1",
    author="Author",
    author_email="author@example.com",
    description="short description",
    long_description="long description",
    long_description_content_type="text/markdown",
    url="https://github.com/nikeros1974/temp_user",
    install_requires=['temp_library @ https://github.com/nikeros1974/temp_library@master',],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)