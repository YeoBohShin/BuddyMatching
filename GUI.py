import tkinter as tk
import os
from Matcher import Matcher

file_path = os.path.dirname(os.path.abspath(__file__))

file_name_data = []
exchanger_data = []
exchanger_preference = []
buddy_data = []
buddy_preference = []

window = tk.Tk()
window.title("Buddy Matching")
window.geometry("600x600")
window.resizable(True, True)

# Create a scrollable frame within the window without a scollbar
canvas = tk.Canvas(window, highlightthickness=0)
scrollable_frame = tk.Frame(canvas, highlightthickness=0)
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(
    scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.pack(side="left", fill="both", expand=True)

# Allow the user to scroll with the mouse wheel


def _on_mousewheel(event):
    if event.delta > 0:
        canvas.yview_scroll(-1, "units")
    else:
        canvas.yview_scroll(1, "units")


canvas.bind_all("<MouseWheel>", _on_mousewheel)


# ALlow the user to scroll with the arrow keys


def _on_arrow_key(event):
    if event.keysym == "Up":
        canvas.yview_scroll(-1, "units")
    elif event.keysym == "Down":
        canvas.yview_scroll(1, "units")
    elif event.keysym == "Page_Up":
        canvas.yview_scroll(-3, "pages")
    elif event.keysym == "Page_Down":
        canvas.yview_scroll(3, "pages")


canvas.bind_all("<Up>", _on_arrow_key)
canvas.bind_all("<Down>", _on_arrow_key)
canvas.bind_all("<Prior>", _on_arrow_key)
canvas.bind_all("<Next>", _on_arrow_key)


def add_column(frame):
    row = frame.grid_size()[1]
    temp_entry = tk.Entry(frame, width=60)
    temp_entry.insert(0, "Column Name")
    temp_entry.grid(row=row, column=0, sticky=tk.W)


def delete_column(frame, column_name, delete_entry):
    for entry in frame.winfo_children():
        if isinstance(entry, tk.Entry) and entry.get() == column_name:
            entry.destroy()
            break
    delete_entry.delete(0, tk.END)
    delete_entry.insert(0, "Name of Column to Delete")


def add_labels(data, frame, row=1):
    for entry in data:
        temp_entry = tk.Entry(frame, width=60)
        temp_entry.insert(0, entry)
        temp_entry.grid(row=row, column=0, sticky=tk.W)
        row += 1


def add_preference_label(data, frame):
    faculty = tk.Label(frame, text="Faculty: ")
    faculty.grid(row=1, column=0, sticky=tk.W)
    faculty_entry = tk.Entry(frame, width=40)
    if len(data) > 0:
        faculty_entry.insert(0, data[0])
    faculty_entry.grid(row=1, column=0, sticky=tk.W, padx=180)
    match_faculty = tk.Label(frame, text="Match Faculty Preference: ")
    match_faculty.grid(row=2, column=0, sticky=tk.W)
    match_faculty_entry = tk.Entry(frame, width=40)
    if len(data) > 1:
        match_faculty_entry.insert(0, data[1])
    match_faculty_entry.grid(row=2, column=0, sticky=tk.W, padx=180)
    gender = tk.Label(frame, text="Gender: ")
    gender.grid(row=3, column=0, sticky=tk.W)
    gender_entry = tk.Entry(frame, width=40)
    if len(data) > 2:
        gender_entry.insert(0, data[2])
    gender_entry.grid(row=3, column=0, sticky=tk.W, padx=180)
    match_gender = tk.Label(frame, text="Match Gender Preference: ")
    match_gender.grid(row=4, column=0, sticky=tk.W)
    match_gender_entry = tk.Entry(frame, width=40)
    if len(data) > 4:
        match_gender_entry.insert(0, data[3])
    match_gender_entry.grid(row=4, column=0, sticky=tk.W, padx=180)
    interests = tk.Label(frame, text="Interests: ")
    interests.grid(row=5, column=0, sticky=tk.W)
    interests_entry = tk.Entry(frame, width=40)
    if len(data) > 4:
        interests_entry.insert(0, data[4])
    interests_entry.grid(row=5, column=0, sticky=tk.W, padx=180)


def fill_file_name_data(data, frame):
    file_name_title = tk.Label(
        frame, text="Input File Names Below: ")
    file_name_title.grid(row=0, column=0, sticky=tk.W)
    exchanger_file_name = tk.Label(
        frame, text="Exchanger Excel File Name: ")
    exchanger_file_name.grid(row=1, column=0, sticky=tk.W)
    exchanger_entry = tk.Entry(frame, width=30)
    if len(data) > 0:
        exchanger_entry.insert(0, data[0])
    exchanger_entry.grid(row=1, column=2)
    buddy_file_name = tk.Label(frame, text="Buddy Excel File Name: ")
    buddy_file_name.grid(row=2, column=0, sticky=tk.W)
    buddy_entry = tk.Entry(frame, width=30)
    if len(data) > 1:
        buddy_entry.insert(0, data[1])
    buddy_entry.grid(row=2, column=2)
    output_file_name = tk.Label(
        frame, text="Matching Output Excel File Name: ")
    output_file_name.grid(row=3, column=0, sticky=tk.W)
    output_entry = tk.Entry(frame, width=30)
    if len(data) > 2:
        output_entry.insert(0, data[2])
    output_entry.grid(row=3, column=2)


def save():
    file_name_data.clear()
    exchanger_data.clear()
    exchanger_preference.clear()
    buddy_data.clear()
    buddy_preference.clear()

    for widget in scrollable_frame.winfo_children():
        if isinstance(widget, tk.Frame):
            for entry in widget.winfo_children():
                if isinstance(entry, tk.Entry):
                    if widget.winfo_children()[0].cget("text") == "Input File Names Below: ":
                        file_name_data.append(entry.get())
                    elif widget.winfo_children()[0].cget("text") == "Input the Name of Exchanger Excel Columns Below: ":
                        exchanger_data.append(entry.get())
                    elif widget.winfo_children()[0].cget("text") == "Input the Name of Compulsory Columns for Exchanger Below: ":
                        exchanger_preference.append(entry.get())
                    elif widget.winfo_children()[0].cget("text") == "Input the Name of Buddy Excel Columns Below: ":
                        buddy_data.append(entry.get())
                    elif widget.winfo_children()[0].cget("text") == "Input the Name of Compulsory Columns for Buddy Below: ":
                        buddy_preference.append(entry.get())

    with open(os.path.join(file_path, "data.txt"), "w") as data_file:
        for entry in file_name_data:
            data_file.write(entry + "\n")
        data_file.write("end!@#$%^&*()\n")
        for entry in exchanger_data:
            data_file.write(entry + "\n")
        data_file.write("end!@#$%^&*()\n")
        for entry in exchanger_preference:
            data_file.write(entry + "\n")
        data_file.write("end!@#$%^&*()\n")
        for entry in buddy_data:
            data_file.write(entry + "\n")
        data_file.write("end!@#$%^&*()\n")
        for entry in buddy_preference:
            data_file.write(entry + "\n")
        data_file.write("end!@#$%^&*()\n")

    temp_label = tk.Label(scrollable_frame, text="Data saved successfully!")
    temp_label.pack()

    temp_label.after(4000, temp_label.destroy)


def load():
    try:
        with open(os.path.join(file_path, "data.txt"), "r") as data_file:
            file_name_data.clear()
            exchanger_data.clear()
            buddy_data.clear()

            for line in data_file:
                if line.strip() == "end!@#$%^&*()":
                    break
                file_name_data.append(line.strip())

            for line in data_file:
                if line.strip() == "end!@#$%^&*()":
                    break
                exchanger_data.append(line.strip())

            for line in data_file:
                if line.strip() == "end!@#$%^&*()":
                    break
                exchanger_preference.append(line.strip())

            for line in data_file:
                if line.strip() == "end!@#$%^&*()":
                    break
                buddy_data.append(line.strip())

            for line in data_file:
                if line.strip() == "end!@#$%^&*()":
                    break
                buddy_preference.append(line.strip())

            file_name_frame = tk.Frame(scrollable_frame)
            file_name_frame.pack(side=tk.TOP, anchor=tk.W, padx=10, pady=10)

            exchanger_data_frame = tk.Frame(scrollable_frame)
            exchanger_data_frame.pack(
                side=tk.TOP, anchor=tk.W, padx=10, pady=10)
            exchanger_data_title = tk.Label(
                exchanger_data_frame, text="Input the Name of Exchanger Excel Columns Below: ")
            exchanger_data_title.grid(row=0, column=0, sticky=tk.W)
            exchanger_edit_frame = tk.Frame(scrollable_frame)
            exchanger_edit_frame.pack(
                side=tk.TOP, anchor=tk.W, padx=10, pady=10)
            delete_exchanger_col_name = tk.Entry(
                exchanger_edit_frame, width=20)
            delete_exchanger_col_name.insert(0, "Name of Column to Delete")
            delete_exchanger_col_name.grid(row=0, column=1, sticky=tk.W)
            tk.Button(exchanger_edit_frame, text="Delete Column", command=lambda: delete_column(
                exchanger_data_frame, delete_exchanger_col_name.get(), delete_exchanger_col_name)).grid(row=0, column=2, sticky=tk.W)
            tk.Button(exchanger_edit_frame, text="Add Column", command=lambda: add_column(
                exchanger_data_frame)).grid(row=0, column=3, sticky=tk.W)

            exchanger_preference_frame = tk.Frame(scrollable_frame)
            exchanger_preference_frame.pack(
                side=tk.TOP, anchor=tk.W, padx=10, pady=10)
            exchanger_preference_title = tk.Label(
                exchanger_preference_frame, text="Input the Name of Compulsory Columns for Exchanger Below: ")
            exchanger_preference_title.grid(row=0, column=0, sticky=tk.W)

            buddy_data_frame = tk.Frame(scrollable_frame)
            buddy_data_frame.pack(side=tk.TOP, anchor=tk.W, padx=10, pady=10)
            buddy_data_title = tk.Label(
                buddy_data_frame, text="Input the Name of Buddy Excel Columns Below: ")
            buddy_data_title.grid(row=0, column=0, sticky=tk.W)
            buddy_edit_frame = tk.Frame(scrollable_frame)
            buddy_edit_frame.pack(
                side=tk.TOP, anchor=tk.W, padx=10, pady=10)
            delete_buddy_col_name = tk.Entry(buddy_edit_frame, width=20)
            delete_buddy_col_name.insert(0, "Name of Column to Delete")
            delete_buddy_col_name.grid(row=0, column=1, sticky=tk.W)
            tk.Button(buddy_edit_frame, text="Delete Column", command=lambda: delete_column(
                buddy_data_frame, delete_buddy_col_name.get(), delete_buddy_col_name)).grid(row=0, column=2, sticky=tk.W)
            tk.Button(buddy_edit_frame, text="Add Column", command=lambda: add_column(
                buddy_data_frame)).grid(row=0, column=3, sticky=tk.W)

            buddy_preference_frame = tk.Frame(scrollable_frame)
            buddy_preference_frame.pack(
                side=tk.TOP, anchor=tk.W, padx=10, pady=10)
            buddy_preference_title = tk.Label(
                buddy_preference_frame, text="Input the Name of Compulsory Columns for Buddy Below: ")
            buddy_preference_title.grid(row=0, column=0, sticky=tk.W)

            fill_file_name_data(file_name_data, file_name_frame)
            add_labels(exchanger_data, exchanger_data_frame)
            add_preference_label(exchanger_preference,
                                 exchanger_preference_frame)
            add_labels(buddy_data, buddy_data_frame)
            add_preference_label(buddy_preference, buddy_preference_frame)

    except FileNotFoundError:
        with open(os.path.join(file_path, "data.txt"), "w") as data_file:
            pass
        load()


tk.Label(scrollable_frame, text="Welcome to Buddy Matching!").pack()


load()
for i in range(len(file_name_data)):
    file_name_data[i] = os.path.join(file_path, file_name_data[i])

matcher = Matcher(file_name_data, exchanger_data,
                  exchanger_preference, buddy_data, buddy_preference)

tk.Button(scrollable_frame, text="Save", command=save).pack()
tk.Button(scrollable_frame, text="Match", command=matcher.match).pack()

window.mainloop()
