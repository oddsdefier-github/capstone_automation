import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

links_local = {
    "2": "https://ieeexplore.ieee.org/abstract/document/9815483/authors#authors",
    "3": "https://www.researchgate.net/publication/321091817_Information_systems_for_smart_services",
    "4": "https://journalppw.com/index.php/jpsp/article/view/7263",
    "5": "https://ejournals.ph/article.php?id=12127",
    "6": "https://ejournals.ph/article.php?id=6120",
    "7": "https://ejournals.ph/article.php?id=6121",
    "8": "https://www.pids.gov.ph/publication/discussion-papers/the-philippine-local-government-water-sector",
    "9": "https://www.pids.gov.ph/publication/philippine-journal-of-development/an-assessment-of-the-financial-sustainability-and-performance-of-philippine-water-districts",
    "10": "https://www.researchgate.net/publication/326260033_Web-based_Billing_and_Collection_System_for_a_Municipal_Water_and_Services_Unit",
    "11": "https://journal.evsu.edu.ph/index.php/itmj/article/view/41",
    "12": "https://www.ijres.org/papers/Volume-10/Issue-6/100610871091.pdf",
    "13": "https://ejournals.ph/article.php?id=7261",
    "14": "https://ieeexplore.ieee.org/abstract/document/9977678",
    "15": "https://ieeexplore.ieee.org/abstract/document/6804531",
    "16": "https://research.lpubatangas.edu.ph/wp-content/uploads/2015/05/APJARBA-2015-1-006-Computerized-vs.-Non-computerized-Accounting-System.pdf",
    "17": "https://www.sajst.org/online/index.php/sajst/article/view/130",
    "18": "https://dl.acm.org/doi/abs/10.1145/3421682.3421691",
    "19": "https://payo.asia/ecommerce-automation-philippines/",
    "20": "https://www.sciencedirect.com/science/article/pii/S1877050919318149",
    "21": "https://ieeexplore.ieee.org/abstract/document/8269446"
}

driver.get(list(links_local.values())[0])
time.sleep(3)
driver.execute_script("window.stop();")

for index, link in list(links_local.items())[1:]:
    driver.execute_script(f"window.open('{link}', '_blank');")
    print(f'[{index}] {link}')
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(3)
    driver.execute_script("window.stop();")

input("Press any key to exit...")
driver.quit()
