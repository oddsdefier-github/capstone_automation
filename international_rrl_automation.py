from selenium import webdriver
import time 

driver = webdriver.Chrome()
driver.maximize_window()

links_international = [
    "https://www.linkedin.com/pulse/can-human-errors-avoided-business-processes-patrick-mutabazi/",
    "https://ieeexplore.ieee.org/document/7530621",
    "https://www.comidor.com/blog/business-process-management/a-comparison-of-manual-and-automated-workflow-processes/",
    "https://www.researchgate.net/publication/369235619_Automatic_Energy_Meter_Billing_System_with_Theft_Detection",
    "https://fepbl.com/index.php/ijarss/article/view/440",
    "http://hdl.handle.net/11394/9216",
    "https://ieeexplore.ieee.org/document/8960144",
    "https://www.researchgate.net/publication/345776202_Implementation_of_Improved_Billing_System",
    "https://ieeexplore.ieee.org/document/9835742",
    "https://ieeexplore.ieee.org/abstract/document/8597179",
    "https://ieeexplore.ieee.org/abstract/document/9675569",
    "https://ieeexplore.ieee.org/abstract/document/9889267",
    "https://ieeexplore.ieee.org/document/9442031",
    "https://www.proquest.com/openview/0d88a38ba77f360ea4e504e1ebc76e2f/1.pdf?pq-origsite=gscholar&cbl=1976354",
    "https://ieeexplore.ieee.org/document/8339088",
    "https://www.sciencedirect.com/science/article/pii/S1877042811024621",
    "https://thesai.org/Downloads/Volume12No8/Paper_48-An_Efficient_IoT_Based_Smart_Water_Meter_System.pdf",
    "https://arxiv.org/abs/2106.15005",
    "https://www.jetir.org/view?paper=JETIR2106786",
    "https://www.calendar.com/blog/data-visualization-is-the-key-to-team-productivity/"
]

driver.get(links_international[0])

for index, link in enumerate(links_international[1:], 1):
    driver.execute_script(f"window.open('{link}', '_blank');")
    print(f'[{index}] {link}')
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(3)  # Wait for 3 seconds
    driver.execute_script("window.stop();")

input("Press any key to exit...")
driver.quit()