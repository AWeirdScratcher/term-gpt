from setuptools import setup

setup(
  name="term-chatgpt",
  author="AWeirdDev",
  version="1.1.6",
  license="MIT License",
  description="Ask ChatGPT directly on your terminal! Fast & Free.",
  long_description=open("README.md", "r", encoding="utf-8").read(),
  long_description_content_type="text/markdown",
  author_email="aweirdscratcher@gmail.com",
  packages=['termgpt'],
  classifiers=[
    "Programming Language :: Python :: 3.10",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Environment :: Console",
  ],
  keywords=["chatgpt", "gpt", "free", "terminal", "textual", "rich", "chat-gpt", "ai"],
  entry_points={
    "console_scripts": [
      "term-gpt=termgpt.main:main"
    ]
  },
  install_requires=["rich", "textual", "requests", "questionary"]
)
