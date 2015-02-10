from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.selenium import selenium

driver = webdriver.Firefox()
driver.get("http://www.python.org")

assert "Python" in driver.title
print driver.title
print '1 passed'
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
name = 'new.png'
driver.get_screenshot_as_file(name)
#x = elem.
#if x :
print 'not found'
#else :
#print 'not found'
driver.close()