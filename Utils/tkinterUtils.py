import tkinter as tk
from tkinter import ttk


def createAccountWindow(accounts):
    # Create the Tkinter window
    root = tk.Tk()
    root.title("Select Account")
    root.geometry("970x200")  # Set window size
    root.resizable(False, False)  # Prevent window resizing

    # Variable to store the selected account
    selectedAccount = None

    # Function to handle button clicks
    def selectAccount(account):
        nonlocal selectedAccount
        selectedAccount = account
        # Close the Tkinter window
        root.destroy()

    # Scrollable frame to contain the buttons
    canvas = tk.Canvas(root)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    # Create buttons for accounts
    for i, account in enumerate(accounts):
        # Create button with image and text
        button = ttk.Button(
            scrollable_frame,
            text=account.name,
            compound=tk.TOP,
            command=lambda acc=account: selectAccount(acc),
            width=20,  # Fixed width for the button
        )

        # Grid positioning
        row = i // 5
        col = i % 5
        button.grid(row=row, column=col, padx=10, pady=10)

    # Start the Tkinter event loop
    root.mainloop()

    # Return the selected account
    return selectedAccount

# Example usage:
# create_account_window(accounts)
