from setuptools import setup, find_packages

setup(
    name="alphabotzpy",
    version="0.1",
    packages=find_packages(),
    install_requires=["pyTelegramBotAPI", "requests"],
    description="Extended Telebot library with large file upload support up to 1 GB By @ThealphaBotz @Adarsh2626 on telegram.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="etrg9044@gmail.com",
    url="https://github.com/utkarshdubey2008/alphabotzpy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
