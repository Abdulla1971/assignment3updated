import pickle
import tkinter as tk

class Supplier:
    def __init__(self, supplier_id, name, address, contact, service_provided, min_guests, max_guests):
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.contact = contact
        self.service_provided = service_provided
        self.min_guests = min_guests
        self.max_guests = max_guests

    @staticmethod
    def add_supplier(master):
        # Function to handle adding a new supplier
        def save_supplier():
            # Retrieve data from entry fields
            supplier_id = supplier_id_entry.get()
            name = name_entry.get()
            address = address_entry.get()
            contact = contact_entry.get()
            service_provided = service_provided_entry.get()
            min_guests = min_guests_entry.get()
            max_guests = max_guests_entry.get()

            # Create a Supplier instance
            new_supplier = Supplier(supplier_id, name, address, contact, service_provided, min_guests, max_guests)

            # Save the supplier data to a pickle file
            with open("supplier_data.pkl", "ab") as file:
                pickle.dump(new_supplier, file)

            # Close the supplier window
            supplier_window.destroy()

        # Create a new window for adding a supplier
        supplier_window = tk.Toplevel(master)
        supplier_window.title("Add Supplier")
        supplier_window.geometry("510x300")
        supplier_window.configure(bg="#f0f0f0")

        # Supplier details labels and entry fields
        tk.Label(supplier_window, text="Supplier ID:", bg="#f0f0f0").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        supplier_id_entry = tk.Entry(supplier_window)
        supplier_id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(supplier_window, text="Name:", bg="#f0f0f0").grid(row=1, column=0, sticky="e", padx=10, pady=5)
        name_entry = tk.Entry(supplier_window)
        name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(supplier_window, text="Address:", bg="#f0f0f0").grid(row=2, column=0, sticky="e", padx=10, pady=5)
        address_entry = tk.Entry(supplier_window)
        address_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(supplier_window, text="Contact:", bg="#f0f0f0").grid(row=3, column=0, sticky="e", padx=10, pady=5)
        contact_entry = tk.Entry(supplier_window)
        contact_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(supplier_window, text="Service Provided:", bg="#f0f0f0").grid(row=4, column=0, sticky="e", padx=10, pady=5)
        service_provided_entry = tk.Entry(supplier_window)
        service_provided_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(supplier_window, text="Min Guests:", bg="#f0f0f0").grid(row=5, column=0, sticky="e", padx=10, pady=5)
        min_guests_entry = tk.Entry(supplier_window)
        min_guests_entry.grid(row=5, column=1, padx=10, pady=5)

        tk.Label(supplier_window, text="Max Guests:", bg="#f0f0f0").grid(row=6, column=0, sticky="e", padx=10, pady=5)
        max_guests_entry = tk.Entry(supplier_window)
        max_guests_entry.grid(row=6, column=1, padx=10, pady=5)

        # Button frame
        button_frame = tk.Frame(supplier_window, bg="#f0f0f0")
        button_frame.grid(row=7, columnspan=2, pady=10)

        # Create buttons with same width
        button_width = 20

        # Define button colors
        button_bg_color = "#343a40"  # Charcoal gray
        button_fg_color = "yellow"

        # Button to save the supplier data
        save_button = tk.Button(button_frame, text="Save", command=save_supplier, width=button_width, bg=button_bg_color, fg=button_fg_color)
        save_button.grid(row=0, column=0, padx=10, pady=5)

    @staticmethod
    def del_supplier(master):
        # Function to handle deleting a supplier
        def delete_supplier():
            # Get supplier ID from entry field
            supplier_id = supplier_id_entry.get()
            suppliers = []  # Initialize an empty list to store supplier data

            # Read supplier data from the pickle file into a list
            with open("supplier_data.pkl", "rb") as file:
                while True:
                    try:
                        sup = pickle.load(file)
                        suppliers.append(sup)
                    except EOFError:
                        break

            # Filter out the supplier with the given ID
            filtered_suppliers = [sup for sup in suppliers if sup.supplier_id != supplier_id]

            # Write the filtered suppliers back to the file
            with open("supplier_data.pkl", "wb") as file:
                for sup in filtered_suppliers:
                    pickle.dump(sup, file)

            # Close the delete window
            delete_window.destroy()

        # Create a window for deleting a supplier
        delete_window = tk.Toplevel(master)
        delete_window.title("Delete Supplier")
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

        # Supplier ID label and entry field
        tk.Label(delete_window, text="Supplier ID:", bg="#f0f0f0").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        supplier_id_entry = tk.Entry(delete_window)
        supplier_id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Button to delete the supplier
        delete_button = tk.Button(delete_window, text="Delete", command=delete_supplier, width=button_width, bg=button_bg_color, fg=button_fg_color)
        delete_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

    @staticmethod
    def edit_supplier(master):
        # Function to retrieve supplier details based on ID
        def edit_supplier_details():
            supplier_id = supplier_id_entry.get()
            # Read supplier data from the pickle file
            with open("supplier_data.pkl", "rb") as file:
                while True:
                    try:
                        supp = pickle.load(file)
                        if supp.supplier_id == supplier_id:
                            # Display supplier details in entry fields
                            name_var.set(supp.name)
                            address_var.set(supp.address)
                            contact_var.set(supp.contact)
                            service_provided_var.set(supp.service_provided)
                            min_guests_var.set(supp.min_guests)
                            max_guests_var.set(supp.max_guests)
                            break
                    except EOFError:
                        break

        # Function to save the edited supplier details
        def save_changes():
            # Get updated supplier details from entry fields
            name = name_entry.get()
            address = address_entry.get()
            contact = contact_entry.get()
            service_provided = service_provided_entry.get()
            min_guests = min_guests_entry.get()
            max_guests = max_guests_entry.get()

            # Create a Supplier instance with updated details
            updated_supplier = Supplier(supplier_id_entry.get(), name, address, contact, service_provided, min_guests, max_guests)

            # Read existing supplier data from the pickle file
            suppliers = []
            with open("supplier_data.pkl", "rb") as file:
                while True:
                    try:
                        supp = pickle.load(file)
                        if supp.supplier_id == supplier_id_entry.get():
                            suppliers.append(updated_supplier)  # Replace the existing supplier with updated details
                        else:
                            suppliers.append(supp)
                    except EOFError:
                        break

            # Write the updated supplier data back to the file
            with open("supplier_data.pkl", "wb") as file:
                for supp in suppliers:
                    pickle.dump(supp, file)

            # Close the edit window
            edit_window.destroy()

        # Create the edit window
        edit_window = tk.Toplevel(master)
        edit_window.title("Edit Supplier")
        edit_window.geometry("510x300")
        edit_window.configure(bg="#f0f0f0")

        # Supplier ID label and entry field
        tk.Label(edit_window, text="Supplier ID:", bg="#f0f0f0").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        supplier_id_entry = tk.Entry(edit_window)
        supplier_id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Button to retrieve supplier details
        retrieve_button = tk.Button(edit_window, text="Retrieve Details", command=edit_supplier_details, bg="#343a40", fg="yellow")
        retrieve_button.grid(row=0, column=2, padx=10, pady=5)

        # Supplier details labels and entry fields
        tk.Label(edit_window, text="Name:", bg="#f0f0f0").grid(row=1, column=0, sticky="e", padx=10, pady=5)
        name_entry = tk.Entry(edit_window)
        name_entry.grid(row=1, column=1, padx=10, pady=5)
        name_var = tk.StringVar()
        name_var.set("")  # Initialize as empty string
        tk.Label(edit_window, textvariable=name_var, bg="#f0f0f0").grid(row=1, column=2, padx=10, pady=5)

        tk.Label(edit_window, text="Address:", bg="#f0f0f0").grid(row=2, column=0, sticky="e", padx=10, pady=5)
        address_entry = tk.Entry(edit_window)
        address_entry.grid(row=2, column=1, padx=10, pady=5)
        address_var = tk.StringVar()
        address_var.set("")  # Initialize as empty string
        tk.Label(edit_window, textvariable=address_var, bg="#f0f0f0").grid(row=2, column=2, padx=10, pady=5)

        tk.Label(edit_window, text="Contact:", bg="#f0f0f0").grid(row=3, column=0, sticky="e", padx=10, pady=5)
        contact_entry = tk.Entry(edit_window)
        contact_entry.grid(row=3, column=1, padx=10, pady=5)
        contact_var = tk.StringVar()
        contact_var.set("")  # Initialize as empty string
        tk.Label(edit_window, textvariable=contact_var, bg="#f0f0f0").grid(row=3, column=2, padx=10, pady=5)

        tk.Label(edit_window, text="Service Provided:", bg="#f0f0f0").grid(row=4, column=0, sticky="e", padx=10, pady=5)
        service_provided_entry = tk.Entry(edit_window)
        service_provided_entry.grid(row=4, column=1, padx=10, pady=5)
        service_provided_var = tk.StringVar()
        service_provided_var.set("")  # Initialize as empty string
        tk.Label(edit_window, textvariable=service_provided_var, bg="#f0f0f0").grid(row=4, column=2, padx=10, pady=5)

        tk.Label(edit_window, text="Min Guests:", bg="#f0f0f0").grid(row=5, column=0, sticky="e", padx=10, pady=5)
        min_guests_entry = tk.Entry(edit_window)
        min_guests_entry.grid(row=5, column=1, padx=10, pady=5)
        min_guests_var = tk.StringVar()
        min_guests_var.set("")  # Initialize as empty string
        tk.Label(edit_window, textvariable=min_guests_var, bg="#f0f0f0").grid(row=5, column=2, padx=10, pady=5)

        tk.Label(edit_window, text="Max Guests:", bg="#f0f0f0").grid(row=6, column=0, sticky="e", padx=10, pady=5)
        max_guests_entry = tk.Entry(edit_window)
        max_guests_entry.grid(row=6, column=1, padx=10, pady=5)
        max_guests_var = tk.StringVar()
        max_guests_var.set("")  # Initialize as empty string
        tk.Label(edit_window, textvariable=max_guests_var, bg="#f0f0f0").grid(row=6, column=2, padx=10, pady=5)

        # Button frame
        button_frame = tk.Frame(edit_window, bg="#f0f0f0")
        button_frame.grid(row=7, columnspan=3, pady=10)

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
        # Function to display supplier details
        def show_supplier_details():
            # Retrieve supplier details based on supplier ID
            supplier_id = supplier_id_entry.get()
            supplier_details = None

            # Read supplier data from the pickle file
            with open("supplier_data.pkl", "rb") as file:
                while True:
                    try:
                        supp = pickle.load(file)
                        if supp.supplier_id == supplier_id:
                            supplier_details = supp
                            break
                    except EOFError:
                        break
            
            if supplier_details:
                # Display supplier details
                name_var.set(supplier_details.name)
                address_var.set(supplier_details.address)
                contact_var.set(supplier_details.contact)
                service_provided_var.set(supplier_details.service_provided)
                min_guests_var.set(supplier_details.min_guests)
                max_guests_var.set(supplier_details.max_guests)
            else:
                # If supplier ID not found, show error message
                result_label.config(text="Supplier ID not found!", fg="red")

        # Create a window for displaying supplier details
        display_window = tk.Toplevel(master)
        display_window.title("Display Suppliers")
        display_window.geometry("510x320")
        display_window.configure(bg="#f0f0f0")

        # Supplier ID label and entry field
        tk.Label(display_window, text="Supplier ID:", bg="#f0f0f0").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        supplier_id_entry = tk.Entry(display_window)
        supplier_id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Button to show supplier details
        show_button = tk.Button(display_window, text="Show Details", command=show_supplier_details, bg="#343a40", fg="yellow")
        show_button.grid(row=0, column=2, padx=10, pady=5)

        # Supplier details labels and variables
        name_var = tk.StringVar()
        address_var = tk.StringVar()
        contact_var = tk.StringVar()
        service_provided_var = tk.StringVar()
        min_guests_var = tk.StringVar()
        max_guests_var = tk.StringVar()

        tk.Label(display_window, text="Name:", bg="#f0f0f0").grid(row=1, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=name_var, bg="#f0f0f0").grid(row=1, column=1, padx=10, pady=5)

        tk.Label(display_window, text="Address:", bg="#f0f0f0").grid(row=2, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=address_var, bg="#f0f0f0").grid(row=2, column=1, padx=10, pady=5)

        tk.Label(display_window, text="Contact:", bg="#f0f0f0").grid(row=3, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=contact_var, bg="#f0f0f0").grid(row=3, column=1, padx=10, pady=5)

        tk.Label(display_window, text="Service Provided:", bg="#f0f0f0").grid(row=4, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=service_provided_var, bg="#f0f0f0").grid(row=4, column=1, padx=10, pady=5)

        tk.Label(display_window, text="Min Guests:", bg="#f0f0f0").grid(row=5, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=min_guests_var, bg="#f0f0f0").grid(row=5, column=1, padx=10, pady=5)

        tk.Label(display_window, text="Max Guests:", bg="#f0f0f0").grid(row=6, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=max_guests_var, bg="#f0f0f0").grid(row=6, column=1, padx=10, pady=5)

        # Result label to display error messages
        result_label = tk.Label(display_window, text="", bg="#f0f0f0", fg="red")
        result_label.grid(row=7, columnspan=2, padx=10, pady=5)
