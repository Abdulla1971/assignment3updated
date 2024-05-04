import pickle
import tkinter as tk

class Employee:
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details, manager_id=None):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.date_of_birth = date_of_birth
        self.passport_details = passport_details
        self.manager_id = manager_id

    @staticmethod
    def add_employee(master):
        # Function to save the details of a new employee
        def save_employee():
            # Retrieve employee details from entry fields
            name = name_entry.get()
            employee_id = employee_id_entry.get()
            department = department_entry.get()
            job_title = job_title_entry.get()
            basic_salary = basic_salary_entry.get()
            age = age_entry.get()
            date_of_birth = dob_entry.get()
            passport_details = passport_entry.get()
            manager_id = manager_id_entry.get()

            # Create an Employee instance with the provided details
            new_employee = Employee(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details, manager_id)

            # Save the employee data to a pickle file
            with open("company_staff.pkl", "ab") as file:
                pickle.dump(new_employee, file)

            # Close the employee window
            employee_window.destroy()

        # Create the employee window
        employee_window = tk.Toplevel(master)
        employee_window.title("Add Employee")
        employee_window.geometry("510x300")
        employee_window.configure(bg="#f0f0f0")

        # Employee details labels and entry fields
        tk.Label(employee_window, text="Name:", bg="#f0f0f0").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        name_entry = tk.Entry(employee_window)
        name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(employee_window, text="Employee ID:", bg="#f0f0f0").grid(row=1, column=0, sticky="e", padx=10, pady=5)
        employee_id_entry = tk.Entry(employee_window)
        employee_id_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(employee_window, text="Department:", bg="#f0f0f0").grid(row=2, column=0, sticky="e", padx=10, pady=5)
        department_entry = tk.Entry(employee_window)
        department_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(employee_window, text="Job Title:", bg="#f0f0f0").grid(row=3, column=0, sticky="e", padx=10, pady=5)
        job_title_entry = tk.Entry(employee_window)
        job_title_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(employee_window, text="Basic Salary:", bg="#f0f0f0").grid(row=4, column=0, sticky="e", padx=10, pady=5)
        basic_salary_entry = tk.Entry(employee_window)
        basic_salary_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(employee_window, text="Age:", bg="#f0f0f0").grid(row=0, column=2, sticky="e", padx=10, pady=5)
        age_entry = tk.Entry(employee_window)
        age_entry.grid(row=0, column=3, padx=10, pady=5)

        tk.Label(employee_window, text="Date of Birth:", bg="#f0f0f0").grid(row=1, column=2, sticky="e", padx=10, pady=5)
        dob_entry = tk.Entry(employee_window)
        dob_entry.grid(row=1, column=3, padx=10, pady=5)

        tk.Label(employee_window, text="Passport Details:", bg="#f0f0f0").grid(row=2, column=2, sticky="e", padx=10, pady=5)
        passport_entry = tk.Entry(employee_window)
        passport_entry.grid(row=2, column=3, padx=10, pady=5)

        tk.Label(employee_window, text="Manager ID:", bg="#f0f0f0").grid(row=3, column=2, sticky="e", padx=10, pady=5)
        manager_id_entry = tk.Entry(employee_window)
        manager_id_entry.grid(row=3, column=3, padx=10, pady=5)

        # Button frame
        button_frame = tk.Frame(employee_window, bg="#f0f0f0")
        button_frame.grid(row=5, columnspan=4, pady=10)

        # Create buttons with same width
        button_width = 20

        # Define button colors
        button_bg_color = "#343a40"  # Charcoal gray
        button_fg_color = "yellow"

        # Button to save the employee data
        save_button = tk.Button(button_frame, text="Save", command=save_employee, width=button_width, bg=button_bg_color, fg=button_fg_color)
        save_button.grid(row=0, column=0, padx=10, pady=5)
    
    @staticmethod
    def del_employee(master):
        # Function to delete an employee from the records
        def delete_employee():
            employee_id = employee_id_entry.get()
            employees = []  # Initialize an empty list to store employee data

            # Read employee data from the pickle file into a list
            with open("company_staff.pkl", "rb") as file:
                while True:
                    try:
                        emp = pickle.load(file)
                        employees.append(emp)
                    except EOFError:
                        break

            # Filter out the employee with the given ID
            filtered_employees = [emp for emp in employees if emp.employee_id != employee_id]

            # Write the filtered employees back to the file
            with open("company_staff.pkl", "wb") as file:
                for emp in filtered_employees:
                    pickle.dump(emp, file)

            # Close the delete window
            delete_window.destroy()

        # Create the delete window
        delete_window = tk.Toplevel(master)
        delete_window.title("Delete Employee")
        delete_window.geometry("250x100")
        delete_window.configure(bg="#f0f0f0")

        # Button frame
        button_frame = tk.Frame(delete_window, bg="#f0f0f0")
        button_frame.grid(row=5, columnspan=4, pady=10)

        # Create buttons with same width
        button_width = 20

        # Define button colors
        button_bg_color = "#343a40"  # Charcoal gray
        button_fg_color = "yellow"

        # Employee ID label and entry field
        tk.Label(delete_window, text="Employee ID:", bg="#f0f0f0").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        employee_id_entry = tk.Entry(delete_window)
        employee_id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Button to delete the employee
        delete_button = tk.Button(delete_window, text="Delete", command=delete_employee, width=button_width, bg=button_bg_color, fg=button_fg_color)
        delete_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

    @staticmethod
    def edit_employee(master):
        # Function to retrieve employee details based on ID
        def edit_employee_details():
            employee_id = employee_id_entry.get()
            # Read employee data from the pickle file
            with open("company_staff.pkl", "rb") as file:
                while True:
                    try:
                        emp = pickle.load(file)
                        if emp.employee_id == employee_id:
                            # Display employee details in entry fields
                            name_var.set(emp.name)
                            department_var.set(emp.department)
                            job_title_var.set(emp.job_title)
                            salary_var.set(emp.basic_salary)
                            age_var.set(emp.age)
                            dob_var.set(emp.date_of_birth)
                            passport_var.set(emp.passport_details)
                            manager_id_var.set(emp.manager_id)
                            break
                    except EOFError:
                        break

        # Function to save the edited employee details
        def save_changes():
            # Get updated employee details from entry fields
            name = name_entry.get()
            department = department_entry.get()
            job_title = job_title_entry.get()
            basic_salary = basic_salary_entry.get()
            age = age_entry.get()
            date_of_birth = dob_entry.get()
            passport_details = passport_entry.get()
            manager_id = manager_id_entry.get()

            # Create an Employee instance with updated details
            updated_employee = Employee(name, employee_id_entry.get(), department, job_title, basic_salary, age, date_of_birth, passport_details, manager_id)

            # Read existing employee data from the pickle file
            employees = []
            with open("company_staff.pkl", "rb") as file:
                while True:
                    try:
                        emp = pickle.load(file)
                        if emp.employee_id == employee_id_entry.get():
                            employees.append(updated_employee)  # Replace the existing employee with updated details
                        else:
                            employees.append(emp)
                    except EOFError:
                        break

            # Write the updated employee data back to the file
            with open("company_staff.pkl", "wb") as file:
                for emp in employees:
                    pickle.dump(emp, file)

            # Close the edit window
            edit_window.destroy()

        # Create the edit window
        edit_window = tk.Toplevel(master)
        edit_window.title("Edit Employee")
        edit_window.geometry("510x300")
        edit_window.configure(bg="#f0f0f0")

        # Employee ID label and entry field
        tk.Label(edit_window, text="Employee ID:", bg="#f0f0f0").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        employee_id_entry = tk.Entry(edit_window)
        employee_id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Button to retrieve employee details
        retrieve_button = tk.Button(edit_window, text="Retrieve Details", command=edit_employee_details, bg="#343a40", fg="yellow")
        retrieve_button.grid(row=0, column=2, padx=10, pady=5)

        # Employee details labels and entry fields
        tk.Label(edit_window, text="Name:", bg="#f0f0f0").grid(row=1, column=0, sticky="e", padx=10, pady=5)
        name_entry = tk.Entry(edit_window)
        name_entry.grid(row=1, column=1, padx=10, pady=5)
        name_var = tk.StringVar()
        name_var.set("")  # Initialize as empty string
        tk.Label(edit_window, textvariable=name_var, bg="#f0f0f0").grid(row=1, column=2, padx=10, pady=5)

        tk.Label(edit_window, text="Department:", bg="#f0f0f0").grid(row=2, column=0, sticky="e", padx=10, pady=5)
        department_entry = tk.Entry(edit_window)
        department_entry.grid(row=2, column=1, padx=10, pady=5)
        department_var = tk.StringVar()
        department_var.set("")  # Initialize as empty string
        tk.Label(edit_window, textvariable=department_var, bg="#f0f0f0").grid(row=2, column=2, padx=10, pady=5)

        tk.Label(edit_window, text="Job Title:", bg="#f0f0f0").grid(row=3, column=0, sticky="e", padx=10, pady=5)
        job_title_entry = tk.Entry(edit_window)
        job_title_entry.grid(row=3, column=1, padx=10, pady=5)
        job_title_var = tk.StringVar()
        job_title_var.set("")  # Initialize as empty string
        tk.Label(edit_window, textvariable=job_title_var, bg="#f0f0f0").grid(row=3, column=2, padx=10, pady=5)

        tk.Label(edit_window, text="Basic Salary:", bg="#f0f0f0").grid(row=4, column=0, sticky="e", padx=10, pady=5)
        basic_salary_entry = tk.Entry(edit_window)
        basic_salary_entry.grid(row=4, column=1, padx=10, pady=5)
        salary_var = tk.StringVar()
        salary_var.set("")  # Initialize as empty string
        tk.Label(edit_window, textvariable=salary_var, bg="#f0f0f0").grid(row=4, column=2, padx=10, pady=5)

        tk.Label(edit_window, text="Age:", bg="#f0f0f0").grid(row=5, column=0, sticky="e", padx=10, pady=5)
        age_entry = tk.Entry(edit_window)
        age_entry.grid(row=5, column=1, padx=10, pady=5)
        age_var = tk.StringVar()
        age_var.set("")  # Initialize as empty string
        tk.Label(edit_window, textvariable=age_var, bg="#f0f0f0").grid(row=5, column=2, padx=10, pady=5)

        tk.Label(edit_window, text="Date of Birth:", bg="#f0f0f0").grid(row=6, column=0, sticky="e", padx=10, pady=5)
        dob_entry = tk.Entry(edit_window)
        dob_entry.grid(row=6, column=1, padx=10, pady=5)
        dob_var = tk.StringVar()
        dob_var.set("")  # Initialize as empty string
        tk.Label(edit_window, textvariable=dob_var, bg="#f0f0f0").grid(row=6, column=2, padx=10, pady=5)

        tk.Label(edit_window, text="Passport Details:", bg="#f0f0f0").grid(row=7, column=0, sticky="e", padx=10, pady=5)
        passport_entry = tk.Entry(edit_window)
        passport_entry.grid(row=7, column=1, padx=10, pady=5)
        passport_var = tk.StringVar()
        passport_var.set("")  # Initialize as empty string
        tk.Label(edit_window, textvariable=passport_var, bg="#f0f0f0").grid(row=7, column=2, padx=10, pady=5)

        tk.Label(edit_window, text="Manager ID:", bg="#f0f0f0").grid(row=8, column=0, sticky="e", padx=10, pady=5)
        manager_id_entry = tk.Entry(edit_window)
        manager_id_entry.grid(row=8, column=1, padx=10, pady=5)
        manager_id_var = tk.StringVar()
        manager_id_var.set("")  # Initialize as empty string
        tk.Label(edit_window, textvariable=manager_id_var, bg="#f0f0f0").grid(row=8, column=2, padx=10, pady=5)

        # Button frame
        button_frame = tk.Frame(edit_window, bg="#f0f0f0")
        button_frame.grid(row=9, columnspan=3, pady=10)

        # Create buttons with same width
        button_width = 20

        # Define button colors
        button_bg_color = "#343a40"  # Charcoal gray
        button_fg_color = "yellow"

        # Button to save the changes
        save_button = tk.Button(button_frame, text="Save Changes", command=save_changes, width=button_width, bg=button_bg_color, fg=button_fg_color)
        save_button.grid(row=0, column=0, padx=10, pady=5)

    @staticmethod
    def show(master):
        def show_employee_details():
            # Retrieve employee details based on employee ID
            employee_id = employee_id_entry.get()
            employee_details = None

            # Read employee data from the pickle file
            with open("company_staff.pkl", "rb") as file:
                while True:
                    try:
                        emp = pickle.load(file)
                        if emp.employee_id == employee_id:
                            employee_details = emp
                            break
                    except EOFError:
                        break
            
            if employee_details:
                # Display employee details
                name_var.set(employee_details.name)
                dept_var.set(employee_details.department)
                job_title_var.set(employee_details.job_title)
                salary_var.set(employee_details.basic_salary)
                age_var.set(employee_details.age)
                dob_var.set(employee_details.date_of_birth)
                passport_var.set(employee_details.passport_details)
                manager_id_var.set(employee_details.manager_id)
            else:
                # If employee ID not found, show error message
                result_label.config(text="Employee ID not found!", fg="red")

        display_window = tk.Toplevel(master)
        display_window.title("Display Employees")
        display_window.geometry("510x320")
        display_window.configure(bg="#f0f0f0")

        # Employee ID label and entry field
        tk.Label(display_window, text="Employee ID:", bg="#f0f0f0").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        employee_id_entry = tk.Entry(display_window)
        employee_id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Button to show employee details
        show_button = tk.Button(display_window, text="Show Details", command=show_employee_details, bg="#343a40", fg="yellow")
        show_button.grid(row=0, column=2, padx=10, pady=5)

        # Employee details labels and variables
        name_var = tk.StringVar()
        dept_var = tk.StringVar()
        job_title_var = tk.StringVar()
        salary_var = tk.StringVar()
        age_var = tk.StringVar()
        dob_var = tk.StringVar()
        passport_var = tk.StringVar()
        manager_id_var = tk.StringVar()

        tk.Label(display_window, text="Name:", bg="#f0f0f0").grid(row=1, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=name_var, bg="#f0f0f0").grid(row=1, column=1, padx=10, pady=5)

        tk.Label(display_window, text="Department:", bg="#f0f0f0").grid(row=2, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=dept_var, bg="#f0f0f0").grid(row=2, column=1, padx=10, pady=5)

        tk.Label(display_window, text="Job Title:", bg="#f0f0f0").grid(row=3, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=job_title_var, bg="#f0f0f0").grid(row=3, column=1, padx=10, pady=5)

        tk.Label(display_window, text="Basic Salary:", bg="#f0f0f0").grid(row=4, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=salary_var, bg="#f0f0f0").grid(row=4, column=1, padx=10, pady=5)

        tk.Label(display_window, text="Age:", bg="#f0f0f0").grid(row=5, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=age_var, bg="#f0f0f0").grid(row=5, column=1, padx=10, pady=5)

        tk.Label(display_window, text="Date of Birth:", bg="#f0f0f0").grid(row=6, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=dob_var, bg="#f0f0f0").grid(row=6, column=1, padx=10, pady=5)

        tk.Label(display_window, text="Passport Details:", bg="#f0f0f0").grid(row=7, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=passport_var, bg="#f0f0f0").grid(row=7, column=1, padx=10, pady=5)

        tk.Label(display_window, text="Manager ID:", bg="#f0f0f0").grid(row=8, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=manager_id_var, bg="#f0f0f0").grid(row=8, column=1, padx=10, pady=5)

        # Result label to display error messages
        result_label = tk.Label(display_window, text="", bg="#f0f0f0", fg="red")
        result_label.grid(row=9, columnspan=3, padx=10, pady=5)