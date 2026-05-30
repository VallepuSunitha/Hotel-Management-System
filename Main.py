import customtkinter as ctk
from tkinter import messagebox
from db import connect
from tkinter import ttk
import random
from PIL import Image, ImageTk
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

#LOGIN
def login_screen():

    app = ctk.CTk()
    app.title("Hotel Login")

    # FULL SCREEN
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    app.geometry(f"{screen_width}x{screen_height}")

    # ================= BACKGROUND IMAGE =================
    bg_img = Image.open("assets/Hotel.jpg")
    bg_img = bg_img.resize((screen_width, screen_height))
    bg_photo = ImageTk.PhotoImage(bg_img, master=app)

    bg_label = ctk.CTkLabel(app, image=bg_photo, text="")
    bg_label.image = bg_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # ================= CENTER LOGIN CARD =================
    login_card = ctk.CTkFrame(
        app,
        width=400,
        height=430,
        fg_color="#111827",
        corner_radius=20
    )
    login_card.place(relx=0.5, rely=0.5, anchor="center")

    login_card.pack_propagate(False)

    # ================= TITLE =================
    ctk.CTkLabel(
        login_card,
        text="WELCOME BACK",
        font=("Arial", 24, "bold")
    ).pack(pady=5)

    ctk.CTkLabel(
        login_card,
        text="Login to continue",
        font=("Arial", 13),
        text_color="#cbd5e1"
    ).pack(pady=5)

    # ================= INPUT FIELDS =================
    username = ctk.CTkEntry(
        login_card,
        placeholder_text="Username",
        width=300,
        height=40
    )
    username.pack(pady=15)

    password = ctk.CTkEntry(
        login_card,
        placeholder_text="Password",
        show="*",
        width=300,
        height=40
    )
    password.pack(pady=10)

    # ================= LOGIN FUNCTION =================
    def login():

        conn = connect()
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM users WHERE username=%s AND password=%s",
            (username.get(), password.get())
        )

        if cur.fetchone():
            app.destroy()
            open_dashboard()
        else:
            messagebox.showerror("Error", "Invalid Login Credentials")

    # ================= BUTTON =================
    ctk.CTkButton(
        login_card,
        text="LOGIN",
        fg_color="#2563eb",
        hover_color="#1d4ed8",
        height=40,
        width=250,
        font=("Arial", 14, "bold"),
        command=login
    ).pack(pady=25)

    app.mainloop()


