import streamlit as st  
import pandas as pd  
from PIL import Image
import os

# Wide Screen applier
st.set_page_config(layout="wide")

CSV_FILE = 'students.csv'
COLUMNS = ['Name', 'Roll No', 'Department', 'Phone No', 'Address', 'City']

# Load data -->
def load_data():
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE, dtype=str)
    else:
        return pd.DataFrame(columns=COLUMNS)

# Save data -->
def save_data(df):
    df.to_csv(CSV_FILE, index=False)

# Clean roll number -->
def clean_roll_no(roll_no):
    return roll_no.strip().lower()

# Header Columns -->
col1, col2, col3 = st.columns([1, 2, 2])
cols1, cols2, col3 = st.columns([1, 2, 2])

with col1:
    img = Image.open("logo.png")
    st.image(img, width=1000)

# Sidebar Menu -->
st.sidebar.title("Menu")
options = ["View Students", "Add Student", "Edit Student", "Remove Student", "Exit"]
choice = st.sidebar.selectbox("Choose an option", options)

# Load existing data -->
data = load_data()

# (i): Display Students -->
if choice == "View Students":
    st.subheader("View Students")
    st.write(data)

# (ii): Add Students -->
elif choice == "Add Student":
    with cols2:
        st.subheader("Add Student")
        with st.form(key='add_student_form'):
            name = st.text_input("Name")
            roll_no = st.text_input("Roll No")
            department = st.text_input("Department")
            phone_no = st.text_input("Phone No")
            address = st.text_input("Address")
            city = st.text_input("City")
            submit_button = st.form_submit_button(label='Add Student')

        if submit_button:
            if name and roll_no and phone_no and address and city and department:
                clean_roll = clean_roll_no(roll_no)
                new_student = pd.DataFrame([[name, clean_roll, department, phone_no, address, city]], columns=COLUMNS)
                data = pd.concat([data, new_student], ignore_index=True)
                save_data(data)
                st.success("Student added successfully")
            else:
                st.error("Please fill in all fields")

# (iii): Edit Students -->
elif choice == "Edit Student":
    with cols2:
        st.subheader("Edit Student")
        roll_no_to_edit = st.text_input("Enter Roll No of student to edit")

        if roll_no_to_edit:
            clean_roll_to_edit = clean_roll_no(roll_no_to_edit)
            student = data[data['Roll No'].str.strip().str.lower() == clean_roll_to_edit]
            if not student.empty:
                with st.form(key='edit_student_form'):
                    name = st.text_input("Name", student.iloc[0]['Name'])
                    department = st.text_input("Department", student.iloc[0]['Department'])
                    phone_no = st.text_input("Phone No", student.iloc[0]['Phone No'])
                    address = st.text_input("Address", student.iloc[0]['Address'])
                    city = st.text_input("City", student.iloc[0]['City'])
                    submit_button = st.form_submit_button(label='Edit Student')

                if submit_button:
                    if name and phone_no and address and city and department:
                        data.loc[data['Roll No'].str.strip().str.lower() == clean_roll_to_edit, 'Name'] = name
                        data.loc[data['Roll No'].str.strip().str.lower() == clean_roll_to_edit, 'Department'] = department
                        data.loc[data['Roll No'].str.strip().str.lower() == clean_roll_to_edit, 'Phone No'] = phone_no
                        data.loc[data['Roll No'].str.strip().str.lower() == clean_roll_to_edit, 'Address'] = address
                        data.loc[data['Roll No'].str.strip().str.lower() == clean_roll_to_edit, 'City'] = city
                        save_data(data)
                        st.success("Student details updated successfully")
                    else:
                        st.error("Please fill in all fields")
            else:
                st.error("Student not found")

# (iv): Remove Students -->
elif choice == "Remove Student":
    with cols2:
        st.subheader("Remove Student")
        roll_no_to_remove = st.text_input("Enter Roll No of student to remove")

        if roll_no_to_remove:
            clean_roll_to_remove = clean_roll_no(roll_no_to_remove)
            if clean_roll_to_remove in data['Roll No'].str.strip().str.lower().values:
                data = data[data['Roll No'].str.strip().str.lower() != clean_roll_to_remove]
                save_data(data)
                st.success("Student removed successfully")
            else:
                st.error("Student not found")

# (v): Exit APP -->
elif choice == "Exit":
    with cols2:
        st.subheader("Exit Application")
        st.write("You can now close the browser tab to exit the application.")

# Footer
st.markdown("___")
st.success('Developed by Muhammad Umair [Click to see More](https://github.com/im-muhammadumair) - © 2024')