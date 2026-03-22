import tkinter as tk

window = tk.Tk()
window.title('To-do-list')
window.geometry("350x400")
tk.Label(window, text="Check your to-do-list and complete the assigments!").pack()

def add_assigment():
    def new_assigment():
        task_frame = tk.Frame(window)
        task_frame.pack()
        assigment=assigment_entry.get()
        assigment_entry.pack_forget() 
        confirmbtn.pack_forget()   
        tk.Label(task_frame, text=f"{assigment}").pack(side=tk.RIGHT)
        variavel_check = tk.BooleanVar()
        check=tk.Checkbutton(task_frame, variable=variavel_check).pack(side=tk.LEFT)
    assigment_entry= tk.Entry(window)
    assigment_entry.pack()
    confirmbtn = tk.Button(window, text="Confirm", command=new_assigment)
    confirmbtn.pack()

tk.Button(window, text="Add an assigment", command=add_assigment).pack()

window.mainloop()
