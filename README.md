# Student Data Management System App using Streamlit

This is a professional and easy to use student data management system app built by using Streamlit and Pandas. It allows you to view, add, edit, and remove student records stored in a CSV file.

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

     Clone Github repository to your local_machine or Folder

    ```sh
    git clone https://github.com/im-muhammadumair/Student_Management_System_App_Using_Streamlit.git
    ```
    
     Move to inside the repository

    ```sh
    cd Student_Management_System_App_Using_Streamlit
    ```

2. If you have a `Virtual Environment` then make sure active it before install packages or Otherwise you can move on 3rd step:

     Making new virtual environment

    ```sh
    python -m venv env            
    ```

     Activating Virtual environment

    ```sh
    env\Scripts\activate          
    ```

3. Install Require packages from `requirements.txt`:

    ```sh
    pip install -r requirements.txt
    ```

4. Add your `logo.png` file to the project directory.


5. If you have already `students.csv` file then it will use it otherwise it will automatically make a new file named `students.csv` in project folder with the following columns:

    ```sh 
    Name , Roll No , Department , Phone No , Address , City
    ```

## Usage
6. **Run the Code**

    ```sh 
    streamlit run app.py
    ```

# License
This project is licensed under the MIT License.
