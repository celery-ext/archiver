# TODOアプリ
#--------------------------
import os
import datetime
import shutil
import tkinter as tk
from tkinter import ttk

# Todoアプリのクラス
class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("archiver")
        self.geometry("500x600")
        self.dt_now = datetime.datetime.now()

        # ファイル名を決めるフレーム
        filename_frame = tk.Frame(self)
        filename_frame.pack(pady=30)
        tk.Label(filename_frame, text="filename:").grid(row=0, column=0)

        #ファイル名の設定
        self.filename_entry = tk.Entry(
            filename_frame,
            width=25
            )
        self.filename_entry.grid(row=0, column=1)
        self.filename_entry.insert(0, "Lesson")

        #拡張子の設定
        self.extension_entry = ttk.Combobox(
            filename_frame,
            values = self.Extension(),
            state="readonly", width=5
            )
        self.extension_entry.grid(row=0,column=2)
        self.extension_entry.current(0)
        
        # 追加ボタンを配置するフレーム
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="archive file", command=self.MakeDirectory).pack(side="left")

        # 追加したfileの一覧を表示(未実装)
        self.file_list = tk.Listbox(self, selectmode="multiple", bd=10)
        self.file_list.pack(fill="both", expand=True)

        # タスクの一覧
        self.files = []

    #拡張子の追加
    def Extension(self):
        option = [
            ".py", ".java", ".json",
            ".html", ".css",".js", 
            ".c", ".cpp", ".cs",
            ".txt"]
        return option
    
    # ディレクトリの作成
    def MakeDirectory(self):
        self.today = self.GetDate()
        self.dir_path = f'archive/{self.today}'
        print(self.dir_path)
        if(os.path.exists(self.dir_path) == False):
            os.mkdir(self.dir_path)

        self.MakeFile()

    # ファイルの保存
    def MakeFile(self):
        self.filename = self.filename_entry.get()
        self.file_extension = self.extension_entry.get()
        self.file_dir_path = f'{self.dir_path}/{self.filename}{self.file_extension}'

        i = 1
        while(os.path.isfile(self.file_dir_path) == True):
            self.file_dir_path = f'{self.dir_path}/{self.filename}{i}{self.file_extension}'
            i += 1

        shutil.copy('main.py',self.file_dir_path)

        file = self.task_entry.get()
        if file:
            self.files.append(self.file_dir_path)
            self.file_list.insert("end",file)
            self.file_entry.delete(0, "end")
        
    # 日付の取得
    def GetDate(self):
        # 西暦の取得
        self.year = str(self.dt_now.year)

        # 月の取得
        if(self.dt_now.month>10):
            self.month = str(self.dt_now.month)
        else:
            self.month = "0" + str(self.dt_now.month)
        
        # 日付の取得
        if(self.dt_now.day>10):
            self.day = str(self.dt_now.day)
        else:
            self.day = "0" + str(self.dt_now.day)

        self.date = self.year + "-" + self.month + "-" + self.day

        return self.date

    # タスクの削除
    def delete_task(self):
        selected_indices = self.task_list.curselection()
        for index in selected_indices[::-1]:
            self.task_list.delete(index)
            self.tasks.pop(index)

# Todoアプリを起動する
if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()