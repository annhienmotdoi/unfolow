
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Đường dẫn đến ChromeDriver
chrome_driver_path = "/data/data/com.termux/files/usr/bin/chromedriver"

# Tạo một phiên trình duyệt Chrome
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

# Mở trang đăng nhập của TikTok
driver.get("https://www.tiktok.com/login")

# Đợi để người dùng đăng nhập thủ công (hoặc tự động nếu bạn biết cách)
time.sleep(60)  # Bạn có thể cần tăng thời gian này

# Đi đến trang danh sách những người đang theo dõi
driver.get("https://www.tiktok.com/@your_username/following")

# Chờ để trang tải hoàn toàn
time.sleep(10)

# Lấy danh sách các nút Unfollow
unfollow_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Following')]")

# Unfollow từng người một
for button in unfollow_buttons:
    button.click()
    time.sleep(1)  # Tạm dừng một chút để tránh bị TikTok chặn

# Đóng trình duyệt
driver.quit()
