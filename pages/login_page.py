from utils.config import BASE_URL, TIMEOUT


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"

    def navigate(self):
        self.page.goto(BASE_URL, timeout=TIMEOUT)
        self.page.wait_for_load_state("networkidle")

    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)