#DASHBOARD UI
def open_dashboard():

    dash = ctk.CTk()
    dash.geometry("1200x700")
    dash.title("Hotel Management Dashboard")

    # ================= GRID LAYOUT =================
    dash.grid_rowconfigure(0, weight=1)
    dash.grid_columnconfigure(1, weight=1)

    # ================= SIDEBAR =================
    sidebar = ctk.CTkFrame(dash, width=240, fg_color="#111")
    sidebar.grid(row=0, column=0, sticky="ns")
    sidebar.grid_propagate(False)

    # TITLE
    ctk.CTkLabel(
        sidebar,
        text="🏨 HOTEL SYSTEM",
        font=("Arial", 18, "bold")
    ).pack(pady=20)

    # MENU TITLE
    ctk.CTkLabel(
        sidebar,
        text="MENU",
        font=("Arial", 14)
    ).pack(pady=10)

    # ================= MAIN AREA =================
    main = ctk.CTkFrame(dash, fg_color="#0f172a")
    main.grid(row=0, column=1, sticky="nsew")

    # ================= TOP HEADER =================
    header = ctk.CTkFrame(main, fg_color="#1e1e1e", height=60)
    header.pack(fill="x", padx=20, pady=20)

    ctk.CTkLabel(
        header,
        text="Dashboard Overview",
        font=("Arial", 20, "bold")
    ).pack(side="left", padx=20)

    # ================= DASH CARDS =================
    card_frame = ctk.CTkFrame(main, fg_color="transparent")
    card_frame.pack(fill="x", padx=20)

    # CARD 1
    card1 = ctk.CTkFrame(card_frame, fg_color="#1f6feb", width=250, height=120, corner_radius=15)
    card1.pack(side="left", padx=15, pady=10)
    card1.pack_propagate(False)

    ctk.CTkLabel(card1, text="TOTAL ROOMS", font=("Arial", 14, "bold")).pack(pady=10)
    ctk.CTkLabel(card1, text="50", font=("Arial", 28, "bold")).pack()

    # CARD 2
    card2 = ctk.CTkFrame(card_frame, fg_color="#16a34a", width=250, height=120, corner_radius=15)
    card2.pack(side="left", padx=15, pady=10)
    card2.pack_propagate(False)

    ctk.CTkLabel(card2, text="BOOKED", font=("Arial", 14, "bold")).pack(pady=10)
    ctk.CTkLabel(card2, text="32", font=("Arial", 28, "bold")).pack()

    # CARD 3
    card3 = ctk.CTkFrame(card_frame, fg_color="#dc2626", width=250, height=120, corner_radius=15)
    card3.pack(side="left", padx=15, pady=10)
    card3.pack_propagate(False)

    ctk.CTkLabel(card3, text="AVAILABLE", font=("Arial", 14, "bold")).pack(pady=10)
    ctk.CTkLabel(card3, text="18", font=("Arial", 28, "bold")).pack()

    # ================= BUTTONS =================
    ctk.CTkButton(
    sidebar,
    text="🛏 Rooms",
    fg_color="#7c3aed",
    hover_color="#a855f7",
    command=lambda: show_rooms(main)
).pack(pady=10, fill="x", padx=10)
    
    ctk.CTkButton(
        sidebar,
        text="🏨 Booking",
        fg_color="#1f6feb",
        hover_color="#3b82f6",
        command=lambda: show_booking(main)
    ).pack(pady=10, fill="x", padx=10)

    ctk.CTkButton(
        sidebar,
        text="📄 View Bookings",
        fg_color="#16a34a",
        hover_color="#22c55e",
        command=lambda: show_table(main)
    ).pack(pady=10, fill="x", padx=10)

    ctk.CTkButton(
        sidebar,
        text="🗑 Delete Booking",
        fg_color="#dc2626",
        hover_color="#ef4444",
        command=lambda: delete_booking_ui(main)
    ).pack(pady=10, fill="x", padx=10)

    ctk.CTkButton(
        sidebar,
        text="🚪 Logout",
        fg_color="#374151",
        hover_color="#6b7280",
        command=lambda: confirm_logout(dash)
    ).pack(pady=20, fill="x", padx=10)

    # DEFAULT PAGE
    show_rooms(main)

    dash.mainloop()


