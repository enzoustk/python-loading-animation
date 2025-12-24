# Dynamic CLI Loading Animation

A lightweight, thread-based Python utility to display animated loading messages in the terminal. This tool allows you to run background tasks while providing visual feedback to the user, including the ability to **update the status message dynamically**.

## ✨ Features

* **Non-blocking:** Uses Python's `threading` to run the animation without stopping your main logic.
* **Context Manager Support:** Clean usage with the `with` statement.
* **Dynamic Updates:** Change the loading message on the fly (e.g., from "Downloading..." to "Processing...").
* **Auto-cleanup:** Automatically clears the terminal line when the task is finished.
* **Zero Dependencies:** Uses only Python standard libraries (`sys`, `time`, `threading`).

## 🚀 Quick Start

To use the loading animation in your project, simply copy the `loading_animation` function and its helper into your script.

```python
import time
from your_module import loading_animation

# Basic usage
with loading_animation("Initial task"):
    time.sleep(2)
    # The animation stops automatically after this block

# Dynamic message updates
with loading_animation("Preparing...") as status:
    time.sleep(1.5)
    
    status['message'] = "Downloading data"
    time.sleep(2)
    
    status['message'] = "Generating report"
    time.sleep(1.5)

print("Done!")

```

## 🛠️ How It Works

1. **Threading:** When the context manager starts, it spawns a daemon thread that handles the visual loop (`.`, `..`, `...`).
2. **Shared State:** It yields a dictionary (`status_data`). Since dictionaries are mutable, any changes you make to `status['message']` inside the `with` block are immediately visible to the animation thread.
3. **Terminal Control:** It uses the carriage return character (`\r`) to overwrite the current line and calculates padding to ensure that shorter messages cleanly overwrite longer ones.

## 📋 Requirements

* Python 3.6+