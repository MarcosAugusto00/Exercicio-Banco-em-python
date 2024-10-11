from setuptools import setup, find_packages # type: ignore

with open("README.md", "r") as f:
    page_description = f.read()
    
setup(
    name="Banco",
    version="0.0.7",
    author="Marcos Augusto",
    author_email="marcosaugustolinodeoliveira@gmail.com",
    description="Um programa simulando uma agência bancaria",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MarcosAugusto00/Exercicio-Banco-em-python",
    packages=find_packages,
    python_requires=">=3.0",
)