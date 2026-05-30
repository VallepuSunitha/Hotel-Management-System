# 🏨 Hotel Management System (Python + MySQL + CustomTkinter)

## 📌 Overview
This is a desktop-based Hotel Management System built using Python, CustomTkinter, and MySQL.  
It provides a modern GUI for managing hotel rooms, bookings, and customer records.

---

## 🚀 Features

- 🔐 Login Authentication System
- 🏠 Dashboard with room statistics
- 🛏 Room Management (Grid UI view)
- 📝 Booking System with bill calculation
- 📄 View Bookings (Search & Refresh)
- 🗑 Delete Bookings (Row selection)
- 🚪 Logout functionality
- 🎨 Modern UI using CustomTkinter

---

## 🛠 Tech Stack

- Python 3.x
- CustomTkinter (GUI)
- MySQL (Database)
- Tkinter ttk (Tables)
- Pillow (Images)

---

## 🗄 Database Setup

Run this SQL before starting project:

```sql
CREATE DATABASE hotel_db;

USE hotel_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    password VARCHAR(100)
);

CREATE TABLE rooms (
    room_no INT PRIMARY KEY,
    type VARCHAR(50),
    price INT,
    status VARCHAR(50)
);

CREATE TABLE bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20),
    room_no INT,
    days INT,
    bill INT
);