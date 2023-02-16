import tkinter as tk
from tkinter import ttk
import openai



def get_api_key():
    # create a new window to prompt for API key
    key_window = tk.Toplevel(root)
    key_window.title("Enter OpenAI API Key")

    key_entry = tk.Entry(key_window, show="*", width=50)
    key_entry.pack(padx=10, pady=20)
    key_entry.focus_set()


    def save_key():
        openai.api_key = key_entry.get()
        key_window.destroy()

    save_button = tk.Button(key_window, text="Save", command=save_key)
    save_button.pack(pady=10)

    # wait for the window to close before continuing
    root.wait_window(key_window)

# create the main window
root = tk.Tk()
root.withdraw()

# prompt for the API key
get_api_key()

def generate_response():
    prompt = prompt_entry.get("1.0", "end-1c")
    if prompt != "":
        if prompt == "exit":
            root.destroy()
        else:
            completion = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=2048)
            response_text.delete(1.0, tk.END)
            response_text.insert(tk.END, completion.choices[0].text)

def clear_prompt():
    prompt_entry.delete(1.0, tk.END)

# show the main window
root.deiconify()
root.title("GPT Chat")
root.geometry("590x670")
root.iconbitmap("./avatar.ico")

root.tk.call("source", "Azure-ttk-theme-main/azure.tcl")
root.tk.call("set_theme", "dark")

style = ttk.Style()
style.configure("TButton", padding=5, width=78, margin=10)

big_frame = ttk.Frame(root,style='Card.TFrame', padding=(5, 6, 7, 8) )
big_frame.pack(fill="both", expand=True)

clear_button = ttk.Button(big_frame, text="Clear", command=clear_prompt, style="TButton")
clear_button.pack()

prompt_label = ttk.Label(big_frame, text="Ask Question:")
prompt_label.pack()
prompt_entry = tk.Text(big_frame, height=12, )
prompt_entry.pack()

generate_button = ttk.Button(big_frame, text="Generate", command=generate_response)
generate_button.pack()

response_label = ttk.Label(big_frame, text="Response:")
response_label.pack()
response_text = tk.Text(big_frame)
response_text.pack(side="left", fill="both", expand=True )

scrollbar = tk.Scrollbar(big_frame)
scrollbar.pack(side="right", fill="y")

response_text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=response_text.yview)

root.mainloop()