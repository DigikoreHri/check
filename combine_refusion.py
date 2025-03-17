import time
import random
import subprocess
import multiprocessing
import time
import os
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
import csv

def run_mitmproxy():
    """Run mitmdump as a subprocess to capture API responses."""
    try:
        print("Starting mitmproxy...")
        subprocess.run(["mitmdump", "-s", "capture_response_refusion.py"], check=True)
    except Exception as e:
        print(f"❌ mitmproxy failed: {e}")

def login_and_generate_riffusion(email: str, password: str):
    # Set up Chrome options
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--ignore-ssl-errors")
    chrome_options.add_argument("--proxy-server=http://127.0.0.1:8080")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        # 1. Go to Riffusion
        driver.get("https://www.riffusion.com/")
        time.sleep(2)

        # 2. Click on the "Login" button
        login_button = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div[1]/div[2]/div[2]/button")
        login_button.click()
        time.sleep(2)

        # 3. Click on the "Sign in with Google" button
        google_login_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/button[1]")
        google_login_button.click()
        time.sleep(2)

        # 4. Enter Gmail ID
        email_input = driver.find_element(By.XPATH, "//input[@type='email']")
        email_input.send_keys(email)
        time.sleep(1)

         # 5. Click "Next"
        next_button_email = driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
        next_button_email.click()
        time.sleep(20)

        # 5. Click "Next"
        # next_button_email.click()
        # time.sleep(15)

        # 6. Enter password
        password_input = driver.find_element(By.XPATH, "//input[@type='password']")
        password_input.send_keys(password)
        time.sleep(10)

        # 7. Click "Next"
        next_button_password = driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
        next_button_password.click()
        time.sleep(30)

        print("Login successful!")
        time.sleep(30)
 
        # Open text area for input
        button_to_open_prompt = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/header/div/div[1]/div/div")
        button_to_open_prompt.click()
        time.sleep(10)

        # Get lyrics once
        lyrics_for_songs = input(f"Enter lyrics for songs: ")

        # Get all 10 sounds before loop
        sounds_list = []
        print("Enter 10 different sounds for each song:")
        for i in range(1, 2):
            sound = input(f"Enter sound for song {i}: ")
            sounds_list.append(sound)

        # Loop to generate 10 songs
        for i in range(10):
            print(f"Generating song {i+1}/10...")

            # Click on "Compose"
            compose_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[1]/button[2]")
            compose_button.click()
            time.sleep(2)

            # Fill in Lyrics
            lyrics_textarea = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/textarea")
            lyrics_textarea.clear()
            lyrics_textarea.send_keys(lyrics_for_songs)
            time.sleep(1)

            # Fill in Sounds (from pre-stored list)
            sounds_textarea = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[3]/div/div[1]/div[3]/div[2]/textarea")
            sounds_textarea.clear()
            sounds_textarea.send_keys(sounds_list[i])
            time.sleep(1)

            # Click on "Generate"
            generate_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[3]/div/div[2]/div/button")
            generate_button.click()
            time.sleep(40)  # Wait for processing

            print(f"Song {i+1} generated successfully!\n")

            button_to_open_prompt = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/header/div/div[1]/div/div")
            button_to_open_prompt.click()
            time.sleep(3)

        print("All 10 songs have been generated! Check Riffusion.")
    
    except Exception as e:
        print("An error occurred:", e)
    
    finally:
        time.sleep(5)
        driver.quit()



if __name__ == "__main__":
    my_email = "finnegansoren4@gmail.com"
    my_password= "TeamDigikore$6789"
    # Create multiprocessing tasks
    process1 = multiprocessing.Process(target=run_mitmproxy)
    process2 = multiprocessing.Process(target=login_and_generate_riffusion(my_email,my_password))
    
    # Start both processes
    process1.start()
    process2.start()
    
    # Wait for both to complete
    process1.join()
    process2.join()
    
    print("✅ Both processes completed.")
