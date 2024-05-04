import pickle
import tkinter as tk

class Client:
    def __init__(self, client_id, name, address, contact_details, budget):
        self.client_id = client_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.budget = budget

    @staticmethod
    def add_client(master):
        # Function to add a new client
        def store_client():
            client_id = client_id_entry.get()
            name = name_entry.get()
            address = address_entry.get()
            contact_details = contact_details_entry.get()
            budget = budget_entry.get()

            # Create a Client instance
            new_client = Client(client_id, name, address, contact_details, budget)

            # Save the client data to a pickle file
            with open("clients_record.pkl", "ab") as file:
                pickle.dump(new_client, file)

            # Close the client window
            client_window.destroy()

        # Create a new window for adding a client
        client_window = tk.Toplevel(master)
        client_window.title("Add Client")
        client_window.geometry("400x250")
        client_window.configure(bg="#f0f0f0")

        # Client details labels and entry fields
        tk.Label(client_window, text="Client ID:", bg="#f0f0f0").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        client_id_entry = tk.Entry(client_window)
        client_id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(client_window, text="Name:", bg="#f0f0f0").grid(row=1, column=0, sticky="e", padx=10, pady=5)
        name_entry = tk.Entry(client_window)
        name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(client_window, text="Address:", bg="#f0f0f0").grid(row=2, column=0, sticky="e", padx=10, pady=5)
        address_entry = tk.Entry(client_window)
        address_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(client_window, text="Contact Details:", bg="#f0f0f0").grid(row=3, column=0, sticky="e", padx=10, pady=5)
        contact_details_entry = tk.Entry(client_window)
        contact_details_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(client_window, text="Budget:", bg="#f0f0f0").grid(row=4, column=0, sticky="e", padx=10, pady=5)
        budget_entry = tk.Entry(client_window)
        budget_entry.grid(row=4, column=1, padx=10, pady=5)

        # Button frame
        button_frame = tk.Frame(client_window, bg="#f0f0f0")
        button_frame.grid(row=5, columnspan=2, pady=10)

        # Create buttons with same width
        button_width = 20

        # Define button colors
        button_bg_color = "#343a40"  # Charcoal gray
        button_fg_color = "yellow"

        # Button to save the client data
        save_button = tk.Button(button_frame, text="Save", command=store_client, width=button_width, bg=button_bg_color, fg=button_fg_color)
        save_button.grid(row=0, column=0, padx=10, pady=5)

    @staticmethod
    def del_client(master):
        # Function to delete a client
        def delete_client():
            client_id = client_id_entry.get()
            clients = []  # Initialize an empty list to store client data

            # Read client data from the pickle file into a list
            with open("clients_record.pkl", "rb") as file:
                while True:
                    try:
                        client = pickle.load(file)
                        clients.append(client)
                    except EOFError:
                        break

            # Filter out the client with the given ID
            filtered_clients = [client for client in clients if client.client_id != client_id]

            # Write the filtered clients back to the file
            with open("clients_record.pkl", "wb") as file:
                for client in filtered_clients:
                    pickle.dump(client, file)

            # Close the delete window
            delete_window.destroy()

        # Create a new window for deleting a client
        delete_window = tk.Toplevel(master)
        delete_window.title("Delete Client")
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

        # Client ID label and entry field
        tk.Label(delete_window, text="Client ID:", bg="#f0f0f0").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        client_id_entry = tk.Entry(delete_window)
        client_id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Button to delete the client
        delete_button = tk.Button(delete_window, text="Delete", command=delete_client, width=button_width, bg=button_bg_color, fg=button_fg_color)
        delete_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

    @staticmethod
    def edit_client(master):
        # Function to retrieve client details based on ID
        def edit_client_details():
            client_id = client_id_entry.get()
            # Read client data from the pickle file
            with open("clients_record.pkl", "rb") as file:
                while True:
                    try:
                        client = pickle.load(file)
                        if client.client_id == client_id:
                            # Display client details in entry fields
                            name_var.set(client.name)
                            address_var.set(client.address)
                            contact_details_var.set(client.contact_details)
                            budget_var.set(client.budget)
                            break
                    except EOFError:
                        break

        # Function to save the edited client details
        def save_changes():
            # Get updated client details from entry fields
            name = name_entry.get()
            address = address_entry.get()
            contact_details = contact_details_entry.get()
            budget = budget_entry.get()

            # Create a Client instance with updated details
            updated_client = Client(client_id_entry.get(), name, address, contact_details, budget)

            # Read existing client data from the pickle file
            clients = []
            with open("clients_record.pkl", "rb") as file:
                while True:
                    try:
                        client = pickle.load(file)
                        if client.client_id == client_id_entry.get():
                            clients.append(updated_client)  # Replace the existing client with updated details
                        else:
                            clients.append(client)
                    except EOFError:
                        break

            # Write the updated client data back to the file
            with open("clients_record.pkl", "wb") as file:
                for client in clients:
                    pickle.dump(client, file)

            # Close the edit window
            edit_window.destroy()

        # Create the edit window
        edit_window = tk.Toplevel(master)
        edit_window.title("Edit Client")
        edit_window.geometry("400x250")
        edit_window.configure(bg="#f0f0f0")

        # Client ID label and entry field
        tk.Label(edit_window, text="Client ID:", bg="#f0f0f0").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        client_id_entry = tk.Entry(edit_window)
        client_id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Button to retrieve client details
        retrieve_button = tk.Button(edit_window, text="Retrieve Details", command=edit_client_details, bg="#343a40", fg="yellow")
        retrieve_button.grid(row=0, column=2, padx=10, pady=5)

        # Client details labels and entry fields
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

        tk.Label(edit_window, text="Contact Details:", bg="#f0f0f0").grid(row=3, column=0, sticky="e", padx=10, pady=5)
        contact_details_entry = tk.Entry(edit_window)
        contact_details_entry.grid(row=3, column=1, padx=10, pady=5)
        contact_details_var = tk.StringVar()
        contact_details_var.set("")  # Initialize as empty string
        tk.Label(edit_window, textvariable=contact_details_var, bg="#f0f0f0").grid(row=3, column=2, padx=10, pady=5)

        tk.Label(edit_window, text="Budget:", bg="#f0f0f0").grid(row=4, column=0, sticky="e", padx=10, pady=5)
        budget_entry = tk.Entry(edit_window)
        budget_entry.grid(row=4, column=1, padx=10, pady=5)
        budget_var = tk.StringVar()
        budget_var.set("")  # Initialize as empty string
        tk.Label(edit_window, textvariable=budget_var, bg="#f0f0f0").grid(row=4, column=2, padx=10, pady=5)

        # Button frame
        button_frame = tk.Frame(edit_window, bg="#f0f0f0")
        button_frame.grid(row=5, columnspan=3, pady=10)

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
        # Function to display client details
        def show_client_details():
            # Retrieve client details based on client ID
            client_id = client_id_entry.get()
            client_details = None

            # Read client data from the pickle file
            with open("clients_record.pkl", "rb") as file:
                while True:
                    try:
                        client = pickle.load(file)
                        if client.client_id == client_id:
                            client_details = client
                            break
                    except EOFError:
                        break
            
            if client_details:
                # Display client details
                name_var.set(client_details.name)
                address_var.set(client_details.address)
                contact_details_var.set(client_details.contact_details)
                budget_var.set(client_details.budget)
            else:
                # If client ID not found, show error message
                result_label.config(text="Client ID not found!", fg="red")

        # Create a new window for displaying client details
        display_window = tk.Toplevel(master)
        display_window.title("Display Clients")
        display_window.geometry("400x250")
        display_window.configure(bg="#f0f0f0")

        # Client ID label and entry field
        tk.Label(display_window, text="Client ID:", bg="#f0f0f0").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        client_id_entry = tk.Entry(display_window)
        client_id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Button to show client details
        show_button = tk.Button(display_window, text="Show Details", command=show_client_details, bg="#343a40", fg="yellow")
        show_button.grid(row=0, column=2, padx=10, pady=5)

        # Client details labels and variables
        name_var = tk.StringVar()
        address_var = tk.StringVar()
        contact_details_var = tk.StringVar()
        budget_var = tk.StringVar()

        tk.Label(display_window, text="Name:", bg="#f0f0f0").grid(row=1, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=name_var, bg="#f0f0f0").grid(row=1, column=1, padx=10, pady=5)

        tk.Label(display_window, text="Address:", bg="#f0f0f0").grid(row=2, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=address_var, bg="#f0f0f0").grid(row=2, column=1, padx=10, pady=5)

        tk.Label(display_window, text="Contact Details:", bg="#f0f0f0").grid(row=3, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=contact_details_var, bg="#f0f0f0").grid(row=3, column=1, padx=10, pady=5)

        tk.Label(display_window, text="Budget:", bg="#f0f0f0").grid(row=4, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=budget_var, bg="#f0f0f0").grid(row=4, column=1, padx=10, pady=5)

        # Result label to display error messages
        result_label = tk.Label(display_window, text="", bg="#f0f0f0", fg="red")
        result_label.grid(row=5, columnspan=3, padx=10, pady=5) 