#Rooms
def show_rooms(frame):

    for widget in frame.winfo_children():
        widget.destroy()

    # TITLE BAR
    header = ctk.CTkFrame(frame, fg_color="transparent")
    header.pack(fill="x", pady=10)

    ctk.CTkLabel(
        header,
        text="ROOMS MANAGEMENT",
        font=("Arial", 26, "bold")
    ).pack()

    # OUTER FRAME
    outer = ctk.CTkFrame(frame, fg_color="transparent")
    outer.pack(fill="both", expand=True)

    # CANVAS (SCROLL AREA)
    canvas = ctk.CTkCanvas(outer, highlightthickness=0, bg="#0b1220")
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = ttk.Scrollbar(outer, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    # INNER CONTAINER
    container = ctk.CTkFrame(canvas, fg_color="transparent")
    canvas_window = canvas.create_window((0, 0), window=container, anchor="n")

    # CENTER FIX
    def resize(event):
        canvas.itemconfig(canvas_window, width=event.width)

    canvas.bind("<Configure>", resize)

    def update_scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    container.bind("<Configure>", update_scroll)

    # GRID CONFIG (3 COLUMNS)
    cols = 3
    for i in range(cols):
        container.grid_columnconfigure(i, weight=1, uniform="cols")

    # FETCH DATA
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT room_no, type, price, status FROM rooms")
    rooms = cur.fetchall()

    row, col = 0, 0

    def on_enter(e, w):
        w.configure(fg_color="#262626")

    def on_leave(e, w):
        w.configure(fg_color="#1e1e1e")

    for r in rooms:

        card = ctk.CTkFrame(
            container,
            fg_color="#1e1e1e",
            corner_radius=20,
            height=250
        )

        card.grid(row=row, column=col, padx=18, pady=18, sticky="nsew")
        card.grid_propagate(False)

        # HOVER EFFECT
        card.bind("<Enter>", lambda e, w=card: on_enter(e, w))
        card.bind("<Leave>", lambda e, w=card: on_leave(e, w))

        # IMAGE
        try:
            img = Image.open("assets/rooms.jpg")
            img = img.resize((150, 100))
            photo = ImageTk.PhotoImage(img, master=card)

            img_label = ctk.CTkLabel(card, image=photo, text="")
            img_label.image = photo
            img_label.pack(pady=10)

        except:
            ctk.CTkLabel(card, text="🏨 Room Image").pack(pady=10)

        # ROOM NUMBER
        ctk.CTkLabel(
            card,
            text=f"Room {r[0]}",
            font=("Arial", 17, "bold")
        ).pack()

        # TYPE
        ctk.CTkLabel(
            card,
            text=f"{r[1]} Room",
            font=("Arial", 13),
            text_color="#cbd5e1"
        ).pack()

        # PRICE
        ctk.CTkLabel(
            card,
            text=f"₹{r[2]} / night",
            font=("Arial", 13),
            text_color="#cbd5e1"
        ).pack()

        # STATUS BADGE (PREMIUM STYLE)
        status = r[3]

        if status == "Available":
            color = "#16a34a"   # green
        elif status == "Booked":
            color = "#dc2626"   # red
        else:
            color = "#f59e0b"   # yellow

        badge = ctk.CTkLabel(
            card,
            text=status,
            fg_color=color,
            text_color="white",
            corner_radius=20,
            width=100,
            height=25,
            font=("Arial", 12, "bold")
        )
        badge.pack(pady=8)

        # GRID CONTROL
        col += 1
        if col == cols:
            col = 0
            row += 1


#ShowBooking
#Showing Booking
def show_booking(frame):

    for widget in frame.winfo_children():
        widget.destroy()

    ctk.CTkLabel(
        frame,
        text="BOOK ROOM",
        font=("Arial", 24, "bold")
    ).pack(pady=20)

    card = ctk.CTkFrame(
        frame,
        width=450,
        height=520,
        fg_color="#1e1e1e",
        corner_radius=20
    )
    card.pack(pady=20)
    card.pack_propagate(False)

    ctk.CTkLabel(
        card,
        text="Enter Booking Details",
        font=("Arial",18,"bold")
    ).pack(pady=15)

    name = ctk.CTkEntry(card, placeholder_text="Customer Name", width=320, height=40)
    name.pack(pady=8)

    phone = ctk.CTkEntry(card, placeholder_text="Phone Number", width=320, height=40)
    phone.pack(pady=8)

    room = ctk.CTkEntry(card, placeholder_text="Room No", width=320, height=40)
    room.pack(pady=8)

    days = ctk.CTkEntry(card, placeholder_text="Number of Days", width=320, height=40)
    days.pack(pady=8)

    def book():

        if not name.get() or not phone.get() or not room.get() or not days.get():
            messagebox.showerror("Error","All fields required")
            return

        conn = connect()
        cur = conn.cursor()

        from datetime import date, timedelta

        bill = int(days.get()) * 1500

        check_in = date.today()
        check_out = check_in + timedelta(days=int(days.get()))

        # INSERT BOOKING
        cur.execute("""
        INSERT INTO bookings
        (name,phone,room_no,days,bill,status,booking_date)
        VALUES(%s,%s,%s,%s,%s,'Booked',NOW())
        """,
        (
            name.get(),
            phone.get(),
            room.get(),
            days.get(),
            bill
        ))

        # UPDATE ROOM STATUS
        cur.execute("""
        UPDATE rooms
        SET status='Booked',
            check_in=%s,
            check_out=%s
        WHERE room_no=%s
        """,
        (
            check_in,
            check_out,
            room.get()
        ))

        conn.commit()

        messagebox.showinfo(
            "Success",
            f"Room Booked!\nBill: ₹{bill}\nCheck-in: {check_in}\nCheck-out: {check_out}"
        )

        # CLEAR INPUTS
        name.delete(0,"end")
        phone.delete(0,"end")
        room.delete(0,"end")
        days.delete(0,"end")

    # BOOK BUTTON ← THIS WAS MISSING
    ctk.CTkButton(
        card,
        text="BOOK NOW",
        fg_color="#2563eb",
        hover_color="#1d4ed8",
        width=220,
        height=45,
        font=("Arial",14,"bold"),
        command=book
    ).pack(pady=20)






#SHOW TABLE
def show_table(frame):

    for widget in frame.winfo_children():
        widget.destroy()

    # TITLE
    ctk.CTkLabel(
        frame,
        text="BOOKING MANAGEMENT",
        font=("Arial", 24, "bold")
    ).pack(pady=10)

    # TOP CONTROL BAR
    top_bar = ctk.CTkFrame(frame, fg_color="#1e1e1e")
    top_bar.pack(fill="x", padx=20, pady=10)

    search_entry = ctk.CTkEntry(top_bar, placeholder_text="Search by Name / Room")
    search_entry.pack(side="left", padx=10, pady=10)

    # TABLE FRAME
    table_frame = ctk.CTkFrame(frame, fg_color="#1e1e1e", corner_radius=15)
    table_frame.pack(fill="both", expand=True, padx=20, pady=10)

    # STYLE
    style = ttk.Style()
    style.theme_use("default")

    style.configure(
        "Treeview",
        background="#2b2b2b",
        foreground="white",
        rowheight=32,
        fieldbackground="#2b2b2b",
        borderwidth=0
    )

    style.configure(
        "Treeview.Heading",
        background="#111",
        foreground="white",
        font=("Arial", 11, "bold")
    )

    style.map("Treeview", background=[("selected", "#1f6feb")])

    # SCROLLBAR
    scroll_y = ttk.Scrollbar(table_frame, orient="vertical")

    table = ttk.Treeview(
        table_frame,
        columns=("ID","Name","Phone","Room","Days","Bill","CheckIn","Status"),
        show="headings",
        yscrollcommand=scroll_y.set
    )

    scroll_y.config(command=table.yview)
    scroll_y.pack(side="right", fill="y")

    for col in ("ID","Name","Phone","Room","Days","Bill","CheckIn","Status"):
        table.heading(col, text=col)
        table.column(col, anchor="center", width=120)

    # LOAD DATA FUNCTION
    def load_data(filter_text=""):
        for row in table.get_children():
            table.delete(row)

        conn = connect()
        cur = conn.cursor()

        if filter_text:
            query = """
            SELECT * FROM bookings
            WHERE name LIKE %s OR room_no LIKE %s
            """
            cur.execute(query, (f"%{filter_text}%", f"%{filter_text}%"))
        else:
            cur.execute("""
            SELECT id,name,phone,room_no,days,bill,booking_date,status
            FROM bookings
            """)

        rows = cur.fetchall()

        for row in rows:

            formatted_date = row[6].strftime("%d-%m-%Y %I:%M %p")

        new_row = (
        row[0],   # ID
        row[1],   # Name
        row[2],   # Phone
        row[3],   # Room
        row[4],   # Days
        row[5],   # Bill
        formatted_date,
        row[7]
    )

        status = row[7]

        if status == "Vacated":

            table.insert(
            "",
            "end",
            values=new_row,
            tags=("vacated",)
        )

        else:
  
            table.insert(
            "",
            "end",
            values=new_row,
            tags=("booked",)
        )

        table.tag_configure(
    "vacated",
    background="#facc15",
    foreground="black"
)

        table.tag_configure(
    "booked",
    background="#2b2b2b",
    foreground="white"
)

    load_data()

    table.pack(fill="both", expand=True)

    # SEARCH FUNCTION
    def search():
        load_data(search_entry.get())

    # BUTTONS
    btn_frame = ctk.CTkFrame(frame, fg_color="#1e1e1e")
    btn_frame.pack(fill="x", padx=20, pady=10)

    ctk.CTkButton(
        btn_frame,
        text="🔍 Search",
        fg_color="#1f6feb",
        command=search
    ).pack(side="left", padx=10)

    ctk.CTkButton(
        btn_frame,
        text="🔄 Refresh",
        fg_color="#16a34a",
        command=lambda: load_data()
    ).pack(side="left", padx=10)



        


def delete_booking_ui(frame):

    for widget in frame.winfo_children():
        widget.destroy()

    ctk.CTkLabel(
        frame,
        text="MANAGE BOOKINGS (VACATE / DELETE)",
        font=("Arial", 24, "bold")
    ).pack(pady=15)

    # TABLE FRAME
    table_frame = ctk.CTkFrame(frame, fg_color="#1e1e1e")
    table_frame.pack(pady=20, padx=20, fill="both", expand=True)

    scroll = ttk.Scrollbar(table_frame, orient="vertical")

    table = ttk.Treeview(
        table_frame,
        columns=("ID","Name","Phone","Room","Days","Bill","CheckIn","Status"),
        show="headings",
        yscrollcommand=scroll.set
    )

    scroll.config(command=table.yview)
    scroll.pack(side="right", fill="y")

    for col in ("ID","Name","Phone","Room","Days","Bill","CheckIn","Status"):
        table.heading(col, text=col)
        table.column(col, anchor="center", width=120)

    conn = connect()
    cur = conn.cursor()
    cur.execute("""
SELECT id,name,phone,room_no,days,bill,booking_date,status
FROM bookings
""")
    rows = cur.fetchall()

    for row in rows:

        formatted_date = row[6].strftime("%d-%m-%Y %I:%M %p")

    new_row = (
        row[0],   # ID
        row[1],   # Name
        row[2],   # Phone
        row[3],   # Room
        row[4],   # Days
        row[5],   # Bill
        formatted_date,
        row[7]
    )

    status = row[7]

    if status == "Vacated":

        table.insert(
            "",
            "end",
            values=new_row,
            tags=("vacated",)
        )

    else:

        table.insert(
            "",
            "end",
            values=new_row,
            tags=("booked",)
        )
    table.tag_configure(
    "vacated",
    background="#facc15",
    foreground="black"
)

    table.tag_configure(
    "booked",
    background="#2b2b2b",
    foreground="white"
)

    table.pack(fill="both", expand=True)

    # STORE SELECTED ROW
    selected_data = {"id": None, "room": None}

    def on_select(event):
        selected = table.focus()
        data = table.item(selected)["values"]
        if data:
            selected_data["id"] = data[0]
            selected_data["room"] = data[3]

    table.bind("<<TreeviewSelect>>", on_select)

    # ================= VACATE =================
    def vacate():

        if not selected_data["id"]:
            messagebox.showerror("Error", "Select a booking first")
            return

        conn = connect()
        cur = conn.cursor()

        cur.execute("UPDATE bookings SET status='Vacated' WHERE id=%s",
                    (selected_data["id"],))

        cur.execute("UPDATE rooms SET status='Available' WHERE room_no=%s",
                    (selected_data["room"],))

        conn.commit()

        messagebox.showinfo("Success", "Room marked as VACATED")
        delete_booking_ui(frame)

    # ================= DELETE =================
    def delete():

        if not selected_data["id"]:
            messagebox.showerror("Error", "Select a booking first")
            return

        confirm = messagebox.askyesno("Confirm", "Delete booking permanently?")

        if confirm:

            conn = connect()
            cur = conn.cursor()

            cur.execute("DELETE FROM bookings WHERE id=%s",
                        (selected_data["id"],))

            cur.execute("UPDATE rooms SET status='Available' WHERE room_no=%s",
                        (selected_data["room"],))

            conn.commit()

            messagebox.showinfo("Success", "Booking Deleted")
            delete_booking_ui(frame)

    # ================= BUTTONS =================
    btn_frame = ctk.CTkFrame(frame, fg_color="transparent")
    btn_frame.pack(pady=10)

    ctk.CTkButton(
        btn_frame,
        text="🟡 VACATE ROOM",
        fg_color="#f59e0b",
        hover_color="#d97706",
        command=vacate
    ).pack(side="left", padx=10)

    ctk.CTkButton(
        btn_frame,
        text="🔴 DELETE BOOKING",
        fg_color="#dc2626",
        hover_color="#ef4444",
        command=delete
    ).pack(side="left", padx=10)



def confirm_logout(dash):

    result = messagebox.askyesno(
        "Logout Confirmation",
        "Do you really want to logout?"
    )

    if result:

        messagebox.showinfo(
            "Logout",
            "You have been logged out successfully"
        )

        dash.destroy()

        # restart login screen cleanly
        login_screen()


if __name__ == "__main__":
    login_screen()