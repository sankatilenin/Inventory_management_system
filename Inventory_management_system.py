import tkinter as tk
from tkinter import messagebox, ttk

class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("500x400")
        
        self.products = {}
        
        # Labels and Entries
        tk.Label(root, text="Product Name:").grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(root, text="Quantity:").grid(row=1, column=0, padx=10, pady=5)
        self.qty_entry = tk.Entry(root)
        self.qty_entry.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(root, text="Price:").grid(row=2, column=0, padx=10, pady=5)
        self.price_entry = tk.Entry(root)
        self.price_entry.grid(row=2, column=1, padx=10, pady=5)
        
        # Buttons
        tk.Button(root, text="Add/Update Product", command=self.add_update_product).grid(row=3, column=0, columnspan=2, pady=5)
        tk.Button(root, text="Remove Product", command=self.remove_product).grid(row=4, column=0, columnspan=2, pady=5)
        
        # Product List
        self.tree = ttk.Treeview(root, columns=("Name", "Quantity", "Price"), show="headings")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Price", text="Price")
        self.tree.grid(row=5, column=0, columnspan=2, pady=10)
        
        self.load_products()
    
    def add_update_product(self):
        name = self.name_entry.get()
        qty = self.qty_entry.get()
        price = self.price_entry.get()
        
        if not name or not qty or not price:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        self.products[name] = (qty, price)
        self.load_products()
        
    def remove_product(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Select a product to remove!")
            return
        
        item = self.tree.item(selected_item)
        del self.products[item["values"][0]]
        self.load_products()
    
    def load_products(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for name, (qty, price) in self.products.items():
            self.tree.insert("", "end", values=(name, qty, price))
        
if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()
