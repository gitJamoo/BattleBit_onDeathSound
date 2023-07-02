
    res_w.set(entry_res_w.get())
    file_url.set(entry_file_url.get())    
    root.destroy()  # Close the GUI window
    
    # You can perform any further operations with res_h, res_w, and file_path here
    # For example, print them to the console
    #print("res_h:", res_h)
    #print("res_w:", res_w)
    #print("File Path:", file_path)

def browse_file():
    file_url = filedialog.askopenfilename()
    entry_file_url.delete(0, tk.END)
    entry_file_url.insert(tk.END, file_url)

root = tk.Tk()

# ur screens resolution
res_w = tk.IntVar()
res_h = tk.IntVar()
file_url = tk.StringVar()

root.title("Variable Input")

# Create the labels and entry fields for res_h, res_w, and file_path
label_res_w = tk.Label(root, text="Enter Resolution width:")
label_res_w.pack()

entry_res_w = tk.Entry(root)
entry_res_w.pack()

label_res_h = tk.Label(root, text="Enter Resolution height:")
label_res_h.pack()

entry_res_h = tk.Entry(root)
entry_res_h.pack()

label_file_url = tk.Label(root, text="Select Sound File:")
label_file_url.pack()

entry_file_url = tk.Entry(root)
entry_file_url.pack()

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack()

# Create the submit button
submit_button = tk.Button(root, text="Submit", command=submit_values)
submit_button.pack()

root.mainloop()

# VIEWBOX COMMANDS, these are special numbers to find where death text is displayed DO NOT MESS WITH!!!
left = res_w.get() * .44921875
upper = res_h.get() * .5555555556
right = res_w.get() * .546875