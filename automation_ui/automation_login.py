import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): # test scenario

    def setUp(self): # ini untuk buka browser dan install sesuai versi browser laptop
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        self.browser = webdriver.Chrome(service=service, options=options)
        
    def test_verify_success_login(self): # test case, awali dengan def test
        # form login
        self.browser.get("https://barru.pythonanywhere.com") # buka situs
        time.sleep(3)
        self.browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("batch18@gmail.com") # isi form email
        time.sleep(1)
        self.browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("batch18") # isi form password
        time.sleep(1)
        self.browser.find_element(By.ID, "signin_login").click() # klik tombol login
        time.sleep(1)

        # pop up
        popup_atas = self.browser.find_element(By.ID, "swal2-title").text # dapetin teks/tulisan pop up atas
        popup_bawah = self.browser.find_element(By.ID,"swal2-content").text # dapetin teks/tulisan pop up bawah
        time.sleep(2)
        
        # validasi
        self.assertIn('Welcome', popup_atas)
        self.assertEqual(popup_bawah, 'Anda Berhasil Login')
        
    def test_verify_failed_login_with_email_registered_and_empty_pass(self): # test case, awali dengan def test
        # form login
        self.browser.get("https://barru.pythonanywhere.com") # buka situs
        time.sleep(3)
        self.browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("batch18@gmail.com") # isi form email
        time.sleep(1)
        self.browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("") # tidak password, diberi string kosong ""
        time.sleep(1)
        self.browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # pop up
        popup_atas = self.browser.find_element(By.ID,"swal2-title").text # dapetin teks/tulisan pop up atas
        popup_bawah = self.browser.find_element(By.ID,"swal2-content").text # dapetin teks/tulisan pop up bawah
        time.sleep(2)
        
        # validasi
        self.assertEqual(popup_atas, 'Cek Formulir Anda')
        self.assertEqual(popup_bawah, 'Password tidak boleh kosong')

    def tearDown(self): # ini untuk tutup browser
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()