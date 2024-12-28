from setuptools import setup, find_packages

setup(
    name="nhabittracker",
    version="1.0.0",
    author="Apurba Nath",
    description="CLI tool for daily habit tracking with Notion",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/apurbzz-1994/notion_habit_tracker_cli",  # Link to your GitHub repo
    packages=find_packages(),
    install_requires=[
        "certifi==2024.12.14",
        "charset-normalizer==3.4.0",
        "idna==3.10",
        "python-dotenv==1.0.1",
        "requests==2.32.3",
        "setuptools==75.6.0",
        "urllib3==2.2.3",
        "pytz==2024.2"
    ],  # dependencies from requirements.txt file
    entry_points={
        "console_scripts": [
            "nhabittracker=nhabittracker.main:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)