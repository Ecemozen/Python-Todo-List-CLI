# CLI-Based Task Management System (To-Do List)

This repository features a robust, production-grade Command-Line Interface (CLI) Task Management application developed in Python. The project showcases fundamental software engineering principles, including file-based persistent data structures, advanced exception handling, and interactive terminal runtime execution loops.

The application manages task records systematically by executing full CRUD operations directly integrated with localized text database streams.

## Technical Capabilities and Architectural Highlights

* **Persistent Data Operations (File I/O):** Implements localized flat-file storage (`gorevler.txt`) using custom delimiters (`|`) and explicit `utf-8` text encoding structures to maintain cross-platform data persistence.
* **Defensive Programming & Exception Handling:** Employs systematic `try-except` wrappers targeting `ValueError`, `IndexError`, and `FileNotFoundError` scenarios to guarantee absolute operational uptime during runtime boundary failures.
* **Dynamic Data Mutations:** Organizes structured dictionaries inside structural dynamic arrays (lists) to handle custom data fields including task string logs, conditional flags, task urgency indices, and validation timestamps.
* **Console User Experience (UX):** Leverages enumerated loops and operational status icons (`✔️`/`✘`) to present intuitive, real-time diagnostic outputs to the terminal interface.

## Application Workflow and Logic Pipeline

1. **Initialization:** The program auto-scans the target filesystem for existing data, gracefully handling missing files by instantiating new local text matrices without throwing catastrophic failures.
2. **Data Serialization:** Object states (Boolean operational flags, metadata strings) are parsed into strings during persistent file writing operations and reconstructed back into memory matrices during file loading sequences.
3. **Menu Run-Loop:** Utilizes a persistent `while True` procedural application loop containing multi-conditional routing modules to orchestrate task management routines.

## Repository Structure

* `todo_manager.py`: Core production-ready Python script containing application business logic, custom UI rendering functions, and persistent file handler blocks.

## Execution and Setup

1. Clone the workspace layout directly into your local runtime environment:
   ```bash
   git clone [https://github.com/Ecemozen/Python-Todo-List-CLI.git](https://github.com/Ecemozen/Python-Todo-List-CLI.git)
