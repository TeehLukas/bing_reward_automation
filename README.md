# Random Search Query Automation

This Python program performs automated search queries on Bing. It uses a list of search terms and randomly combines two terms to create a search query. The program then opens a new tab in the web browser, enters the search query, and performs the search.

The program is designed to take advantage of the Microsoft Bing Reward System, where daily rewards can be collected. There are a maximum of 90 rewards per day, and each query earns 3 coins. This program automates the reward collection process on a daily basis.

## Prerequisites

- Python 3.x
- `webbrowser` module (included in Python by default)
- `time` module (included in Python by default)
- `pyautogui` module (can be installed with `pip install pyautogui`)
- `random` module (included in Python by default)

## Installation

1. Ensure that Python 3.x is installed.
2. Install the `pyautogui` module with the following command:
   ```bash
   pip install pyautogui
