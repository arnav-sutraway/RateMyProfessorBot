from playwright.sync_api import sync_playwright

def test_submit_rating():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            channel="msedge",
            headless=False,
            args=["--start-maximized"]
        )

        context = browser.new_context(no_viewport=True)
        page = context.new_page()

        page.goto("https://www.ratemyprofessors.com/add/professor-rating/3088979")

        # --------------------
        # SELECT COURSE CODE
        # --------------------
        dropdown = page.locator(".css-1nfef2z-control").first
        dropdown.scroll_into_view_if_needed()
        page.wait_for_timeout(300)
        dropdown.click()

        # Wait for menu to appear
        page.wait_for_timeout(300)

        # Click the option
        page.get_by_text("2211K", exact=True).click()

        

        # --------------------
        # QUALITY (5 stars)
        # --------------------
        slider = page.locator("div[data-testid='SliderBox']").nth(4)
        page.wait_for_selector("div[data-testid='SliderBox']")
        page.wait_for_timeout(500)

        box = slider.bounding_box()
        # DEBUGGING print("QUALITY slider box:", box)

        page.mouse.click(
            box["x"] + box["width"] * 0.9,
            box["y"] + box["height"] / 2
        )

        # DEBUGGING print(slider.get_attribute("aria-selected"))
        page.wait_for_timeout(1000)

        # --------------------
        # DIFFICULTY (1 star)
        # --------------------
        difficulty = page.locator("div[data-testid='SliderBox']").nth(5)
        difficulty.scroll_into_view_if_needed()
        #page.wait_for_timeout(500)

        dbox = difficulty.bounding_box()
        # DEBUGGING print("DIFFICULTY slider box:", dbox)

        # Click LEFT side: 1 star
        page.mouse.click(
            dbox["x"] + dbox["width"] * 0.9,
            dbox["y"] + dbox["height"] / 2
        )

        # DEBUGGING print("DIFFICULTY aria-selected:", difficulty.get_attribute("aria-selected"))
        page.wait_for_timeout(800)

        # --------------------
        # WOULD YOU TAKE AGAIN? (YES)
        # --------------------

        take_again = page.locator("input#wouldTakeAgain-Yes")
        take_again.scroll_into_view_if_needed()
        take_again.click()
        page.wait_for_timeout(800)

        # --------------------
        # TAKEN FOR CREDIT? (YES)
        # --------------------
        taken_for_credit = page.locator("input#forCredit-Yes")
        taken_for_credit.scroll_into_view_if_needed()
        taken_for_credit.click()
        page.wait_for_timeout(800)

        # --------------------
        # USES TEXTBOOKS? (NO)
        # --------------------
        uses_textbooks = page.locator("input#usesTextbooks-No")
        uses_textbooks.scroll_into_view_if_needed()
        uses_textbooks.click()
        page.wait_for_timeout(800)

        # --------------------
        # ATTENDANCE MANDATORY? (NO)
        # --------------------
        attendance_mandatory = page.locator("input#attendanceMandatory-No")
        attendance_mandatory.scroll_into_view_if_needed()
        attendance_mandatory.click()
        page.wait_for_timeout(800)

        # --------------------
        # SELECT GRADE RECEIVED
        # --------------------
        
        dropdown = page.locator(".css-1j0hwvb-control").first
        dropdown.scroll_into_view_if_needed()
        page.wait_for_timeout(300)
        dropdown.click()

        # Wait for menu to appear
        page.wait_for_timeout(300)

        # Click the option
        page.get_by_text("A", exact=True).click()


        # --------------------
        # SELECT 3 TAGS
        # --------------------
        import random

        tags = page.locator(".FormTag__StyledCheckBoxContainer-sc-1hp6xsc-0")
        count = tags.count()

        # Pick 3 unique random indexes
        random_indexes = random.sample(range(count), 3)

        for i in random_indexes:
            tag = tags.nth(i)
            tag.scroll_into_view_if_needed()
            tag.click()
            page.wait_for_timeout(500)


        # --------------------
        # WRITE A REVIEW
        # --------------------
        import json, random

        with open("reviews.json", "r") as f:
            data = json.load(f)

        review_text = random.choice(data["reviews"])

        page.fill("textarea[name='comment']", review_text)
        page.wait_for_timeout(500)


        # --------------------
        # CLICK SUBMIT
        # --------------------
        submit_btn = page.locator(".add-teacher-rating-btn")
        submit_btn.wait_for(state="visible")

        submit_btn.scroll_into_view_if_needed()
        page.wait_for_timeout(300)

        submit_btn.click()


        # --------------------
        # EXIT REVIEW
        # --------------------
        page.wait_for_timeout(3000)
        browser.close()

if __name__ == '__main__':
    test_submit_rating()
