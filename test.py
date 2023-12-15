import tkinter as tk
import os

class ProjectRunner:
    def __init__(self, master):
        self.master = master
        master.title("Criminal detection system")
        master.configure(bg="#202d42") 
        tk.Label(text="Criminal Detection System", fg="white", bg="#202d42",
        font="Arial 35 bold", pady=20).pack()

        self.project_a_button = tk.Button(master, text="A", command=self.run_project_a, font="Arial 15 bold", padx=20, bg="#2196f3",
            fg="white", pady=10, bd=0, highlightthickness=0, activebackground="#091428",
            activeforeground="white")
        self.project_a_button.pack(pady=10) 

        self.project_b_button = tk.Button(master, text="B", command=self.run_project_b, font="Arial 15 bold", padx=20, bg="#2196f3",
            fg="white", pady=10, bd=0, highlightthickness=0, activebackground="#091428",
            activeforeground="white")
        self.project_b_button.pack(pady=10)

      
        self.project_a_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        self.project_b_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    def run_project_a(self):
        project_a_path = "C:\\Users\\HP\\Desktop\\final year project\\Criminal-Identification-System-master-master"
        os.chdir(project_a_path)
        os.system("python home.py")
        os.chdir("..")

    def run_project_b(self):
        project_b_path = "C:\\Users\\HP\\Desktop\\new\\Facial-Recognition-for-Crime-Detection-master"
        os.chdir(project_b_path)
        os.system("python home.py")
        os.chdir("..")

root = tk.Tk()
project_runner = ProjectRunner(root)
root.mainloop()
