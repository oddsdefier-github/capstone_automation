from selenium import webdriver
import time 

driver = webdriver.Chrome()
driver.maximize_window()

links_international = {
    "1": "https://www.linkedin.com/pulse/can-human-errors-avoided-business-processes-patrick-mutabazi/",
    "2": "https://ieeexplore.ieee.org/document/7530621",
    "3": "https://www.comidor.com/blog/business-process-management/a-comparison-of-manual-and-automated-workflow-processes/",
    "4": "https://www.researchgate.net/publication/369235619_Automatic_Energy_Meter_Billing_System_with_Theft_Detection",
    "5": "https://fepbl.com/index.php/ijarss/article/view/440",
    "6": "http://hdl.handle.net/11394/9216",
    "7": "https://ieeexplore.ieee.org/document/8960144",
    "8": "https://www.researchgate.net/publication/345776202_Implementation_of_Improved_Billing_System",
    "9": "https://ieeexplore.ieee.org/document/9835742",
    "10": "https://ieeexplore.ieee.org/abstract/document/8597179",
    "11": "https://ieeexplore.ieee.org/abstract/document/9675569",
    "12": "https://ieeexplore.ieee.org/abstract/document/9889267",
    "13": "https://ieeexplore.ieee.org/document/9442031",
    "14": "https://www.proquest.com/openview/0d88a38ba77f360ea4e504e1ebc76e2f/1.pdf?pq-origsite=gscholar&cbl=1976354",
    "15": "https://ieeexplore.ieee.org/document/8339088",
    "16": "https://www.sciencedirect.com/science/article/pii/S1877042811024621",
    "17": "https://thesai.org/Downloads/Volume12No8/Paper_48-An_Efficient_IoT_Based_Smart_Water_Meter_System.pdf",
    "18": "https://arxiv.org/abs/2106.15005",
    "19": "https://www.jetir.org/view?paper=JETIR2106786",
    "20": "https://www.calendar.com/blog/data-visualization-is-the-key-to-team-productivity/"
}


driver.get(links_international["1"])
time.sleep(3)
driver.execute_script("return window.stop();")

for index, link in list(links_international.items())[1:]:
    driver.execute_script(f"window.open('{link}', '_blank');")
    print(f"[{index}] {link}")
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(3)
    driver.execute_script("return window.stop();")

input("Press any key to exit...")
driver.quit()