from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def check_element_presence(driver, element_locator, max_attempts=5, delay=2):
    for attempt in range(max_attempts):
        print(f"Attempt {attempt + 1}/{max_attempts}")
        try:
            # Wait for the element to be present
            WebDriverWait(driver, delay).until(EC.presence_of_element_located(element_locator))
            print(f"Element found: {element_locator}")
            return True  # Element found
        except Exception:
            print(f"Element not found: {element_locator}")


    print("Element not found after multiple attempts.")
    return False  # Element not found after all attempts