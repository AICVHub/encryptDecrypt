import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from cryptography.fernet import Fernet

class FileEncryptorDecryptor:
    def __init__(self):
        self.key = None
        self.fernet = None

    def generate_key(self):
        self.key = Fernet.generate_key()
        return self.key

    def save_key(self, key, key_filename='key.key'):
        try:
            with open(key_filename, 'wb') as key_file:
                key_file.write(key)
        except Exception as e:
            messagebox.showerror("错误", f"保存密钥时发生错误: {e}")

    def load_key(self, key_filename):
        try:
            with open(key_filename, 'rb') as key_file:
                key = key_file.read()
            self.fernet = Fernet(key)
        except FileNotFoundError:
            messagebox.showerror("错误", "密钥文件未找到，请确保密钥文件存在。")
        except Exception as e:
            messagebox.showerror("错误", f"加载密钥时发生错误: {e}")

    def encrypt_file(self, input_filename, output_filename):
        if not self.fernet:
            self.fernet = Fernet(self.generate_key())
            self.save_key(self.key)

        try:
            with open(input_filename, 'rb') as input_file:
                content = input_file.read()
            encrypted_content = self.fernet.encrypt(content)
            with open(output_filename, 'wb') as output_file:
                output_file.write(encrypted_content)
            messagebox.showinfo("成功", "文件已加密。")
        except Exception as e:
            messagebox.showerror("错误", f"加密过程中发生错误: {e}")

    def decrypt_file(self, input_filename, output_filename):
        if not self.fernet:
            messagebox.showerror("错误", "请先加载密钥。")

        try:
            with open(input_filename, 'rb') as input_file:
                encrypted_content = input_file.read()
            decrypted_content = self.fernet.decrypt(encrypted_content)
            with open(output_filename, 'wb') as output_file:
                output_file.write(decrypted_content)
            messagebox.showinfo("成功", "文件已解密。")
        except Fernet.InvalidToken:
            messagebox.showerror("错误", "解密失败，密钥可能不正确。")
        except Exception as e:
            messagebox.showerror("错误", f"解密过程中发生错误: {e}")

class EncryptDecryptApp:
    def __init__(self, root):
        self.root = root
        self.root.title("文件加密/解密工具")
        self.ed = FileEncryptorDecryptor()

        self.frame = ttk.Frame(self.root, padding="3 3 12 12")
        self.frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.encrypt_button = ttk.Button(self.frame, text="加密文件", command=self.encrypt_file)
        self.encrypt_button.grid(column=0, row=0, padx=10, pady=10)

        self.decrypt_button = ttk.Button(self.frame, text="解密文件", command=self.decrypt_file)
        self.decrypt_button.grid(column=1, row=0, padx=10, pady=10)

        self.key_load_button = ttk.Button(self.frame, text="加载密钥", command=self.load_key)
        self.key_load_button.grid(column=2, row=0, padx=10, pady=10)

    def encrypt_file(self):
        input_filename = filedialog.askopenfilename(
            title="选择要加密的文件",
            filetypes=[("所有文件", "*.*")]
        )
        if not input_filename:
            return

        output_filename = filedialog.asksaveasfilename(
            title="保存加密文件",
            defaultextension=".enc",
            filetypes=[("加密文件", "*.enc")]
        )
        if not output_filename:
            return

        self.ed.encrypt_file(input_filename, output_filename)

    def decrypt_file(self):
        input_filename = filedialog.askopenfilename(
            title="选择要解密的文件",
            filetypes=[("加密文件", "*.enc")]
        )
        if not input_filename:
            return

        output_filename = filedialog.asksaveasfilename(
            title="保存解密文件",
            defaultextension=".txt",
            filetypes=[("解密文件", "*")]
        )
        if not output_filename:
            return

        self.ed.decrypt_file(input_filename, output_filename)

    def load_key(self):
        key_filename = filedialog.askopenfilename(
            title="选择密钥文件",
            filetypes=[("密钥文件", "*.key")]
        )
        if not key_filename:
            return

        self.ed.load_key(key_filename)

if __name__ == '__main__':
    root = tk.Tk()
    app = EncryptDecryptApp(root)
    root.mainloop()