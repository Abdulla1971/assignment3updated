import pickle  # Import the pickle module for serialization
import tkinter as tk  # Import the tkinter module for GUI creation

class Venue:
    # Define the Venue class
    def __init__(self, venue_id, name, address, contact, min_guests, max_guests):
        # Constructor to initialize venue attributes
        self.venue_id = venue_id
        self.name = name
        self.address = address
        self.contact = contact
        self.min_guests = min_guests
        self.max_guests = max_guests

    @staticmethod
    def add_venue(master):
        # Static method to add a new venue
        def save_venue():
            # Function to save venue details to file
            venue_id = venue_id_entry.get()
            name = name_entry.get()
            address = address_entry.get()
            contact = contact_entry.get()
            min_guests = min_guests_entry.get()
            max_guests = max_guests_entry.get()

            # Create a new Venue instance with provided details
            new_venue = Venue(venue_id, name, address, contact, min_guests, max_guests)

            # Open the file in append binary mode and serialize the new venue object
            with open("venue_data.pkl", "ab") as file:
                pickle.dump(new_venue, file)

            # Close the window after saving
            venue_window.destroy()

        # Create a new window for adding a venue
        venue_window = tk.Toplevel(master)
        venue_window.title("Add Venue")
        venue_window.geometry("510x300")
        venue_window.configure(bg="#f0f0f0")

        # Label and entry field for Venue ID
        tk.Label(venue_window, text="Venue ID:", bg="#f0f0f0").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        venue_id_entry = tk.Entry(venue_window)
        venue_id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Label and entry field for Venue Name
        tk.Label(venue_window, text="Name:", bg="#f0f0f0").grid(row=1, column=0, sticky="e", padx=10, pady=5)
        name_entry = tk.Entry(venue_window)
        name_entry.grid(row=1, column=1, padx=10, pady=5)

        # Label and entry field for Venue Address
        tk.Label(venue_window, text="Address:", bg="#f0f0f0").grid(row=2, column=0, sticky="e", padx=10, pady=5)
        address_entry = tk.Entry(venue_window)
        address_entry.grid(row=2, column=1, padx=10, pady=5)

        # Label and entry field for Venue Contact
        tk.Label(venue_window, text="Contact:", bg="#f0f0f0").grid(row=3, column=0, sticky="e", padx=10, pady=5)
        contact_entry = tk.Entry(venue_window)
        contact_entry.grid(row=3, column=1, padx=10, pady=5)

        # Label and entry field for Minimum Guests
        tk.Label(venue_window, text="Min Guests:", bg="#f0f0f0").grid(row=4, column=0, sticky="e", padx=10, pady=5)
        min_guests_entry = tk.Entry(venue_window)
        min_guests_entry.grid(row=4, column=1, padx=10, pady=5)

        # Label and entry field for Maximum Guests
        tk.Label(venue_window, text="Max Guests:", bg="#f0f0f0").grid(row=5, column=0, sticky="e", padx=10, pady=5)
        max_guests_entry = tk.Entry(venue_window)
        max_guests_entry.grid(row=5, column=1, padx=10, pady=5)

        # Frame for buttons
        button_frame = tk.Frame(venue_window, bg="#f0f0f0")
        button_frame.grid(row=6, columnspan=2, pady=10)

        # Define button properties
        button_width = 20
        button_bg_color = "#343a40"  # Charcoal gray
        button_fg_color = "yellow"

        # Button to save the venue
        save_button = tk.Button(button_frame, text="Save", command=save_venue, width=button_width, bg=button_bg_color, fg=button_fg_color)
        save_button.grid(row=0, column=0, padx=10, pady=5)

    @staticmethod
    def del_venue(master):
        # Static method to delete a venue
        def delete_venue():
            # Function to delete a venue from the file
            venue_id = venue_id_entry.get()
            venues = []

            # Read existing venues from file
            with open("venue_data.pkl", "rb") as file:
                while True:
                    try:
                        venue = pickle.load(file)
                        venues.append(venue)
                    except EOFError:
                        break

            # Filter out the venue to be deleted
            filtered_venues = [venue for venue in venues if venue.venue_id != venue_id]

            # Write the filtered list back to the file
            with open("venue_data.pkl", "wb") as file:
                for venue in filtered_venues:
                    pickle.dump(venue, file)

            # Close the delete window
            delete_window.destroy()

        # Create a window for deleting a venue
        delete_window = tk.Toplevel(master)
        delete_window.title("Delete Venue")
        delete_window.geometry("250x100")
        delete_window.configure(bg="#f0f0f0")

        # Frame for buttons
        button_frame = tk.Frame(delete_window, bg="#f0f0f0")
        button_frame.grid(row=5, columnspan=4, pady=10)

        # Define button properties
        button_width = 20
        button_bg_color = "#343a40"  # Charcoal gray
        button_fg_color = "yellow"

        # Label and entry field for Venue ID
        tk.Label(delete_window, text="Venue ID:", bg="#f0f0f0").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        venue_id_entry = tk.Entry(delete_window)
        venue_id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Button to delete the venue
        delete_button = tk.Button(delete_window, text="Delete", command=delete_venue, width=button_width, bg=button_bg_color, fg=button_fg_color)
        delete_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

    @staticmethod
    def edit_venue(master):
        # Static method to edit a venue
        def edit_venue_details():
            # Function to retrieve venue details for editing
            venue_id = venue_id_entry.get()
            with open("venue_data.pkl", "rb") as file:
                while True:
                    try:
                        venue = pickle.load(file)
                        if venue.venue_id == venue_id:
                            # Display venue details in entry fields
                            name_var.set(venue.name)
                            address_var.set(venue.address)
                            contact_var.set(venue.contact)
                            min_guests_var.set(venue.min_guests)
                            max_guests_var.set(venue.max_guests)
                            break
                    except EOFError:
                        break

        def save_changes():
            # Function to save edited venue details
            name = name_entry.get()
            address = address_entry.get()
            contact = contact_entry.get()
            min_guests = min_guests_entry.get()
            max_guests = max_guests_entry.get()

            # Create updated venue object
            updated_venue = Venue(venue_id_entry.get(), name, address, contact, min_guests, max_guests)

            venues = []
            # Read existing venues and update the edited one
            with open("venue_data.pkl", "rb") as file:
                while True:
                    try:
                        venue = pickle.load(file)
                        if venue.venue_id == venue_id_entry.get():
                            venues.append(updated_venue)
                        else:
                            venues.append(venue)
                    except EOFError:
                        break

            # Write the updated venues back to the file
            with open("venue_data.pkl", "wb") as file:
                for venue in venues:
                    pickle.dump(venue, file)

            # Close the edit window
            edit_window.destroy()

        # Create a window for editing a venue
        edit_window = tk.Toplevel(master)
        edit_window.title("Edit Venue")
        edit_window.geometry("510x300")
        edit_window.configure(bg="#f0f0f0")

        # Label and entry field for Venue ID
        tk.Label(edit_window, text="Venue ID:", bg="#f0f0f0").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        venue_id_entry = tk.Entry(edit_window)
        venue_id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Button to retrieve venue details for editing
        retrieve_button = tk.Button(edit_window, text="Retrieve Details", command=edit_venue_details, bg="#343a40", fg="yellow")
        retrieve_button.grid(row=0, column=2, padx=10, pady=5)

        # Label and entry field for Venue Name
        tk.Label(edit_window, text="Name:", bg="#f0f0f0").grid(row=1, column=0, sticky="e", padx=10, pady=5)
        name_entry = tk.Entry(edit_window)
        name_entry.grid(row=1, column=1, padx=10, pady=5)
        name_var = tk.StringVar()
        name_var.set("")
        tk.Label(edit_window, textvariable=name_var, bg="#f0f0f0").grid(row=1, column=2, padx=10, pady=5)

        # Label and entry field for Venue Address
        tk.Label(edit_window, text="Address:", bg="#f0f0f0").grid(row=2, column=0, sticky="e", padx=10, pady=5)
        address_entry = tk.Entry(edit_window)
        address_entry.grid(row=2, column=1, padx=10, pady=5)
        address_var = tk.StringVar()
        address_var.set("")
        tk.Label(edit_window, textvariable=address_var, bg="#f0f0f0").grid(row=2, column=2, padx=10, pady=5)

        # Label and entry field for Venue Contact
        tk.Label(edit_window, text="Contact:", bg="#f0f0f0").grid(row=3, column=0, sticky="e", padx=10, pady=5)
        contact_entry = tk.Entry(edit_window)
        contact_entry.grid(row=3, column=1, padx=10, pady=5)
        contact_var = tk.StringVar()
        contact_var.set("")
        tk.Label(edit_window, textvariable=contact_var, bg="#f0f0f0").grid(row=3, column=2, padx=10, pady=5)

        # Label and entry field for Minimum Guests
        tk.Label(edit_window, text="Min Guests:", bg="#f0f0f0").grid(row=4, column=0, sticky="e", padx=10, pady=5)
        min_guests_entry = tk.Entry(edit_window)
        min_guests_entry.grid(row=4, column=1, padx=10, pady=5)
        min_guests_var = tk.StringVar()
        min_guests_var.set("")
        tk.Label(edit_window, textvariable=min_guests_var, bg="#f0f0f0").grid(row=4, column=2, padx=10, pady=5)

        # Label and entry field for Maximum Guests
        tk.Label(edit_window, text="Max Guests:", bg="#f0f0f0").grid(row=5, column=0, sticky="e", padx=10, pady=5)
        max_guests_entry = tk.Entry(edit_window)
        max_guests_entry.grid(row=5, column=1, padx=10, pady=5)
        max_guests_var = tk.StringVar()
        max_guests_var.set("")
        tk.Label(edit_window, textvariable=max_guests_var, bg="#f0f0f0").grid(row=5, column=2, padx=10, pady=5)

        # Frame for buttons
        button_frame = tk.Frame(edit_window, bg="#f0f0f0")
        button_frame.grid(row=6, columnspan=3, pady=10)

        # Define button properties
        button_width = 20
        button_bg_color = "#343a40"  # Charcoal gray
        button_fg_color = "yellow"

        # Button to save changes
        save_button = tk.Button(button_frame, text="Save Changes", command=save_changes, width=button_width, bg=button_bg_color, fg=button_fg_color)
        save_button.grid(row=0, column=0, padx=10, pady=5)

    @staticmethod
    def show(master):
        # Static method to display venue details
        def show_venue_details():
            venue_id = venue_id_entry.get()
            venue_details = None

            # Read venue data from file
            with open("venue_data.pkl", "rb") as file:
                while True:
                    try:
                        venue = pickle.load(file)
                        if venue.venue_id == venue_id:
                            venue_details = venue
                            break
                    except EOFError:
                        break

            if venue_details:
                # Display venue details
                name_var.set(venue_details.name)
                address_var.set(venue_details.address)
                contact_var.set(venue_details.contact)
                min_guests_var.set(venue_details.min_guests)
                max_guests_var.set(venue_details.max_guests)
            else:
                # If venue ID not found, show error message
                result_label.config(text="Venue ID not found!", fg="red")

        # Create a window for displaying venue details
        display_window = tk.Toplevel(master)
        display_window.title("Display Venues")
        display_window.geometry("510x320")
        display_window.configure(bg="#f0f0f0")

        # Label and entry field for Venue ID
        tk.Label(display_window, text="Venue ID:", bg="#f0f0f0").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        venue_id_entry = tk.Entry(display_window)
        venue_id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Button to show venue details
        show_button = tk.Button(display_window, text="Show Details", command=show_venue_details, bg="#343a40", fg="yellow")
        show_button.grid(row=0, column=2, padx=10, pady=5)

        # Variables to store venue details
        name_var = tk.StringVar()
        address_var = tk.StringVar()
        contact_var = tk.StringVar()
        min_guests_var = tk.StringVar()
        max_guests_var = tk.StringVar()

        # Labels to display venue details
        tk.Label(display_window, text="Name:", bg="#f0f0f0").grid(row=1, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=name_var, bg="#f0f0f0").grid(row=1, column=1, padx=10, pady=5)

        tk.Label(display_window, text="Address:", bg="#f0f0f0").grid(row=2, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=address_var, bg="#f0f0f0").grid(row=2, column=1, padx=10, pady=5)

        tk.Label(display_window, text="Contact:", bg="#f0f0f0").grid(row=3, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=contact_var, bg="#f0f0f0").grid(row=3, column=1, padx=10, pady=5)

        tk.Label(display_window, text="Min Guests:", bg="#f0f0f0").grid(row=4, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=min_guests_var, bg="#f0f0f0").grid(row=4, column=1, padx=10, pady=5)

        tk.Label(display_window, text="Max Guests:", bg="#f0f0f0").grid(row=5, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=max_guests_var, bg="#f0f0f0").grid(row=5, column=1, padx=10, pady=5)

        # Label to display result or error message
        result_label = tk.Label(display_window, text="", bg="#f0f0f0", fg="red")
        result_label.grid(row=6, columnspan=3, padx=10, pady=5) 
