import tkinter as tk

def display_property(root, property, add_to_favorites, request_viewing):
    frame = tk.Frame(root)
    frame.pack(pady=10)

    tk.Label(frame, text=f"Property ID: {property.property_id}").pack()
    tk.Label(frame, text=f"Address: {property.address}").pack()
    tk.Label(frame, text=f"Price: {property.price}").pack()
    tk.Label(frame, text=f"Type: {property.property_type.value}").pack()
    tk.Label(frame, text=f"Status: {property.status.value}").pack()
    tk.Label(frame, text=f"Owner: {property.owner}").pack()

    tk.Button(frame, text="Add to Favorites", command=lambda p=property: add_to_favorites(p)).pack(side=tk.LEFT)
    tk.Button(frame, text="Request Viewing", command=lambda p=property: request_viewing(p)).pack(side=tk.RIGHT)
