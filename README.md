# Gym Member Management System

## Overview
The **Gym Member Management System** is a Python-based command-line application designed to manage gym memberships. It allows users to add, search, edit, delete, and display gym member information, with data persistently stored in a CSV file (`gym_members.csv`). The system provides a simple interface for gym administrators to track member details, including name, membership ID, and status (active or unactive).

## Features
- **Add Member**: Register a new member with name, membership ID, and status.
- **Search Member**: Search for members by name, ID, or status.
- **Show All Members**: Display all registered members.
- **Edit Member**: Update member name or status using their membership ID.
- **Delete Member**: Remove a member from the system using their membership ID.
- **Data Persistence**: Member data is saved to and loaded from a CSV file.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/gym-member-management-system.git
   cd gym-member-management-system
   ```

2. **Python Version**:
   Ensure you have Python 3.6 or higher installed. You can check your Python version with:
   ```bash
   python --version
   ```

3. **Install Dependencies**:
   This project uses only Python standard library modules (`time`, `os`, `csv`), so no additional dependencies are required. However, you can verify by installing dependencies (if any) from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the program:
   ```bash
   python gym.py
   ```

2. The main menu will display the following options:
   ```
   ----->Gym **REMO** Member Management System<-----
   1. Add Member
   2. Search Member
   3. Show All Members
   4. Edit Member
   5. Delete Member
   6. Exit
   ```

3. Enter a number (1–6) to select an option and follow the prompts to manage gym members.

### Example Workflow
- **Add a Member**: Choose option 1, enter the member’s name, ID, and status (active or unactive).
- **Search for a Member**: Choose option 2, select search type (name, ID, or status), and enter the search value.
- **Edit a Member**: Choose option 4, provide the member’s ID, and update their name or status.

## File Structure
```
gym-member-management-system/
│
├── gym.py              # Main Python script for the Gym Management System
├── gym_members.csv     # CSV file for storing member data (created automatically)
├── README.md           # Project documentation
├── requirements.txt    # List of Python dependencies
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

## Contact
For any questions or suggestions, feel free to open an issue or contact the repository owner.