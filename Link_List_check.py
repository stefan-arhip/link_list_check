# pip install keyboard
import webbrowser
import keyboard
import time
firefox = webbrowser.Mozilla("C:\\FirefoxPortable\\App\\Firefox64\\firefox.exe")
with open('search.txt', 'r') as file:
    for line in file:
        #webbrowser.get('firefox').open_new_tab("https://www.bing.com/search?q="+line.strip())
        firefox.open('https://www.bing.com/search?q='+line.strip())
        time.sleep(5)
        keyboard.press_and_release('ctrl + w') 
