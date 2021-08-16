from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
import time
from selenium.webdriver.common.action_chains import ActionChains
=# user_agent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Mobile Safari/537.36"
opts = ChromeOptions()
opts.add_argument("--start-maximized")
opts.add_argument("--width=2560")
opts.add_argument("--height=1440")
# opts.add_argument(f"--user-agent={user_agent}")
def get_keywords(url):
    print('hi')

    driver = webdriver.Chrome(options=opts)

    print("hihi")
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1.5)
    seeMoreButton = driver.find_element_by_css_selector("span.right>img")
    # print(seeMoreButton.text)
    time.sleep(2)
    ActionChains(driver).move_to_element(seeMoreButton)
    outputFile = open("keyword.txt","w+")
    count = 0
    while count < 250:
        keywordSections = driver.find_elements_by_css_selector("div.content")
        print(len(keywordSections))
        for section in keywordSections:
            keyword = section.find_element_by_css_selector("span.title")
            print(keyword.text)
            outputFile.write(keyword.text+"\n")
        seeMoreButton.click()
        count += 1
        time.sleep(1.5)
    outputFile.close()    

if __name__ == "__main__":
    url = "https://tiki.vn/"
    get_keywords(url)