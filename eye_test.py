from selenium import webdriver

driver = webdriver.Firefox()
driver.get(
    '<a class="vglnk" href="http://www.igame.com/eye-test/" rel="nofollow"><span>http</span><span>://</span><span>www</span><span>.</span><span>igame</span><span>.</span><span>com</span><span>/</span><span>eye</span><span>-</span><span>test</span><span>/</span></a>')
# Игра находится во фрейме, поэтому переключаемся на фрейм
driver.switch_to_frame(driver.find_element_by_tag_name('iframe'))

# Разворачиваем окно, нам ведь еще скрины делать
driver.maximize_window()

# Начинаем выигрывать. Результат 50 нас вполне устроит
for i in range(50):
    elem = driver.find_element_by_class_name('thechosenone')
    elem.click()

# Делаем скриншот результата
driver.save_screenshot('eyetest.png')

driver.close()