import tkinter as tk
def make_read_only():
    text_widget.config(state=tk.DISABLED)

root = tk.Tk()

text_widget = tk.Text(root, height=4, width=30)
text_widget.insert(tk.END, "Editable Text")
text_widget.pack()

readonly_button = tk.Button(root, text="Make Read-Only", command=make_read_only)
readonly_button.pack()

root.mainloop()
