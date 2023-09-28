import tkinter as tk
import add_vocabulary
import study_vocabulary

def open_add_vocabulary_window():
    add_vocabulary.show_add_vocabulary_window()

def open_study_vocabulary_window():
    study_vocabulary.show_study_vocabulary_window()

app = tk.Tk()
app.title("Ứng dụng học từ vựng Tiếng Anh")


# Tạo tiêu đề
label_tieu_de = tk.Label(app, text="Ứng dụng học từ vựng Tiếng Anh", font=("Arial", 24))
label_tieu_de.pack(pady=20)

# Tạo nút "Thêm từ vựng"
btn_them_tu_vung = tk.Button(app, text="Thêm từ vựng", font=("Arial", 14), command=open_add_vocabulary_window)
btn_them_tu_vung.pack(pady=10)

# Tạo nút "Học từ vựng"
btn_hoc_tu_vung = tk.Button(app, text="Học từ vựng", font=("Arial", 14), command=open_study_vocabulary_window)
btn_hoc_tu_vung.pack(pady=10)

app.mainloop()
