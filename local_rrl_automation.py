from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

links_local = [
    "https://ieeexplore.ieee.org/abstract/document/9815483/authors#authors",
    "https://www.researchgate.net/publication/321091817_Information_systems_for_smart_services",
    "https://journalppw.com/index.php/jpsp/article/view/7263",
    "https://ejournals.ph/article.php?id=12127",
    "https://ejournals.ph/article.php?id=6120",
    "https://ejournals.ph/article.php?id=6121",
    "https://www.pids.gov.ph/publication/discussion-papers/the-philippine-local-government-water-sector",
    "https://www.pids.gov.ph/publication/philippine-journal-of-development/an-assessment-of-the-financial-sustainability-and-performance-of-philippine-water-districts",
    "https://www.researchgate.net/publication/326260033_Web-based_Billing_and_Collection_System_for_a_Municipal_Water_and_Services_Unit",
    "https://journal.evsu.edu.ph/index.php/itmj/article/view/41",
    "https://www.ijres.org/papers/Volume-10/Issue-6/100610871091.pdf",
    "https://ejournals.ph/article.php?id=7261",
    "https://ieeexplore.ieee.org/abstract/document/9977678",
    "https://ieeexplore.ieee.org/abstract/document/6804531",
    "https://research.lpubatangas.edu.ph/wp-content/uploads/2015/05/APJARBA-2015-1-006-Computerized-vs.-Non-computerized-Accounting-System.pdf",
    "https://www.sajst.org/online/index.php/sajst/article/view/130",
    "https://dl.acm.org/doi/abs/10.1145/3421682.3421691",
    "https://payo.asia/ecommerce-automation-philippines/",
    "https://www.sciencedirect.com/science/article/pii/S1877050919318149",
    "https://ieeexplore.ieee.org/abstract/document/8269446"
    
]

driver.get(links_local[0])

for index, link in enumerate(links_local[1:], 1):
    driver.execute_script(f"window.open('{link}', '_blank');")
    print(f'[{index}] {link}')
    driver.switch_to.window(driver.window_handles[-1])

input("Press any key to exit...")
driver.quit()