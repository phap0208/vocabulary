import tkinter as tk
from tkinter import messagebox
import mysql.connector


def show_add_vocabulary_window():
    add_vocabulary_window = tk.Toplevel()
    add_vocabulary_window.title("Thêm từ vựng")
    add_vocabulary_window.geometry("400x300")  # Đặt kích thước cửa sổ

    label_word = tk.Label(add_vocabulary_window, text="Từ vựng:", font=("Arial", 14))
    label_word.pack()

    entry_word = tk.Entry(add_vocabulary_window, font=("Arial", 14))
    entry_word.pack()

    label_meaning = tk.Label(add_vocabulary_window, text="Nghĩa:", font=("Arial", 14))
    label_meaning.pack()

    entry_meaning = tk.Entry(add_vocabulary_window, font=("Arial", 14))
    entry_meaning.pack()

    def add_vocabulary():
        word = entry_word.get()
        meaning = entry_meaning.get()

        if not word or not meaning:
            messagebox.showerror("Lỗi", "Vui lòng nhập từ vựng và nghĩa.")
            return

        # Kết nối đến cơ sở dữ liệu MySQL
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="vocabulary"
            )
            cursor = conn.cursor()

            # Kiểm tra xem từ vựng đã tồn tại hay chưa
            cursor.execute("SELECT * FROM vocabulary WHERE word = %s", (word,))
            existing_word = cursor.fetchone()

            if existing_word:
                messagebox.showinfo("Thông báo", "Từ vựng đã tồn tại.")
            else:
                # Thêm từ vựng mới vào cơ sở dữ liệu
                cursor.execute("INSERT INTO vocabulary (word, meaning) VALUES (%s, %s)", (word, meaning))
                conn.commit()
                messagebox.showinfo("Thông báo", "Thêm từ vựng thành công.")

            cursor.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi: {str(e)}")

    btn_add = tk.Button(add_vocabulary_window, text="Thêm từ vựng", font=("Arial", 14), command=add_vocabulary)
    btn_add.pack()

    add_vocabulary_window.mainloop()
