# Keylogger Project

A simple keylogger built using Python. This keylogger logs keystrokes made by the user and stores them in a file. It can run in the background and is useful for learning how keylogging works for educational purposes. Please use this script responsibly and only on systems you own or have explicit permission to test.

## Features

- Logs keystrokes made by the user.
- Stores logs with timestamps in a text file.
- Runs in the background as a daemon.
- Optionally sends logs via email for remote monitoring.
- Configurable to stop the keylogger on pressing the "ESC" key.

## Installation

### Prerequisites

- Python 3.x
- **pynput** library for keyboard listening

### Step-by-Step Installation

1. **Clone the Repository**:

   Clone this repository to your local machine.

   ```bash
   git clone https://github.com/shanmukh-git7/keylogger.git
   cd keylogger
   
2.Create a Virtual Environment (Optional but recommended):

It's always a good idea to isolate dependencies.

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # For Linux/MacOS
.\venv\Scripts\activate   # For Windows

3.Install Dependencies:

Install the required Python libraries.

bash
Copy
Edit
pip install pynput

4.Run the Script:

Execute the keylogger script to start logging keystrokes.

bash
Copy
Edit
python keylogger.py

5.Run the Script:

Execute the keylogger script to start logging keystrokes.

bash
Copy
Edit
python keylogger.py


