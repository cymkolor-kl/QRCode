import qrcode

# 建立 QR Code 物件
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.ERROR_CORRECT_L,
    box_size=10,
    border=5
)

# 提示用戶輸入文字
text = input("請輸入要產生 QR Code 的文字：")

# 提示用戶輸入檔案名稱
filename = input("請輸入要儲存的檔案名稱：")

# 將文字加到 QR Code 物件中
qr.add_data(text)

# 產生 QR Code 圖片
qr.make(fit=True)

# 將 QR Code 圖片儲存到檔案中
qr.make_image().save(filename + ".png")

# 顯示 QR Code 圖片
img = qr.make_image()
img.show()