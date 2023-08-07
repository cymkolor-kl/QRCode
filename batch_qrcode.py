import os
import qrcode
import csv
import tkinter as tk
from tkinter import filedialog
from tqdm import tqdm

# 建立 QR Code 物件
def generate_qr_code(text, filename, output_folder):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=5
    )

    # 將文字加到 QR Code 物件中
    qr.add_data(text)

    # 產生 QR Code 圖片
    qr.make(fit=True)

    # 將 QR Code 圖片儲存到檔案中
    filepath = os.path.join(output_folder, filename + ".png")
    qr.make_image().save(filepath)

# 批量生成 QR Code 函數
def batch_generate_qr_codes(csv_file, output_folder):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        total_qr_codes = sum(1 for _ in reader)  # 獲得總產碼數量
        file.seek(0)  # 重新將檔案指標移到檔案開頭
        for row in tqdm(reader, total=total_qr_codes, desc="Generating QR Codes"):
            if len(row) == 2:
                filename, text = row[0], row[1]
                generate_qr_code(text, filename, output_folder)
        return total_qr_codes

# 提示用戶選擇包含"檔案名稱, 數據資料"的 CSV 文件
root = tk.Tk()
root.withdraw()
csv_file = filedialog.askopenfilename(title="選擇包含檔案名稱和數據資料的CSV文件", filetypes=[("CSV Files", "*.csv")])

# 提示用户输入要儲存的資料夾名稱
output_folder = input("請輸入要儲存的資料夾名稱：")

# 建立儲存資料夾
os.makedirs(output_folder, exist_ok=True)

# 批量生成 QR Code，獲得總產碼數量
total_qr_codes = batch_generate_qr_codes(csv_file, output_folder)

# 顯示總產碼數量
print("總產碼數量：", total_qr_codes)

# 顯示訊息，按任意鍵關閉視窗
input("按任意鍵關閉視窗...")
