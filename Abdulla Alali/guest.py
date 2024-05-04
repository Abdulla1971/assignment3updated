import pickle  # Import the pickle module for object serialization
import tkinter as tk  # Import the tkinter module for GUI creation

class Guest:
    def __init__(self, guest_id, name, address, contact):
        self.guest_id = guest_id
        self.name = name
        self.address = address
        self.contact = contact

    @staticmethod
    def add_guest(master):
        # Function to handle adding a new guest
        def save_guest():
            # Retrieve data from entry fields
            guest_id = guest_id_entry.get()
            name = name_entry.get()
            address = address_entry.get()
            contact = contact_entry.get()

            # Create a Guest instance
            new_guest = Guest(guest_id, name, address, contact)

            # Save the guest data to a pickle file
            with open("guest_data.pkl", "ab") as file:
                pickle.dump(new_guest, file)

            # Close the guest window
            guest_window.destroy()

        # Create a new window for adding a guest
        guest_window = tk.Toplevel(master)
        guest_window.title("Add Guest")
        guest_window.geometry("510x300")
        guest_window.configure(bg="#f0f0f0")

        # Guest details labels and entry fields
        tk.Label(guest_window, text="Guest ID:", bg="#f0f0f0").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        guest_id_entry = tk.Entry(guest_window)
        guest_id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(guest_window, text="Name:", bg="#f0f0f0").grid(row=1, column=0, sticky="e", padx=10, pady=5)
        name_entry = tk.Entry(guest_window)
        name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(guest_window, text="Address:", bg="#f0f0f0").grid(row=2, column=0, sticky="e", padx=10, pady=5)
        address_entry = tk.Entry(guest_window)
        address_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(guest_window, text="Contact:", bg="#f0f0f0").grid(row=3, column=0, sticky="e", padx=10, pady=5)
        contact_entry = tk.Entry(guest_window)
        contact_entry.grid(row=3, column=1, padx=10, pady=5)

        # Button frame
        button_frame = tk.Frame(guest_window, bg="#f0f0f0")
        button_frame.grid(row=4, columnspan=2, pady=10)

        # Button to save the guest data
        save_button = tk.Button(button_frame, text="Save", command=save_guest, width=20, bg="#343a40", fg="yellow")
        save_button.grid(row=0, column=0, padx=10, pady=5)

    @staticmethod
    def del_guest(master):
        # Function to handle deleting a guest
        def delete_guest():
            # Get guest ID from entry field
            guest_id = guest_id_entry.get()
            guests = []  # Initialize an empty list to store guest data

            # Read guest data from the pickle file into a list
            with open("guest_data.pkl", "rb") as file:
                while True:
                    try:
                        guest = pickle.load(file)
                        guests.append(guest)
                    except EOFError:
                        break

            # Filter out the guest with the given ID
            filtered_guests = [guest for guest in guests if guest.guest_id != guest_id]

            # Write the filtered guests back to the file
            with open("guest_data.pkl", "wb") as file:
                for guest in filtered_guests:
                    pickle.dump(guest, file)

            # Close the delete window
            delete_window.destroy()

        # Create a window for deleting a guest
        delete_window = tk.Toplevel(master)
        delete_window.title("Delete Guest")
        delete_window.geometry("250x100")
        delete_window.configure(bg="#f0f0f0")

        # Button frame
        button_frame = tk.Frame(delete_window, bg="#f0f0f0")
        button_frame.grid(row=5, columnspan=4, pady=10)

        # Guest ID label and entry field
        tk.Label(delete_window, text="Guest ID:", bg="#f0f0f0").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        guest_id_entry = tk.Entry(delete_window)
        guest_id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Button to delete the guest
        delete_button = tk.Button(delete_window, text="Delete", command=delete_guest, width=20, bg="#343a40", fg="yellow")
        delete_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

    @staticmethod
    def edit_guest(master):
        # Function to handle editing guest details
        def edit_guest_details():
            # Get guest ID from entry field
            guest_id = guest_id_entry.get()
            # Read guest data from the pickle file
            with open("guest_data.pkl", "rb") as file:
                while True:
                    try:
                        guest = pickle.load(file)
                        if guest.guest_id == guest_id:
                            # Display guest details in entry fields
                            name_var.set(guest.name)
                            address_var.set(guest.address)
                            contact_var.set(guest.contact)
                            break
                    except EOFError:
                        break

        # Function to save the edited guest details
        def save_changes():
            # Get updated guest details from entry fields
            name = name_entry.get()
            address = address_entry.get()
            contact = contact_entry.get()

            # Create a Guest instance with updated details
            updated_guest = Guest(guest_id_entry.get(), name, address, contact)

            # Read existing guest data from the pickle file
            guests = []
            with open("guest_data.pkl", "rb") as file:
                while True:
                    try:
                        guest = pickle.load(file)
                        if guest.guest_id == guest_id_entry.get():
                            guests.append(updated_guest)  # Replace the existing guest with updated details
                        else:
                            guests.append(guest)
                    except EOFError:
                        break

            # Write the updated guest data back to the file
            with open("guest_data.pkl", "wb") as file:
                for guest in guests:
                    pickle.dump(guest, file)

            # Close the edit window
            edit_window.destroy()

        # Create the edit window
        edit_window = tk.Toplevel(master)
        edit_window.title("Edit Guest")
        edit_window.geometry("510x300")
        edit_window.configure(bg="#f0f0f0")

        # Guest ID label and entry field
        tk.Label(edit_window, text="Guest ID:", bg="#f0f0f0").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        guest_id_entry = tk.Entry(edit_window)
        guest_id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Button to retrieve guest details
        retrieve_button = tk.Button(edit_window, text="Retrieve Details", command=edit_guest_details, bg="#343a40", fg="yellow")
        retrieve_button.grid(row=0, column=2, padx=10, pady=5)

        # Guest details labels and entry fields
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

        # Button frame
        button_frame = tk.Frame(edit_window, bg="#f0f0f0")
        button_frame.grid(row=4, columnspan=3, pady=10)

        # Button to save the changes
        save_button = tk.Button(button_frame, text="Save Changes", command=save_changes, width=20, bg="#343a40", fg="yellow")
        save_button.grid(row=0, column=0, padx=10, pady=5)

    @staticmethod
    def show(master):
        # Function to handle displaying guest details
        def show_guest_details():
            # Retrieve guest details based on guest ID
            guest_id = guest_id_entry.get()
            guest_details = None

            # Read guest data from the pickle file
            with open("guest_data.pkl", "rb") as file:
                while True:
                    try:
                        guest = pickle.load(file)
                        if guest.guest_id == guest_id:
                            guest_details = guest
                            break
                    except EOFError:
                        break
            
            if guest_details:
                # Display guest details
                name_var.set(guest_details.name)
                address_var.set(guest_details.address)
                contact_var.set(guest_details.contact)
            else:
                # If guest ID not found, show error message
                result_label.config(text="Guest ID not found!", fg="red")

        # Create a window for displaying guest details
        display_window = tk.Toplevel(master)
        display_window.title("Display Guests")
        display_window.geometry("510x220")
        display_window.configure(bg="#f0f0f0")

        # Guest ID label and entry field
        tk.Label(display_window, text="Guest ID:", bg="#f0f0f0").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        guest_id_entry = tk.Entry(display_window)
        guest_id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Button to show guest details
        show_button = tk.Button(display_window, text="Show Details", command=show_guest_details, bg="#343a40", fg="yellow")
        show_button.grid(row=0, column=2, padx=10, pady=5)

        # Guest details labels and variables
        name_var = tk.StringVar()
        address_var = tk.StringVar()
        contact_var = tk.StringVar()

        tk.Label(display_window, text="Name:", bg="#f0f0f0").grid(row=1, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=name_var, bg="#f0f0f0").grid(row=1, column=1, padx=10, pady=5)

        tk.Label(display_window, text="Address:", bg="#f0f0f0").grid(row=2, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=address_var, bg="#f0f0f0").grid(row=2, column=1, padx=10, pady=5)

        tk.Label(display_window, text="Contact:", bg="#f0f0f0").grid(row=3, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=contact_var, bg="#f0f0f0").grid(row=3, column=1, padx=10, pady=5)

        # Result label to display error messages
        result_label = tk.Label(display_window, text="", bg="#f0f0f0", fg="red")
        result_label.grid(row=4, columnspan=3, padx=10, pady=5)