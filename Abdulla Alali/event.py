import pickle
import tkinter as tk

class Event:
    # Class for representing an event

    def __init__(self, event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, suppliers_company, invoice):
        # Constructor method for initializing event attributes
        self.event_id = event_id
        self.event_type = event_type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue_address = venue_address
        self.client_id = client_id
        self.guest_list = guest_list
        self.suppliers_company = suppliers_company
        self.invoice = invoice

    @staticmethod
    def add_event(master):
        # Static method to add a new event

        def save_event():
            # Function to save the entered event details
            event_id = event_id_entry.get()
            event_type = event_type_entry.get()
            theme = theme_entry.get()
            date = date_entry.get()
            time = time_entry.get()
            duration = duration_entry.get()
            venue_address = venue_address_entry.get()
            client_id = client_id_entry.get()
            guest_list = guest_list_entry.get()
            suppliers_company = suppliers_company_entry.get()
            invoice = invoice_entry.get()

            # Create a new event object with entered details
            new_event = Event(event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, suppliers_company, invoice)

            # Write the new event to the file
            with open("events.pkl", "ab") as file:
                pickle.dump(new_event, file)

            # Close the event window after saving
            event_window.destroy()

        # Create a new window for adding an event
        event_window = tk.Toplevel(master)
        event_window.title("Add Event")
        event_window.geometry("510x400")
        event_window.configure(bg="#f0f0f0")

        # Label and entry field for Event ID
        tk.Label(event_window, text="Event ID:", bg="#f0f0f0").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        event_id_entry = tk.Entry(event_window)
        event_id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Label and entry field for Event Type
        tk.Label(event_window, text="Event Type:", bg="#f0f0f0").grid(row=1, column=0, sticky="e", padx=10, pady=5)
        event_type_entry = tk.Entry(event_window)
        event_type_entry.grid(row=1, column=1, padx=10, pady=5)

        # Label and entry field for Theme
        tk.Label(event_window, text="Theme:", bg="#f0f0f0").grid(row=2, column=0, sticky="e", padx=10, pady=5)
        theme_entry = tk.Entry(event_window)
        theme_entry.grid(row=2, column=1, padx=10, pady=5)

        # Label and entry field for Date
        tk.Label(event_window, text="Date:", bg="#f0f0f0").grid(row=3, column=0, sticky="e", padx=10, pady=5)
        date_entry = tk.Entry(event_window)
        date_entry.grid(row=3, column=1, padx=10, pady=5)

        # Label and entry field for Time
        tk.Label(event_window, text="Time:", bg="#f0f0f0").grid(row=4, column=0, sticky="e", padx=10, pady=5)
        time_entry = tk.Entry(event_window)
        time_entry.grid(row=4, column=1, padx=10, pady=5)

        # Label and entry field for Duration
        tk.Label(event_window, text="Duration:", bg="#f0f0f0").grid(row=5, column=0, sticky="e", padx=10, pady=5)
        duration_entry = tk.Entry(event_window)
        duration_entry.grid(row=5, column=1, padx=10, pady=5)

        # Label and entry field for Venue Address
        tk.Label(event_window, text="Venue Address:", bg="#f0f0f0").grid(row=6, column=0, sticky="e", padx=10, pady=5)
        venue_address_entry = tk.Entry(event_window)
        venue_address_entry.grid(row=6, column=1, padx=10, pady=5)

        # Label and entry field for Client ID
        tk.Label(event_window, text="Client ID:", bg="#f0f0f0").grid(row=7, column=0, sticky="e", padx=10, pady=5)
        client_id_entry = tk.Entry(event_window)
        client_id_entry.grid(row=7, column=1, padx=10, pady=5)

        # Label and entry field for Guest List
        tk.Label(event_window, text="Guest List:", bg="#f0f0f0").grid(row=8, column=0, sticky="e", padx=10, pady=5)
        guest_list_entry = tk.Entry(event_window)
        guest_list_entry.grid(row=8, column=1, padx=10, pady=5)

        # Label and entry field for Suppliers Company
        tk.Label(event_window, text="Suppliers Company:", bg="#f0f0f0").grid(row=9, column=0, sticky="e", padx=10, pady=5)
        suppliers_company_entry = tk.Entry(event_window)
        suppliers_company_entry.grid(row=9, column=1, padx=10, pady=5)

        # Label and entry field for Invoice
        tk.Label(event_window, text="Invoice:", bg="#f0f0f0").grid(row=10, column=0, sticky="e", padx=10, pady=5)
        invoice_entry = tk.Entry(event_window)
        invoice_entry.grid(row=10, column=1, padx=10, pady=5)

        # Frame for buttons
        button_frame = tk.Frame(event_window, bg="#f0f0f0")
        button_frame.grid(row=11, columnspan=2, pady=10)

        button_width = 20

        button_bg_color = "#343a40"  # Charcoal gray
        button_fg_color = "yellow"

        # Button to save event
        save_button = tk.Button(button_frame, text="Save", command=save_event, width=button_width, bg=button_bg_color, fg=button_fg_color)
        save_button.grid(row=0, column=0, padx=10, pady=5)

    @staticmethod
    def del_event(master):
        # Static method to delete an event

        def delete_event():
            # Function to delete the specified event
            event_id = event_id_entry.get()
            events = []

            # Read events from file and exclude the one to be deleted
            with open("events.pkl", "rb") as file:
                while True:
                    try:
                        evt = pickle.load(file)
                        if evt.event_id != event_id:
                            events.append(evt)
                    except EOFError:
                        break

            # Write the remaining events back to the file
            with open("events.pkl", "wb") as file:
                for evt in events:
                    pickle.dump(evt, file)

            # Close the delete window after deleting
            delete_window.destroy()

        # Create a new window for deleting an event
        delete_window = tk.Toplevel(master)
        delete_window.title("Delete Event")
        delete_window.geometry("250x100")
        delete_window.configure(bg="#f0f0f0")

        # Frame for buttons
        button_frame = tk.Frame(delete_window, bg="#f0f0f0")
        button_frame.grid(row=5, columnspan=4, pady=10)

        button_width = 20

        button_bg_color = "#343a40"  # Charcoal gray
        button_fg_color = "yellow"

        # Label and entry field for Event ID
        tk.Label(delete_window, text="Event ID:", bg="#f0f0f0").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        event_id_entry = tk.Entry(delete_window)
        event_id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Button to delete event
        delete_button = tk.Button(delete_window, text="Delete", command=delete_event, width=button_width, bg=button_bg_color, fg=button_fg_color)
        delete_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

    @staticmethod
    def edit_event(master):
        # Static method to edit an event

        def edit_event_details():
            # Function to retrieve and display event details for editing
            event_id = event_id_entry.get()
            with open("events.pkl", "rb") as file:
                while True:
                    try:
                        evt = pickle.load(file)
                        if evt.event_id == event_id:
                            event_type_var.set(evt.event_type)
                            theme_var.set(evt.theme)
                            date_var.set(evt.date)
                            time_var.set(evt.time)
                            duration_var.set(evt.duration)
                            venue_address_var.set(evt.venue_address)
                            client_id_var.set(evt.client_id)
                            guest_list_var.set(evt.guest_list)
                            suppliers_company_var.set(evt.suppliers_company)
                            invoice_var.set(evt.invoice)
                            break
                    except EOFError:
                        break

        def save_changes():
            # Function to save the edited event details
            event_id = event_id_entry.get()
            event_type = event_type_entry.get()
            theme = theme_entry.get()
            date = date_entry.get()
            time = time_entry.get()
            duration = duration_entry.get()
            venue_address = venue_address_entry.get()
            client_id = client_id_entry.get()
            guest_list = guest_list_entry.get()
            suppliers_company = suppliers_company_entry.get()
            invoice = invoice_entry.get()

            # Create an updated event object
            updated_event = Event(event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, suppliers_company, invoice)

            # Read events from file and update the specified event
            events = []
            with open("events.pkl", "rb") as file:
                while True:
                    try:
                        evt = pickle.load(file)
                        if evt.event_id == event_id:
                            events.append(updated_event)
                        else:
                            events.append(evt)
                    except EOFError:
                        break

            # Write the updated events back to the file
            with open("events.pkl", "wb") as file:
                for evt in events:
                    pickle.dump(evt, file)

            # Close the edit window after saving changes
            edit_window.destroy()

        # Create a new window for editing an event
        edit_window = tk.Toplevel(master)
        edit_window.title("Edit Event")
        edit_window.geometry("510x400")
        edit_window.configure(bg="#f0f0f0")

        # Label and entry field for Event ID
        tk.Label(edit_window, text="Event ID:", bg="#f0f0f0").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        event_id_entry = tk.Entry(edit_window)
        event_id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Button to retrieve event details for editing
        retrieve_button = tk.Button(edit_window, text="Retrieve Details", command=edit_event_details, bg="#343a40", fg="yellow")
        retrieve_button.grid(row=0, column=2, padx=10, pady=5)

        # Label and entry field for Event Type
        tk.Label(edit_window, text="Event Type:", bg="#f0f0f0").grid(row=1, column=0, sticky="e", padx=10, pady=5)
        event_type_entry = tk.Entry(edit_window)
        event_type_entry.grid(row=1, column=1, padx=10, pady=5)
        event_type_var = tk.StringVar()
        event_type_var.set("")  
        tk.Label(edit_window, textvariable=event_type_var, bg="#f0f0f0").grid(row=1, column=2, padx=10, pady=5)

        # Label and entry field for Theme
        tk.Label(edit_window, text="Theme:", bg="#f0f0f0").grid(row=2, column=0, sticky="e", padx=10, pady=5)
        theme_entry = tk.Entry(edit_window)
        theme_entry.grid(row=2, column=1, padx=10, pady=5)
        theme_var = tk.StringVar()
        theme_var.set("")  
        tk.Label(edit_window, textvariable=theme_var, bg="#f0f0f0").grid(row=2, column=2, padx=10, pady=5)

        # Label and entry field for Date
        tk.Label(edit_window, text="Date:", bg="#f0f0f0").grid(row=3, column=0, sticky="e", padx=10, pady=5)
        date_entry = tk.Entry(edit_window)
        date_entry.grid(row=3, column=1, padx=10, pady=5)
        date_var = tk.StringVar()
        date_var.set("")  
        tk.Label(edit_window, textvariable=date_var, bg="#f0f0f0").grid(row=3, column=2, padx=10, pady=5)

        # Label and entry field for Time
        tk.Label(edit_window, text="Time:", bg="#f0f0f0").grid(row=4, column=0, sticky="e", padx=10, pady=5)
        time_entry = tk.Entry(edit_window)
        time_entry.grid(row=4, column=1, padx=10, pady=5)
        time_var = tk.StringVar()
        time_var.set("")  
        tk.Label(edit_window, textvariable=time_var, bg="#f0f0f0").grid(row=4, column=2, padx=10, pady=5)

        # Label and entry field for Duration
        tk.Label(edit_window, text="Duration:", bg="#f0f0f0").grid(row=5, column=0, sticky="e", padx=10, pady=5)
        duration_entry = tk.Entry(edit_window)
        duration_entry.grid(row=5, column=1, padx=10, pady=5)
        duration_var = tk.StringVar()
        duration_var.set("")  
        tk.Label(edit_window, textvariable=duration_var, bg="#f0f0f0").grid(row=5, column=2, padx=10, pady=5)

        # Label and entry field for Venue Address
        tk.Label(edit_window, text="Venue Address:", bg="#f0f0f0").grid(row=6, column=0, sticky="e", padx=10, pady=5)
        venue_address_entry = tk.Entry(edit_window)
        venue_address_entry.grid(row=6, column=1, padx=10, pady=5)
        venue_address_var = tk.StringVar()
        venue_address_var.set("")  
        tk.Label(edit_window, textvariable=venue_address_var, bg="#f0f0f0").grid(row=6, column=2, padx=10, pady=5)

        # Label and entry field for Client ID
        tk.Label(edit_window, text="Client ID:", bg="#f0f0f0").grid(row=7, column=0, sticky="e", padx=10, pady=5)
        client_id_entry = tk.Entry(edit_window)
        client_id_entry.grid(row=7, column=1, padx=10, pady=5)
        client_id_var = tk.StringVar()
        client_id_var.set("")  
        tk.Label(edit_window, textvariable=client_id_var, bg="#f0f0f0").grid(row=7, column=2, padx=10, pady=5)

        # Label and entry field for Guest List
        tk.Label(edit_window, text="Guest List:", bg="#f0f0f0").grid(row=8, column=0, sticky="e", padx=10, pady=5)
        guest_list_entry = tk.Entry(edit_window)
        guest_list_entry.grid(row=8, column=1, padx=10, pady=5)
        guest_list_var = tk.StringVar()
        guest_list_var.set("")  
        tk.Label(edit_window, textvariable=guest_list_var, bg="#f0f0f0").grid(row=8, column=2, padx=10, pady=5)

        # Label and entry field for Suppliers Company
        tk.Label(edit_window, text="Suppliers Company:", bg="#f0f0f0").grid(row=9, column=0, sticky="e", padx=10, pady=5)
        suppliers_company_entry = tk.Entry(edit_window)
        suppliers_company_entry.grid(row=9, column=1, padx=10, pady=5)
        suppliers_company_var = tk.StringVar()
        suppliers_company_var.set("")  
        tk.Label(edit_window, textvariable=suppliers_company_var, bg="#f0f0f0").grid(row=9, column=2, padx=10, pady=5)

        # Label and entry field for Invoice
        tk.Label(edit_window, text="Invoice:", bg="#f0f0f0").grid(row=10, column=0, sticky="e", padx=10, pady=5)
        invoice_entry = tk.Entry(edit_window)
        invoice_entry.grid(row=10, column=1, padx=10, pady=5)
        invoice_var = tk.StringVar()
        invoice_var.set("")  
        tk.Label(edit_window, textvariable=invoice_var, bg="#f0f0f0").grid(row=10, column=2, padx=10, pady=5)

        # Frame for buttons
        button_frame = tk.Frame(edit_window, bg="#f0f0f0")
        button_frame.grid(row=11, columnspan=3, pady=10)

        button_width = 20

        button_bg_color = "#343a40"  # Charcoal gray
        button_fg_color = "yellow"

        # Button to save changes
        save_button = tk.Button(button_frame, text="Save Changes", command=save_changes, width=button_width, bg=button_bg_color, fg=button_fg_color)
        save_button.grid(row=0, column=0, padx=10, pady=5)

    @staticmethod
    def show(master):
        # Static method to display event details

        def show_event_details():
            # Function to retrieve and display event details
            event_id = event_id_entry.get()
            event_details = None
            with open("events.pkl", "rb") as file:
                while True:
                    try:
                        evt = pickle.load(file)
                        if evt.event_id == event_id:
                            event_details = evt
                            break
                    except EOFError:
                        break

            if event_details:
                event_type_var.set(event_details.event_type)
                theme_var.set(event_details.theme)
                date_var.set(event_details.date)
                time_var.set(event_details.time)
                duration_var.set(event_details.duration)
                venue_address_var.set(event_details.venue_address)
                client_id_var.set(event_details.client_id)
                guest_list_var.set(event_details.guest_list)
                suppliers_company_var.set(event_details.suppliers_company)
                invoice_var.set(event_details.invoice)
            else:
                result_label.config(text="Event ID not found!", fg="red")

        # Create a new window for displaying event details
        display_window = tk.Toplevel(master)
        display_window.title("Display Events")
        display_window.geometry("510x450")
        display_window.configure(bg="#f0f0f0")

        # Label and entry field for Event ID
        tk.Label(display_window, text="Event ID:", bg="#f0f0f0").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        event_id_entry = tk.Entry(display_window)
        event_id_entry.grid(row=0, column=1, padx=10, pady=5)

        # Button to display event details
        display_button = tk.Button(display_window, text="Display Details", command=show_event_details, bg="#343a40", fg="yellow")
        display_button.grid(row=0, column=2, padx=10, pady=5)

        # Labels and variables to display event details
        event_type_var = tk.StringVar()
        theme_var = tk.StringVar()
        date_var = tk.StringVar()
        time_var = tk.StringVar()
        duration_var = tk.StringVar()
        venue_address_var = tk.StringVar()
        client_id_var = tk.StringVar()
        guest_list_var = tk.StringVar()
        suppliers_company_var = tk.StringVar()
        invoice_var = tk.StringVar()

        tk.Label(display_window, text="Event Type:", bg="#f0f0f0").grid(row=1, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=event_type_var, bg="#f0f0f0").grid(row=1, column=1, padx=10, pady=5)

        tk.Label(display_window, text="Theme:", bg="#f0f0f0").grid(row=2, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=theme_var, bg="#f0f0f0").grid(row=2, column=1, padx=10, pady=5)

        tk.Label(display_window, text="Date:", bg="#f0f0f0").grid(row=3, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=date_var, bg="#f0f0f0").grid(row=3, column=1, padx=10, pady=5)

        tk.Label(display_window, text="Time:", bg="#f0f0f0").grid(row=4, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=time_var, bg="#f0f0f0").grid(row=4, column=1, padx=10, pady=5)

        tk.Label(display_window, text="Duration:", bg="#f0f0f0").grid(row=5, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=duration_var, bg="#f0f0f0").grid(row=5, column=1, padx=10, pady=5)

        tk.Label(display_window, text="Venue Address:", bg="#f0f0f0").grid(row=6, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=venue_address_var, bg="#f0f0f0").grid(row=6, column=1, padx=10, pady=5)

        tk.Label(display_window, text="Client ID:", bg="#f0f0f0").grid(row=7, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=client_id_var, bg="#f0f0f0").grid(row=7, column=1, padx=10, pady=5)

        tk.Label(display_window, text="Guest List:", bg="#f0f0f0").grid(row=8, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=guest_list_var, bg="#f0f0f0").grid(row=8, column=1, padx=10, pady=5)

        tk.Label(display_window, text="Suppliers Company:", bg="#f0f0f0").grid(row=9, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=suppliers_company_var, bg="#f0f0f0").grid(row=9, column=1, padx=10, pady=5)

        tk.Label(display_window, text="Invoice:", bg="#f0f0f0").grid(row=10, column=0, sticky="e", padx=10, pady=5)
        tk.Label(display_window, textvariable=invoice_var, bg="#f0f0f0").grid(row=10, column=1, padx=10, pady=5)

        # Label to show result of displaying event details
        result_label = tk.Label(display_window, text="", bg="#f0f0f0")
        result_label.grid(row=11, columnspan=2, pady=10)