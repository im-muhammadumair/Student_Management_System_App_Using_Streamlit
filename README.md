# Student Management System App in Python Using Streamlit and pandas

This is a simple student management system built using Streamlit. It allows you to view, add, edit, and remove student records stored in a CSV file.

## Features

- **View Students:** Display the list of all students info.
- **Add Student:** Add a new student info to the database.
- **Edit Student:** Edit the info of an existing student.
- **Remove Student:** Remove a student info from the database.
- **Exit:** Close the application.
- **Work as Local Database:** It will save student info for lifetime

## Prerequisites

- Python 3.7 or higher
- Streamlit
- Pandas
- Pillow (PIL)

## Installation
1. **Clone the repository:**
```sh
    git clone https://github.com/im-muhammadumair/Student_Management_System_App_Using_Streamlit.git
    cd Student_Management_System_App_Using_Streamlit

```

2. If you have a `Virtual Environment` then make sure active it before install packages or Otherwise you can move on second step:

    ```sh
    python -m venv env            # Making new virtual environment
    env\Scripts\activate          # Activating Virtual environment
    ```

3. Install Require packages from `requirements.txt`:

    ```sh
    pip install -r requirements.txt
    ```

4. Add your `logo.png` file to the project directory.

4. If you have already `students.csv` file then it will use it otherwise it will automatically make a new file named `students.csv` in project folder with the following columns:

    ```csv
    Name , Roll No , Department , Phone No , Address , City
    ```

## Usage

Run the Streamlit app:

```sh
    streamlit run code.py
    ```

