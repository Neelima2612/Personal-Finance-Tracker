import csv
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from database import *

# DATABASE CONNECT
connect_db()

# SET CTK GRAPHICS THEME
ctk.set_appearance_mode("dark")

class ModernFinanceTracker(ctk.CTk):
    def __init__(self, username):
        super().__init__()
        
        self.current_user = username # Store current session user

        # MAIN WINDOW SETTINGS
        self.title(f"Personal Finance Tracker - [{self.current_user}]")
        self.geometry("950x820")  
        self.configure(fg_color="#141E2E")  
        self.resizable(True, True)

        # ---- HEADER CONTAINER ----
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.pack(fill="x", pady=(20, 10))

        self.title_label = ctk.CTkLabel(
            self.header_frame,
            text="PERSONAL FINANCE TRACKER",
            font=ctk.CTkFont(family="Georgia", size=24, weight="bold"),
            text_color="#E2A786"  
        )
        self.title_label.pack()

        self.line_canvas = tk.Canvas(self.header_frame, width=320, height=2, bg="#E2A786", highlightthickness=0)
        self.line_canvas.pack(pady=(5, 5))

        # ---- DASHBOARD GRID SPLIT ----
        self.grid_container = ctk.CTkFrame(self, fg_color="transparent")
        self.grid_container.pack(fill="both", expand=True, padx=30, pady=5)
        self.grid_container.grid_columnconfigure(0, weight=4, minsize=420)  
        self.grid_container.grid_columnconfigure(1, weight=5, minsize=400)  

        # ================= LEFT SIDE: INPUT & CONTROLS =================
        self.left_frame = ctk.CTkFrame(self.grid_container, fg_color="transparent")
        self.left_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 20))

        # ENTRY CONTROLS FIELDS
        self.income_entry = self.create_input_field(self.left_frame, "Monthly Income", "Enter income")
        self.food_entry = self.create_input_field(self.left_frame, "Food Expense", "Enter food expense")
        self.travel_entry = self.create_input_field(self.left_frame, "Travel Expense", "Enter travel expense")
        self.other_entry = self.create_input_field(self.left_frame, "Other Expense", "Enter other expense")

        # ACTIONS CONTROLS BUTTONS
        self.calc_btn = self.create_styled_button(self.left_frame, "⚙️   CALCULATE REPORT", "#006680", "#0080A1", self.calculate)
        self.history_btn = self.create_styled_button(self.left_frame, "📄   Show History", "#2D3748", "#3F4E66", self.show_history)
        self.export_btn = self.create_styled_button(self.left_frame, "📥   Export CSV", "#2D3748", "#3F4E66", self.export_csv)

        self.logout_btn = ctk.CTkButton(
            self.left_frame,
            text="Logout   ↪",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="transparent",
            hover_color="#2D3748",
            text_color="#E63946",
            command=self.logout
        )
        self.logout_btn.pack(pady=(15, 5))

        # ================= RIGHT SIDE: EMBEDDED ANALYTICS =================
        self.right_frame = ctk.CTkFrame(self.grid_container, fg_color="#1E293B", corner_radius=12, border_color="#334155", border_width=1)
        self.right_frame.grid(row=0, column=1, sticky="nsew", pady=(10, 15))

        self.chart_title = ctk.CTkLabel(
            self.right_frame, 
            text="Spending Breakdown (Live)", 
            font=ctk.CTkFont(size=15, weight="bold"),
            text_color="#94A3B8"
        )
        self.chart_title.pack(pady=(15, 0))

        self.chart_canvas = None
        self.render_empty_chart()

        # ================= FOOTER DATA BANNER =================
        self.result_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.result_frame.pack(fill="x", pady=(15, 30))

        self.result_label = ctk.CTkLabel(
            self.result_frame,
            text="Total Expense: ₹0     |     Balance Left: ₹0\nHighest Spending Category: None     |     Analysis: Awaiting Input...",
            font=ctk.CTkFont(family="Arial", size=16, weight="bold"),  
            text_color="#94A3B8",
            justify="center"
        )
        self.result_label.pack()

    def create_input_field(self, parent, label_text, placeholder):
        lbl = ctk.CTkLabel(parent, text=label_text, font=ctk.CTkFont(size=13, weight="bold"), text_color="#FFFFFF")
        lbl.pack(anchor="w", padx=10, pady=(6, 2))
        
        entry = ctk.CTkEntry(
            parent,
            placeholder_text=placeholder,
            height=38,
            corner_radius=8,
            fg_color="#1E293B",
            border_color="#475569",
            text_color="#FFFFFF",
            placeholder_text_color="#64748B"
        )
        entry.pack(fill="x", padx=10, pady=(0, 6))
        return entry

    def create_styled_button(self, parent, text, fg, hover, command):
        btn = ctk.CTkButton(
            parent,
            text=text,
            height=42,
            corner_radius=8,
            font=ctk.CTkFont(size=13, weight="bold" if "CALCULATE" in text else "normal"),
            fg_color=fg,
            hover_color=hover,
            text_color="#FFFFFF",
            command=command
        )
        btn.pack(fill="x", padx=10, pady=5)
        return btn

    # ---- EMBEDDED MATPLOTLIB GRAPH LOGIC ----
    def update_embedded_chart(self, food, travel, other):
        if self.chart_canvas:
            self.chart_canvas.get_tk_widget().destroy()

        if food == 0 and travel == 0 and other == 0:
            self.render_empty_chart()
            return

        fig, ax = plt.subplots(figsize=(4, 3.2), facecolor='#1E293B')
        ax.set_facecolor("#1E293B")
        
        slices = [food, travel, other]
        labels = ['Food', 'Travel', 'Other']
        colors = ['#00B4D8', '#E2A786', '#475569']  

        ax.pie(slices, labels=labels, autopct='%1.1f%%', colors=colors, textprops={'color': '#FFFFFF', 'fontsize': 10}, startangle=90)
        ax.axis('equal')
        
        self.chart_canvas = FigureCanvasTkAgg(fig, master=self.right_frame)
        self.chart_canvas.draw()
        self.chart_canvas.get_tk_widget().pack(fill="both", expand=True, padx=20, pady=10)
        plt.close(fig)

    def render_empty_chart(self):
        fig, ax = plt.subplots(figsize=(4, 3.2), facecolor='#1E293B')
        ax.set_facecolor("#1E293B")
        ax.pie([1], labels=['No Data Entered'], colors=['#334155'], textprops={'color': '#64748B', 'fontsize': 11}, startangle=90)
        ax.axis('equal')
        self.chart_canvas = FigureCanvasTkAgg(fig, master=self.right_frame)
        self.chart_canvas.draw()
        self.chart_canvas.get_tk_widget().pack(fill="both", expand=True, padx=20, pady=10)
        plt.close(fig)

    # ---- CALCULATE FUNCTION ----
    def calculate(self):
        try:
            val_income = str(self.income_entry.get()).replace(",", "").strip()
            val_food = str(self.food_entry.get()).replace(",", "").strip()
            val_travel = str(self.travel_entry.get()).replace(",", "").strip()
            val_other = str(self.other_entry.get()).replace(",", "").strip()
            
    
            if not val_income or not val_food or not val_travel or not val_other:
                messagebox.showerror("Blank Fields", "Please fill all the boxes with numbers!")
                return

            income = float(val_income)
            food = float(val_food)
            travel = float(val_travel)
            other = float(val_other)
            
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numeric digits only!")
            return

        # 2. Database saving & calculations block
        try:
            total_expense = food + travel + other
            balance = income - total_expense

            # SAVE TO DATABASE SPECIFIC USER
            insert_transaction(self.current_user, "Expense", "Food", food)
            insert_transaction(self.current_user, "Expense", "Travel", travel)
            insert_transaction(self.current_user, "Expense", "Other", other)

            expenses = {"Food": food, "Travel": travel, "Other": other}
            highest_cat = max(expenses, key=expenses.get)

            if balance > income * 0.5:
                suggestion = "Excellent Saving Habit 💎"
                balance_color = "#2ECC71"  
            elif balance > income * 0.3:
                suggestion = "Good Financial Management 👍"
                balance_color = "#2ECC71"  
            elif balance > 0:
                suggestion = "Try reducing unnecessary expenses 📉"
                balance_color = "#E2A786"  
            else:
                suggestion = "Warning! Expenses exceeded income 🚨"
                balance_color = "#E63946"  

            self.update_embedded_chart(food, travel, other)

            self.result_label.configure(
                text=f"Total Expense: ₹{total_expense}     |     Balance Left: ₹{balance}\nHighest Spending: {highest_cat}     |     👉 Analysis: {suggestion}",
                font=ctk.CTkFont(family="Arial", size=16, weight="bold"),
                text_color=balance_color
            )

        except Exception as err:
            messagebox.showerror("Execution Error", f"Technical breakdown trace: {err}")

    def show_history(self):
        try:
            data = fetch_transactions(self.current_user)
        except:
            data = []

        history_window = ctk.CTkToplevel(self)
        history_window.title("Transaction History")
        history_window.geometry("500x420")
        history_window.configure(fg_color="#141E2E")
        history_window.after(100, lambda: history_window.focus()) 

        title = ctk.CTkLabel(history_window, text="Transaction Logging History", font=ctk.CTkFont(size=16, weight="bold"), text_color="#E2A786")
        title.pack(pady=15)

        text_box = ctk.CTkTextbox(
            history_window,
            font=("Arial", 12),
            fg_color="#1E293B",
            text_color="#FFFFFF",
            border_color="#334155",
            border_width=1,
            corner_radius=8
        )
        text_box.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        for row in data:
            text_box.insert(tk.END, f"Category: {row[0]} | Type: {row[1]} | Amount: ₹{row[2]}\n")
        text_box.configure(state="disabled")

    def export_csv(self):
        try:
            data = fetch_transactions(self.current_user)
            filename = f"{self.current_user}_transactions.csv"
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Category", "Type", "Amount"])
                for row in data:
                    writer.writerow(row)
            messagebox.showinfo("Success", f"Data exported cleanly to {filename}!")
        except Exception as e:
            messagebox.showerror("Export Failed", f"Could not export transaction histories: {e}")

    def logout(self):
        self.destroy()
        try:
            import login
        except ImportError:
            print("System File 'login.py' interface missing configuration targets.")

def start_app(username):
    app = ModernFinanceTracker(username)
    app.mainloop()

if __name__ == "__main__":
    start_app("GuestUser")