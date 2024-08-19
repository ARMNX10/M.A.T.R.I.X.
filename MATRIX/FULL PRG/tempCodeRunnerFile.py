def open_index_html_selenium():
    url = "file:///D:/MATRIX/FULL%20PRG/index.html"
    chrome_option = Options()
    user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2"
    chrome_option.add_argument (f"user-agent={user_agent}")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service,options=chrome_option)
    driver.maximize_window()
    driver.get(url=url)
    driver.fullscreen_window()
    sleep(10)