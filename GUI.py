import tkinter as tk
import os
import sys
from Matcher import Matcher

executable_dir = os.path.dirname(os.path.abspath(sys.executable))
# executable_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(executable_dir, "data.txt")

matching_preferences = []
file_name_data = []
exchanger_data = []
exchanger_preference = []
buddy_data = []
buddy_preference = []

window = tk.Tk()
window.title("Buddy Matching")
window.geometry("650x600")
window.resizable(True, True)

# Create a scrollable frame within the window without a scollbar
canvas = tk.Canvas(window, highlightthickness=0)
scrollable_frame = tk.Frame(canvas, highlightthickness=0)
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(
    scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.pack(side="left", fill="both", expand=True)

button_frame = tk.Frame(scrollable_frame)

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


def add_column(frame, entry="Column Name"):
    row = frame.grid_size()[1]
    temp_entry = tk.Entry(frame, width=50)
    temp_entry.insert(0, entry)
    temp_entry.grid(row=row, column=0, sticky=tk.W)
    button = tk.Button(frame, text="Delete", command=lambda: delete_column(
        frame, row))
    button.grid(row=row, column=0, sticky=tk.W, padx=470)


def delete_column(frame, row):
    for entry in frame.winfo_children():
        if entry.grid_info().get("row") == row:
            entry.destroy()


def add_labels(data, frame):
    for entry in data:
        add_column(frame, entry)


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


def add_matching_preferences_label(data, frame):
    matching_preferences_title = tk.Label(
        frame, text="Matching Preferences: ")
    matching_preferences_title.grid(row=0, column=0, sticky=tk.W)
    num_of_exchanger_per_buddy = tk.Label(
        frame, text="Max Number of Exchangers per Buddy: ")
    num_of_exchanger_per_buddy.grid(row=1, column=0, sticky=tk.W)
    num_of_exchanger_per_buddy_entry = tk.Entry(frame, width=20)
    if len(data) > 0:
        num_of_exchanger_per_buddy_entry.insert(0, data[0])
    num_of_exchanger_per_buddy_entry.grid(
        row=1, column=1, sticky=tk.W)
    percentage_of_buddies_with_max_exchangers = tk.Label(
        frame, text="Percentage of Buddies with Max Exchangers: ")
    percentage_of_buddies_with_max_exchangers.grid(
        row=2, column=0, sticky=tk.W)
    percentage_of_buddies_with_max_exchangers_entry = tk.Entry(frame, width=20)
    if len(data) > 1:
        percentage_of_buddies_with_max_exchangers_entry.insert(0, data[1])
    percentage_of_buddies_with_max_exchangers_entry.grid(
        row=2, column=1, sticky=tk.W)


def fill_file_name_data(data, frame):
    file_name_title = tk.Label(
        frame, text="Input the Name of Files Below: ")
    file_name_title.grid(row=0, column=0, sticky=tk.W)
    exchanger_file_name = tk.Label(
        frame, text="Exchanger Excel File Name: ")
    exchanger_file_name.grid(row=1, column=0, sticky=tk.W)
    exchanger_entry = tk.Entry(frame, width=40)
    if len(data) > 0:
        exchanger_entry.insert(0, data[0])
    exchanger_entry.grid(row=1, column=2)
    buddy_file_name = tk.Label(frame, text="Buddy Excel File Name: ")
    buddy_file_name.grid(row=2, column=0, sticky=tk.W)
    buddy_entry = tk.Entry(frame, width=40)
    if len(data) > 1:
        buddy_entry.insert(0, data[1])
    buddy_entry.grid(row=2, column=2)
    output_file_name = tk.Label(
        frame, text="Matching Output Excel File Name: ")
    output_file_name.grid(row=3, column=0, sticky=tk.W)
    output_entry = tk.Entry(frame, width=40)
    if len(data) > 2:
        output_entry.insert(0, data[2])
    output_entry.grid(row=3, column=2)


def save():
    matching_preferences.clear()
    file_name_data.clear()
    exchanger_data.clear()
    exchanger_preference.clear()
    buddy_data.clear()
    buddy_preference.clear()

    for widget in scrollable_frame.winfo_children():
        if isinstance(widget, tk.Frame):
            for entry in widget.winfo_children():
                if isinstance(entry, tk.Entry):
                    if widget.winfo_children()[0].cget("text") == "Matching Preferences: " and entry.get() != "":
                        matching_preferences.append(entry.get())
                    elif widget.winfo_children()[0].cget("text") == "Input the Name of Files Below: " and entry.get() != "":
                        file_name_data.append(entry.get())
                    elif widget.winfo_children()[0].cget("text") == "Input the Name of Columns from the Exchanger Excel You Want to Appear in the Output File Below: " and entry.get() != "":
                        exchanger_data.append(entry.get())
                    elif widget.winfo_children()[0].cget("text") == "Input the Name of Corresponding Compulsory Columns from Exchangers Excel Below: " and entry.get() != "":
                        exchanger_preference.append(entry.get())
                    elif widget.winfo_children()[0].cget("text") == "Input the Name of Columns from the Buddy Excel You Want to Appear in the Output File Below: " and entry.get() != "":
                        buddy_data.append(entry.get())
                    elif widget.winfo_children()[0].cget("text") == "Input the Name of Corresponding Compulsory Columns from Buddies Excel Below: " and entry.get() != "":
                        buddy_preference.append(entry.get())

    with open(file_path, "w") as data_file:
        for entry in matching_preferences:
            data_file.write(entry + "\n")
        data_file.write("end!@#$%^&*()\n")
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

    for i in range(len(file_name_data)):
        temp = "../../../"
        file_name_data[i] = temp + file_name_data[i]
        file_name_data[i] = os.path.join(executable_dir, file_name_data[i])

    try:
        if len(matching_preferences) > 0:
            matching_preferences[0] = int(matching_preferences[0])
        if len(matching_preferences) > 1:
            matching_preferences[1] = float(matching_preferences[1])
    except ValueError:
        temp_label = tk.Label(
            button_frame, text="Please ensure that inputs for matching preferences are numbers")
        temp_label.grid(row=1, column=1)

        temp_label.after(4000, temp_label.destroy)
        return

    temp_label = tk.Label(button_frame, text="Data saved successfully!")
    temp_label.grid(row=1, column=1)

    temp_label.after(4000, temp_label.destroy)


def load():
    try:
        with open(file_path, "r") as data_file:
            matching_preferences.clear()
            file_name_data.clear()
            exchanger_data.clear()
            exchanger_preference.clear()
            buddy_data.clear()
            buddy_preference.clear()

            for line in data_file:
                if line.strip() == "end!@#$%^&*()":
                    break
                matching_preferences.append(int(line.strip()))
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

            matching_preferences_frame = tk.Frame(scrollable_frame)
            matching_preferences_frame.pack(
                side=tk.TOP, anchor=tk.W, padx=10, pady=10)
            file_name_frame = tk.Frame(scrollable_frame)
            file_name_frame.pack(side=tk.TOP, anchor=tk.W, padx=10, pady=10)

            exchanger_data_frame = tk.Frame(scrollable_frame)
            exchanger_data_frame.pack(
                side=tk.TOP, anchor=tk.W, padx=10, pady=10)
            exchanger_data_title = tk.Label(
                exchanger_data_frame, text="Input the Name of Columns from the Exchanger Excel You Want to Appear in the Output File Below: ")
            exchanger_data_title.grid(row=0, column=0, sticky=tk.W)
            exchanger_edit_frame = tk.Frame(scrollable_frame)
            exchanger_edit_frame.pack(
                side=tk.TOP, anchor=tk.W, padx=10, pady=10)
            tk.Button(exchanger_edit_frame, text="Add Column", command=lambda: add_column(
                exchanger_data_frame)).grid(row=0, column=0, sticky=tk.W)

            exchanger_preference_frame = tk.Frame(scrollable_frame)
            exchanger_preference_frame.pack(
                side=tk.TOP, anchor=tk.W, padx=10, pady=10)
            exchanger_preference_title = tk.Label(
                exchanger_preference_frame, text="Input the Name of Corresponding Compulsory Columns from Exchangers Excel Below: ")
            exchanger_preference_title.grid(row=0, column=0, sticky=tk.W)

            buddy_data_frame = tk.Frame(scrollable_frame)
            buddy_data_frame.pack(side=tk.TOP, anchor=tk.W, padx=10, pady=10)
            buddy_data_title = tk.Label(
                buddy_data_frame, text="Input the Name of Columns from the Buddy Excel You Want to Appear in the Output File Below: ")
            buddy_data_title.grid(row=0, column=0, sticky=tk.W)
            buddy_edit_frame = tk.Frame(scrollable_frame)
            buddy_edit_frame.pack(
                side=tk.TOP, anchor=tk.W, padx=10, pady=10)
            tk.Button(buddy_edit_frame, text="Add Column", command=lambda: add_column(
                buddy_data_frame)).grid(row=0, column=0, sticky=tk.W)

            buddy_preference_frame = tk.Frame(scrollable_frame)
            buddy_preference_frame.pack(
                side=tk.TOP, anchor=tk.W, padx=10, pady=10)
            buddy_preference_title = tk.Label(
                buddy_preference_frame, text="Input the Name of Corresponding Compulsory Columns from Buddies Excel Below: ")
            buddy_preference_title.grid(row=0, column=0, sticky=tk.W)

            add_matching_preferences_label(
                matching_preferences, matching_preferences_frame)
            fill_file_name_data(file_name_data, file_name_frame)
            add_labels(exchanger_data, exchanger_data_frame)
            add_preference_label(exchanger_preference,
                                 exchanger_preference_frame)
            add_labels(buddy_data, buddy_data_frame)
            add_preference_label(buddy_preference, buddy_preference_frame)

            for i in range(len(file_name_data)):
                file_name_data[i] = os.path.join(
                    executable_dir, file_name_data[i])

    except FileNotFoundError:
        with open(file_path, "w") as data_file:
            pass
        load()


tk.Label(scrollable_frame, text="Welcome to Buddy Matching!").pack(
    side=tk.TOP, anchor=tk.W, padx=225, pady=10)


load()


def start_match():
    try:
        matcher = Matcher(file_name_data, exchanger_data,
                          exchanger_preference, buddy_data, buddy_preference, matching_preferences)
        matcher.match()

        temp = tk.Label(button_frame,
                        text="Matching Successful! Please check the output file")
        temp.grid(row=2, column=1)

        temp.after(4000, temp.destroy)
    except Exception as e:
        temp = tk.Label(button_frame,
                        text=e)
        temp.grid(row=2, column=1)

        temp.after(4000, temp.destroy)


tk.Label(scrollable_frame, text="Ensure that you have Saved before starting the Match").pack(
    side=tk.TOP, anchor=tk.W, padx=10)

button_frame.pack(side=tk.TOP, anchor=tk.W, padx=10)
tk.Button(button_frame, text="Save", command=save).grid(row=1, column=0)
tk.Button(button_frame, text="Match",
          command=start_match).grid(row=2, column=0)

window.mainloop()
