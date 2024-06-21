from time import sleep

import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import config


class JobsSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["linkedin.com"]

    def start_requests(self):
        url = "https://www.linkedin.com/login/pt?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
        yield SeleniumRequest(
            url=url,
            callback=self.parse
        )

    def parse(self, response):
        driver = response.request.meta["driver"]
        driver.find_element(By.ID, "username").send_keys(config.EMAIL)
        driver.find_element(By.ID, "password").send_keys(config.PASSWORD)
        driver.find_element(By.CSS_SELECTOR, ".btn__primary--large.from__button--floating").click()
        sleep(60)
        driver.get(config.URL)

        while True:
            # Pega todas as vagas da página
            jobs = driver.find_elements(By.CSS_SELECTOR,
                                        ".scaffold-layout__list-container > .scaffold-layout__list-item")

            # Percorre cada vaga da página
            for job in jobs:
                job.click()
                sleep(3)
                job_description = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, '#job-details > div'))
                )

                yield {
                    "job_description": job_description.text.replace("\n", " ")
                }

            # Tenta seguir para próxima página, se não houve, para o script
            try:
                next_page = driver.find_element(By.CSS_SELECTOR, ".artdeco-pagination__pages > .selected + li")
                ActionChains(driver).scroll_to_element(next_page).perform()
                next_page.click()
                sleep(1)
            except NoSuchElementException:
                break
