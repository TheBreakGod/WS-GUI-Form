import tkinter as tk
from tkinter import ttk

def submit_form():
    print("Form submitted")

def cancel_form():
    print("Form cancelled")

root = tk.Tk()
root.title("สมัครสมาชิก")

# Set the main window background color
root.configure(bg="#e0f7fa")

# Personal Information Frame
personal_frame = tk.LabelFrame(root, text="ข้อมูลส่วนตัว", padx=10, pady=10, bg="#e0f7fa", fg="#00695c", font=("Helvetica", 12, "bold"))
personal_frame.pack(padx=10, pady=10)

# Row 1
title_label = tk.Label(personal_frame, text="คำนำหน้า:", bg="#e0f7fa")
title_label.grid(row=0, column=0, sticky="e")
title_combo = ttk.Combobox(personal_frame, values=["กรุณาเลือก", "นาย", "นาง", "นางสาว"])
title_combo.grid(row=0, column=1)

# Row 2
first_name_label = tk.Label(personal_frame, text="ชื่อ:", bg="#e0f7fa")
first_name_label.grid(row=1, column=0, sticky="e")
first_name_entry = tk.Entry(personal_frame)
first_name_entry.grid(row=1, column=1)

last_name_label = tk.Label(personal_frame, text="นามสกุล:", bg="#e0f7fa")
last_name_label.grid(row=1, column=2, sticky="e")
last_name_entry = tk.Entry(personal_frame)
last_name_entry.grid(row=1, column=3)

# Row 3
dob_label = tk.Label(personal_frame, text="วันเดือนปีเกิด:", bg="#e0f7fa")
dob_label.grid(row=2, column=0, sticky="e")
dob_entry = tk.Entry(personal_frame)
dob_entry.grid(row=2, column=1)

# Row 4
gender_label = tk.Label(personal_frame, text="เพศ:", bg="#e0f7fa")
gender_label.grid(row=3, column=0, sticky="e")
gender_var = tk.StringVar()
male_radio = tk.Radiobutton(personal_frame, text="ชาย", variable=gender_var, value="ชาย", bg="#e0f7fa")
female_radio = tk.Radiobutton(personal_frame, text="หญิง", variable=gender_var, value="หญิง", bg="#e0f7fa")
male_radio.grid(row=3, column=1)
female_radio.grid(row=3, column=2)

# Row 5
email_label = tk.Label(personal_frame, text="อีเมล์:", bg="#e0f7fa")
email_label.grid(row=4, column=0, sticky="e")
email_entry = tk.Entry(personal_frame)
email_entry.grid(row=4, column=1, columnspan=3, sticky="we")

# Row 6
phone_label = tk.Label(personal_frame, text="เบอร์โทรศัพท์:", bg="#e0f7fa")
phone_label.grid(row=5, column=0, sticky="e")
phone_entry = tk.Entry(personal_frame)
phone_entry.grid(row=5, column=1, columnspan=3, sticky="we")

# Row 7
address_label = tk.Label(personal_frame, text="ที่อยู่ปัจจุบัน:", bg="#e0f7fa")
address_label.grid(row=6, column=0, sticky="ne")
address_text = tk.Text(personal_frame, height=4, width=30)
address_text.grid(row=6, column=1, columnspan=3, sticky="we")

# Row 8
subdistrict_label = tk.Label(personal_frame, text="อำเภอ:", bg="#e0f7fa")
subdistrict_label.grid(row=7, column=0, sticky="e")
subdistrict_entry = tk.Entry(personal_frame)
subdistrict_entry.grid(row=7, column=1)

province_label = tk.Label(personal_frame, text="จังหวัด:", bg="#e0f7fa")
province_label.grid(row=7, column=2, sticky="e")
province_entry = tk.Entry(personal_frame)
province_entry.grid(row=7, column=3)

# Row 9
postcode_label = tk.Label(personal_frame, text="รหัสไปรษณีย์:", bg="#e0f7fa")
postcode_label.grid(row=8, column=0, sticky="e")
postcode_entry = tk.Entry(personal_frame)
postcode_entry.grid(row=8, column=1)

# Row 10
age_label = tk.Label(personal_frame, text="อายุ:", bg="#e0f7fa")
age_label.grid(row=9, column=0, sticky="e")
age_combo = ttk.Combobox(personal_frame, values=["กรุณาเลือก"] + list(range(1, 101)))
age_combo.grid(row=9, column=1)

# Row 11
hobbies_label = tk.Label(personal_frame, text="งานอดิเรก:", bg="#e0f7fa")
hobbies_label.grid(row=10, column=0, sticky="ne")
hobbies_frame = tk.Frame(personal_frame, bg="#e0f7fa")
hobbies_frame.grid(row=10, column=1, columnspan=3, sticky="w")
hobbies_vars = {
    "อ่านหนังสือ": tk.IntVar(),
    "เล่นเกม": tk.IntVar(),
    "ดูหนัง": tk.IntVar(),
    "ฟังเพลง": tk.IntVar(),
    "ปลูกต้นไม้": tk.IntVar(),
    "ท่องเที่ยว": tk.IntVar()
}
for i, (hobby, var) in enumerate(hobbies_vars.items()):
    tk.Checkbutton(hobbies_frame, text=hobby, variable=var, bg="#e0f7fa").grid(row=i//3, column=i%3, sticky="w")

# User Information Frame
user_frame = tk.LabelFrame(root, text="ข้อมูลผู้ใช้", padx=10, pady=10, bg="#e0f7fa", fg="#00695c", font=("Helvetica", 12, "bold"))
user_frame.pack(padx=10, pady=10)

# Username and Password
username_label = tk.Label(user_frame, text="Username:", bg="#e0f7fa")
username_label.grid(row=0, column=0, sticky="e")
username_entry = tk.Entry(user_frame)
username_entry.grid(row=0, column=1)

password_label = tk.Label(user_frame, text="Password:", bg="#e0f7fa")
password_label.grid(row=1, column=0, sticky="e")
password_entry = tk.Entry(user_frame, show="*")
password_entry.grid(row=1, column=1)

# Buttons
buttons_frame = tk.Frame(root, bg="#e0f7fa")
buttons_frame.pack(padx=10, pady=10)

submit_button = tk.Button(buttons_frame, text="สมัครสมาชิก", command=submit_form, bg="#00796b", fg="white")
submit_button.grid(row=0, column=0, padx=5)

cancel_button = tk.Button(buttons_frame, text="ยกเลิก", command=cancel_form, bg="#d32f2f", fg="white")
cancel_button.grid(row=0, column=1, padx=5)

root.mainloop()
