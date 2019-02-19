import shelve, re, os
from selenium import webdriver
import pyperclip
from selenium.webdriver.common.keys import Keys
import time

WP_USER = "your_user_name"
WP_PASS = "your_passwd"
WP_DOMAIN = "http://example.com"

def wordpress(text_body, excerpt_text):
	path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'geckodriver.exe'))
	browser = webdriver.Firefox(executable_path=path)
	browser.get(WP_DOMAIN + "/wp-admin/post-new.php")
	wpuser = browser.find_element_by_id("user_login")
	wpuser.send_keys(WP_USER)


	wppass = browser.find_element_by_id("user_pass")
	wppass.send_keys(WP_PASS)

	wpsb = browser.find_element_by_id("wp-submit")
	wpsb.click()
	time.sleep(2)

	body = browser.find_element_by_tag_name("body")
	body.send_keys(Keys.CONTROL, Keys.ALT, Keys.SHIFT, "m")

	pc = browser.find_element_by_class_name("editor-post-text-editor")
	pc.click()
	pyperclip.copy(text_body)
	pc.send_keys(Keys.CONTROL, "v")

	time.sleep(1)
	
	excerpt = browser.find_elements_by_class_name("components-panel__body")[1]
	excerpt.click()	
	excerpt = browser.find_elements_by_class_name("components-panel__body")[3]
	excerpt.click()	
	excerpt = browser.find_elements_by_class_name("components-panel__body")[4]
	excerpt.click()

	excerpt = browser.find_element_by_class_name("components-textarea-control__input")
	excerpt.click()

	pyperclip.copy(excerpt_text)
	excerpt.send_keys(Keys.CONTROL, "v")
