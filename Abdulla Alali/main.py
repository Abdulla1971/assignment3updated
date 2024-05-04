import pickle
import tkinter as tk
from employee import Employee
from event import Event
from client import Client
from supplier import Supplier
from venue import Venue
from guest import Guest

class MainTkinterFrontend:
    def __init__(self, master):
        self.master = master
        self.master.title("Greatest Events Company Management System")
        self.master.geometry("600x400")

        # Set background color
        self.master.configure(bg="#f0f0f0")

        # Create a label for the title
        title_label = tk.Label(master, text="Welcome to Greatest Events Company", font=("Helvetica", 20), bg="#f0f0f0")
        title_label.pack(pady=20)

        # Create buttons frame
        buttons_frame = tk.Frame(master, bg="#f0f0f0")
        buttons_frame.pack()

        # Create buttons with same width
        button_width = 20

        # Define button colors
        button_bg_color = "#343a40"  # Charcoal gray
        button_fg_color = "black"

        employee_button = tk.Button(buttons_frame, text="Manage Employees", width=button_width, command=self.employee_futher_menu, bg=button_bg_color, fg=button_fg_color)
        employee_button.grid(row=0, column=0, padx=10, pady=10)

        event_button = tk.Button(buttons_frame, text="Manage Events", width=button_width, command=self.event_futher_menu, bg=button_bg_color, fg=button_fg_color)
        event_button.grid(row=0, column=1, padx=10, pady=10)

        client_button = tk.Button(buttons_frame, text="Manage Clients", width=button_width, command=self.client_further_menu, bg=button_bg_color, fg=button_fg_color)
        client_button.grid(row=1, column=0, padx=10, pady=10)

        supplier_button = tk.Button(buttons_frame, text="Manage Suppliers", width=button_width, command=self.supplier_further_menu, bg=button_bg_color, fg=button_fg_color)
        supplier_button.grid(row=1, column=1, padx=10, pady=10)

        venue_button = tk.Button(buttons_frame, text="Manage Venues", width=button_width, command=self.venue_further_menu, bg=button_bg_color, fg=button_fg_color)
        venue_button.grid(row=2, column=0, padx=10, pady=10)

        guest_button = tk.Button(buttons_frame, text="Manage Guests", width=button_width, command=self.guest_further_menu, bg=button_bg_color, fg=button_fg_color)
        guest_button.grid(row=2, column=1, padx=10, pady=10)

        feedback_button = tk.Button(buttons_frame, text="Feedback & Rating", width=button_width, command=self.feedback_rating_menu, bg=button_bg_color, fg=button_fg_color)
        feedback_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def employee_futher_menu(self):
        employee_window = tk.Toplevel(self.master)
        employee_window.title("Employee Management")
        employee_window.geometry("600x400")
        employee_window.configure(bg="#f0f0f0")

        # Create a label for the title
        title_label = tk.Label(employee_window, text="Manage Employees", font=("Helvetica", 20), bg="#f0f0f0")
        title_label.pack(pady=20)

        # Create buttons frame
        employee_buttons_frame = tk.Frame(employee_window, bg="#f0f0f0")
        employee_buttons_frame.pack()

        # Create buttons with same width
        button_width = 20

        # Define button colors
        button_bg_color = "#343a40"  # Charcoal gray
        button_fg_color = "black"

        add_button = tk.Button(employee_buttons_frame, text="Add Employee", width=button_width, command=lambda: Employee.add_employee(self.master), bg=button_bg_color, fg=button_fg_color)
        add_button.grid(row=0, column=0, padx=10, pady=10)

        delete_button = tk.Button(employee_buttons_frame, text="Delete Employee", width=button_width, command=lambda: Employee.del_employee(self.master), bg=button_bg_color, fg=button_fg_color)
        delete_button.grid(row=0, column=1, padx=10, pady=10)

        edit_button = tk.Button(employee_buttons_frame, text="Edit Employee", width=button_width, command=lambda: Employee.edit_employee(self.master), bg=button_bg_color, fg=button_fg_color)
        edit_button.grid(row=1, column=0, padx=10, pady=10)

        display_button = tk.Button(employee_buttons_frame, text="Display Employees", width=button_width, command=lambda: Employee.show(self.master), bg=button_bg_color, fg=button_fg_color)
        display_button.grid(row=1, column=1, padx=10, pady=10)

    def event_futher_menu(self):
        event_window = tk.Toplevel(self.master)
        event_window.title("Event Management")
        event_window.geometry("600x400")
        event_window.configure(bg="#f0f0f0")

        # Create a label for the title
        title_label = tk.Label(event_window, text="Manage Events", font=("Helvetica", 20), bg="#f0f0f0")
        title_label.pack(pady=20)

        # Create buttons frame
        event_buttons_frame = tk.Frame(event_window, bg="#f0f0f0")
        event_buttons_frame.pack()

        # Create buttons with same width
        button_width = 20

        # Define button colors
        button_bg_color = "#343a40"  # Charcoal gray
        button_fg_color = "black"

        add_event_button = tk.Button(event_buttons_frame, text="Add Event", width=button_width, command=lambda: Event.add_event(self.master), bg=button_bg_color, fg=button_fg_color)
        add_event_button.grid(row=2, column=0, padx=10, pady=10)

        delete_event_button = tk.Button(event_buttons_frame, text="Delete Event", width=button_width, command=lambda: Event.del_event(self.master), bg=button_bg_color, fg=button_fg_color)
        delete_event_button.grid(row=2, column=1, padx=10, pady=10)

        edit_event_button = tk.Button(event_buttons_frame, text="Edit Event", width=button_width, command=lambda: Event.edit_event(self.master), bg=button_bg_color, fg=button_fg_color)
        edit_event_button.grid(row=3, column=0, padx=10, pady=10)

        display_events_button = tk.Button(event_buttons_frame, text="Display Events", width=button_width, command=lambda: Event.show(self.master), bg=button_bg_color, fg=button_fg_color)
        display_events_button.grid(row=3, column=1, padx=10, pady=10)

    def client_further_menu(self):
        client_window = tk.Toplevel(self.master)
        client_window.title("Client Management")
        client_window.geometry("600x400")
        client_window.configure(bg="#f0f0f0")

        # Create a label for the title
        title_label = tk.Label(client_window, text="Manage Clients", font=("Helvetica", 20), bg="#f0f0f0")
        title_label.pack(pady=20)

        # Create buttons frame
        client_buttons_frame = tk.Frame(client_window, bg="#f0f0f0")
        client_buttons_frame.pack()

        # Create buttons with same width
        button_width = 20

        # Define button colors
        button_bg_color = "#343a40"  # Charcoal gray
        button_fg_color = "black"

        add_button = tk.Button(client_buttons_frame, text="Add Client", width=button_width, command=lambda: Client.add_client(self.master), bg=button_bg_color, fg=button_fg_color)
        add_button.grid(row=0, column=0, padx=10, pady=10)

        delete_button = tk.Button(client_buttons_frame, text="Delete Client", width=button_width, command=lambda: Client.del_client(self.master), bg=button_bg_color, fg=button_fg_color)
        delete_button.grid(row=0, column=1, padx=10, pady=10)

        edit_button = tk.Button(client_buttons_frame, text="Edit Client", width=button_width, command=lambda: Client.edit_client(self.master), bg=button_bg_color, fg=button_fg_color)
        edit_button.grid(row=1, column=0, padx=10, pady=10)

        display_button = tk.Button(client_buttons_frame, text="Display Clients", width=button_width, command=lambda: Client.show(self.master), bg=button_bg_color, fg=button_fg_color)
        display_button.grid(row=1, column=1, padx=10, pady=10)

    def supplier_further_menu(self):
        supplier_window = tk.Toplevel(self.master)
        supplier_window.title("Supplier Management")
        supplier_window.geometry("600x400")
        supplier_window.configure(bg="#f0f0f0")

        # Create a label for the title
        title_label = tk.Label(supplier_window, text="Manage Suppliers", font=("Helvetica", 20), bg="#f0f0f0")
        title_label.pack(pady=20)

        # Create buttons frame
        supplier_buttons_frame = tk.Frame(supplier_window, bg="#f0f0f0")
        supplier_buttons_frame.pack()

        # Create buttons with same width
        button_width = 20

        # Define button colors
        button_bg_color = "#343a40"  # Charcoal gray
        button_fg_color = "black"

        add_button = tk.Button(supplier_buttons_frame, text="Add Supplier", width=button_width, command=lambda: Supplier.add_supplier(self.master), bg=button_bg_color, fg=button_fg_color)
        add_button.grid(row=0, column=0, padx=10, pady=10)

        delete_button = tk.Button(supplier_buttons_frame, text="Delete Supplier", width=button_width, command=lambda: Supplier.del_supplier(self.master), bg=button_bg_color, fg=button_fg_color)
        delete_button.grid(row=0, column=1, padx=10, pady=10)

        edit_button = tk.Button(supplier_buttons_frame, text="Edit Supplier", width=button_width, command=lambda: Supplier.edit_supplier(self.master), bg=button_bg_color, fg=button_fg_color)
        edit_button.grid(row=1, column=0, padx=10, pady=10)

        display_button = tk.Button(supplier_buttons_frame, text="Display Suppliers", width=button_width, command=lambda: Supplier.show(self.master), bg=button_bg_color, fg=button_fg_color)
        display_button.grid(row=1, column=1, padx=10, pady=10)

    def venue_further_menu(self):
        venue_window = tk.Toplevel(self.master)
        venue_window.title("Venue Management")
        venue_window.geometry("600x400")
        venue_window.configure(bg="#f0f0f0")

        # Create a label for the title
        title_label = tk.Label(venue_window, text="Manage Venues", font=("Helvetica", 20), bg="#f0f0f0")
        title_label.pack(pady=20)

        # Create buttons frame
        venue_buttons_frame = tk.Frame(venue_window, bg="#f0f0f0")
        venue_buttons_frame.pack()

        # Create buttons with same width
        button_width = 20

        # Define button colors
        button_bg_color = "#343a40"  # Charcoal gray
        button_fg_color = "black"

        add_button = tk.Button(venue_buttons_frame, text="Add Venue", width=button_width, command=lambda: Venue.add_venue(self.master), bg=button_bg_color, fg=button_fg_color)
        add_button.grid(row=0, column=0, padx=10, pady=10)

        delete_button = tk.Button(venue_buttons_frame, text="Delete Venue", width=button_width, command=lambda: Venue.del_venue(self.master), bg=button_bg_color, fg=button_fg_color)
        delete_button.grid(row=0, column=1, padx=10, pady=10)

        edit_button = tk.Button(venue_buttons_frame, text="Edit Venue", width=button_width, command=lambda: Venue.edit_venue(self.master), bg=button_bg_color, fg=button_fg_color)
        edit_button.grid(row=1, column=0, padx=10, pady=10)

        display_button = tk.Button(venue_buttons_frame, text="Display Venues", width=button_width, command=lambda: Venue.show(self.master), bg=button_bg_color, fg=button_fg_color)
        display_button.grid(row=1, column=1, padx=10, pady=10)

    def guest_further_menu(self):
        guest_window = tk.Toplevel(self.master)
        guest_window.title("Guest Management")
        guest_window.geometry("600x400")
        guest_window.configure(bg="#f0f0f0")

        # Create a label for the title
        title_label = tk.Label(guest_window, text="Manage Guests", font=("Helvetica", 20), bg="#f0f0f0")
        title_label.pack(pady=20)

        # Create buttons frame
        guest_buttons_frame = tk.Frame(guest_window, bg="#f0f0f0")
        guest_buttons_frame.pack()

        # Create buttons with same width
        button_width = 20

        # Define button colors
        button_bg_color = "#343a40"  # Charcoal gray
        button_fg_color = "black"

        add_button = tk.Button(guest_buttons_frame, text="Add Guest", width=button_width, command=lambda: Guest.add_guest(self.master), bg=button_bg_color, fg=button_fg_color)
        add_button.grid(row=0, column=0, padx=10, pady=10)

        delete_button = tk.Button(guest_buttons_frame, text="Delete Guest", width=button_width, command=lambda: Guest.del_guest(self.master), bg=button_bg_color, fg=button_fg_color)
        delete_button.grid(row=0, column=1, padx=10, pady=10)

        edit_button = tk.Button(guest_buttons_frame, text="Edit Guest", width=button_width, command=lambda: Guest.edit_guest(self.master), bg=button_bg_color, fg=button_fg_color)
        edit_button.grid(row=1, column=0, padx=10, pady=10)

        display_button = tk.Button(guest_buttons_frame, text="Display Guests", width=button_width, command=lambda: Guest.show(self.master), bg=button_bg_color, fg=button_fg_color)
        display_button.grid(row=1, column=1, padx=10, pady=10)

    def feedback_rating_menu(self):
        feedback_rating_window = tk.Toplevel(self.master)
        feedback_rating_window.title("Feedback & Rating")
        feedback_rating_window.geometry("400x200")
        feedback_rating_window.configure(bg="#f0f0f0")

        # Create a label for the title
        title_label = tk.Label(feedback_rating_window, text="Feedback & Rating", font=("Helvetica", 20), bg="#f0f0f0")
        title_label.pack(pady=20)

        # Create buttons frame
        feedback_rating_buttons_frame = tk.Frame(feedback_rating_window, bg="#f0f0f0")
        feedback_rating_buttons_frame.pack()

        # Create buttons with same width
        button_width = 20

        # Define button colors
        button_bg_color = "#343a40"  # Charcoal gray
        button_fg_color = "black"

        add_feedback_button = tk.Button(feedback_rating_buttons_frame, text="Add Feedback and Rating", width=button_width, command=self.add_feedback_rating, bg=button_bg_color, fg=button_fg_color)
        add_feedback_button.grid(row=0, column=0, padx=10, pady=10)

        show_feedback_button = tk.Button(feedback_rating_buttons_frame, text="Show Feedback and Rating", width=button_width, command=self.show_feedback_rating, bg=button_bg_color, fg=button_fg_color)
        show_feedback_button.grid(row=0, column=1, padx=10, pady=10)

    def add_feedback_rating(self):
        # Create a window to get input from the user
        feedback_input_window = tk.Toplevel(self.master)
        feedback_input_window.title("Add Feedback & Rating")
        feedback_input_window.geometry("400x280")  # Adjusted height to accommodate the larger comments field
        feedback_input_window.configure(bg="#f0f0f0")

        # Create labels and entry fields for user input
        name_label = tk.Label(feedback_input_window, text="Name:", bg="#f0f0f0")
        name_label.grid(row=0, column=0, padx=10, pady=10)
        name_entry = tk.Entry(feedback_input_window)
        name_entry.grid(row=0, column=1, padx=10, pady=10)

        event_label = tk.Label(feedback_input_window, text="Event:", bg="#f0f0f0")
        event_label.grid(row=1, column=0, padx=10, pady=10)
        event_entry = tk.Entry(feedback_input_window)
        event_entry.grid(row=1, column=1, padx=10, pady=10)

        rating_label = tk.Label(feedback_input_window, text="Rating:", bg="#f0f0f0")
        rating_label.grid(row=2, column=0, padx=10, pady=10)
        rating_entry = tk.Entry(feedback_input_window)
        rating_entry.grid(row=2, column=1, padx=10, pady=10)

        comments_label = tk.Label(feedback_input_window, text="Comments:", bg="#f0f0f0")
        comments_label.grid(row=3, column=0, padx=10, pady=10)
        comments_entry = tk.Text(feedback_input_window, height=5, width=30)  # Adjusted height to make the comments field bigger
        comments_entry.grid(row=3, column=1, padx=10, pady=10)

        # Create a submit button
        submit_button = tk.Button(feedback_input_window, text="Submit", command=lambda: self.add_feedback_rating(
            name_entry.get(), event_entry.get(), rating_entry.get(), comments_entry.get("1.0", tk.END)), bg="#343a40", fg="black")
        submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Function to add feedback
        def add_feedback(name, event, rating, comments):
            # Create a dictionary to store feedback data
            feedback_data = {
                "Name": name,
                "Event": event,
                "Rating": rating,
                "Comments": comments
            }

            # Load existing feedback data from file
            try:
                with open("feedback_pkl.pkl", "rb") as file:
                    existing_feedback = pickle.load(file)
            except FileNotFoundError:
                existing_feedback = []

            # Append new feedback to existing data
            existing_feedback.append(feedback_data)

            # Save updated feedback data to file
            with open("feedback_pkl.pkl", "wb") as file:
                pickle.dump(existing_feedback, file)

            # Close the feedback input window after submitting
            feedback_input_window.destroy()

        # Call the add_feedback function when the submit button is clicked
        submit_button.config(command=lambda: add_feedback(name_entry.get(), event_entry.get(), rating_entry.get(), comments_entry.get("1.0", tk.END)))

    def show_feedback_rating(self):
        # Load feedback data from file
        try:
            with open("feedback_pkl.pkl", "rb") as file:
                feedback_data = pickle.load(file)
        except FileNotFoundError:
            feedback_data = []

        # Create a window to display feedback data
        show_feedback_window = tk.Toplevel(self.master)
        show_feedback_window.title("Feedback & Rating")
        show_feedback_window.geometry("600x400")
        show_feedback_window.configure(bg="#f0f0f0")

        # Create a label for the title
        title_label = tk.Label(show_feedback_window, text="Feedback & Rating", font=("Helvetica", 20), bg="#f0f0f0")
        title_label.pack(pady=20)

        # Create a frame to hold feedback entries
        feedback_frame = tk.Frame(show_feedback_window, bg="#f0f0f0")
        feedback_frame.pack()

        # Display feedback data
        for i, feedback in enumerate(feedback_data, start=1):
            feedback_label = tk.Label(feedback_frame, text=f"Feedback {i}", font=("Helvetica", 12, "bold"), bg="#f0f0f0")
            feedback_label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

            name_label = tk.Label(feedback_frame, text=f"Name: {feedback['Name']}", bg="#f0f0f0")
            name_label.grid(row=i, column=1, padx=10, pady=5, sticky="w")

            event_label = tk.Label(feedback_frame, text=f"Event: {feedback['Event']}", bg="#f0f0f0")
            event_label.grid(row=i, column=2, padx=10, pady=5, sticky="w")

            rating_label = tk.Label(feedback_frame, text=f"Rating: {feedback['Rating']}", bg="#f0f0f0")
            rating_label.grid(row=i, column=3, padx=10, pady=5, sticky="w")

            comments_label = tk.Label(feedback_frame, text=f"Comments: {feedback['Comments']}", bg="#f0f0f0", justify="left")
            comments_label.grid(row=i, column=4, padx=10, pady=5, sticky="w")

        # If there are no feedback entries, display a message
        if not feedback_data:
            no_feedback_label = tk.Label(show_feedback_window, text="No feedback available.", font=("Helvetica", 12), bg="#f0f0f0")
            no_feedback_label.pack(pady=20)

def main():
    root = tk.Tk()
    app = MainTkinterFrontend(root)
    root.mainloop()

if __name__ == "__main__":
    main()
