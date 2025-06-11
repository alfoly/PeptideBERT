from setuptools import setup, find_packages

setup(
    name="PeptideBERT",
    version="0.1.0",
    description="A Python package for peptide analysis using BERT-based models.",
    author="alfoly",
    author_email="",
    url="https://github.com/alfoly/PeptideBERT",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        # Add main dependencies here, e.g.:
        # "torch>=1.9.0",
        # "transformers>=4.0.0",
        # "numpy>=1.18.0",
    ],
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="peptide BERT bioinformatics machine-learning",
)
