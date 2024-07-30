# Student Management System App in Python Using Streamlit and pandas

This is a simple student management system built using Streamlit. It allows you to view, add, edit, and remove student records stored in a CSV file.

## Features

- **View Students:** Display the list of all students.
- **Add Student:** Add a new student to the database.
- **Edit Student:** Edit the details of an existing student.
- **Remove Student:** Remove a student from the database.
- **Exit:** Close the application.

## Prerequisites

- Python 3.7 or higher
- Streamlit
- Pandas
- Pillow (PIL)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/your-username/student-management-system.git
    cd student-management-system
    ```

2. Install the required packages:

    ```sh
    pip install streamlit pandas pillow
    ```

3. Add your `logo.png` file to the project directory.

4. Create a `students.csv` file with the following columns if it doesn't already exist:

    ```csv
    Name,Roll No,Department,Phone No,Address,City
    ```

## Usage

Run the Streamlit app:

```sh
streamlit run app.py