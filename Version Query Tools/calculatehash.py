import hashlib
import tkinter as tk
from tkinter import filedialog

def compute_sha256(file_path):
    """计算 SHA-256 哈希值"""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return "ERROR: 文件未找到！"
    except Exception as e:
        return f"ERROR: {e}"

def select_file():
    """打开文件选择窗口"""
    file_path = filedialog.askopenfilename(title="选择 .big 文件", filetypes=[("BIG Files", "*.big"), ("All Files", "*.*")])
    if not file_path:
        return
    
    hash_value = compute_sha256(file_path)
    
    result_label.config(text=f"SHA-256: {hash_value}")

    # 生成 hash.txt
    with open("hash.txt", "w") as output_file:
        output_file.write(hash_value + "\n")

    status_label.config(text="哈希值已保存至 hash.txt")

# 创建 GUI 界面
root = tk.Tk()
root.title("BIG 文件哈希计算工具")
root.geometry("500x200")

# 按钮选择文件
btn_select = tk.Button(root, text="选择文件", command=select_file)
btn_select.pack(pady=20)

# 结果显示
result_label = tk.Label(root, text="SHA-256: ", wraplength=480, justify="left")
result_label.pack()

# 状态提示
status_label = tk.Label(root, text="", fg="green")
status_label.pack()

root.mainloop()
