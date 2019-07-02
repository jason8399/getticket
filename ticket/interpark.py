from selenium.webdriver.support.ui import WebDriverWait

from .ticketbase import TicketBase


class Interpark(TicketBase):
    def __init__(self, config):
        super(Interpark, self).__init__(config)
        pass

    def exectue(self):
        # Get ticket Page
        prdNo = self.config["Default"]["prdNo"]
        self.driver.get("http://www.globalinterpark.com/detail/"
                        "edetail?prdNo={0}&dispNo=01003".format(prdNo))

        # Login
        self.driver.execute_script("fn_signin()")
        self.driver.find_element_by_id("memEmail")\
                   .send_keys(self.config["Default"]["Email"])
        self.driver.find_element_by_id("memPass")\
                   .send_keys(self.config["Default"]["Password"])
        self.driver.find_element_by_id("sign_in").click()

        # Switch to "product_detail_area" until iframe finishing loading
        self.driver.switch_to.frame(WebDriverWait(self.driver, 30).until(
            lambda x: x.find_element_by_id("product_detail_area")))

        # Open Booking window
        self.driver.execute_script("javascript:fnNormalBooking()")

        # Switch to Open window
        self.driver.switch_to.window(self.driver.window_handles[1])

        # Switch to "ifrmBookStep" until iframe finishing loading
        self.driver.switch_to.frame(WebDriverWait(self.driver, 30).until(
            lambda x: x.find_element_by_id("ifrmBookStep")))

        # Select concert date
        date = self.config["Default"]["Concert_Date"]
        avaiable_day = self.driver.find_elements_by_name("CellPlayDate")
        script = ""
        for elem in avaiable_day:
            if date in elem.get_attribute("onclick"):
                script = elem.get_attribute("onclick")
        self.driver.execute_script(script)

        # Switch back to default frame
        self.driver.switch_to.default_content()

        # To next step
        WebDriverWait(self.driver, 2).until(
                lambda x: x.find_element_by_id("LargeNextBtn").is_displayed())
        self.driver.execute_script("javascript:fnNextStep('P');")
