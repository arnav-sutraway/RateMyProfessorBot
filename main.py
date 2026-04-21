from playwright.sync_api import sync_playwright
from RmpBot import *
import bot

def test_submit_rating():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            channel="msedge",
            headless=False,
            args=["--start-maximized"]
        )

        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        link = "https://www.ratemyprofessors.com/add/professor-rating/3088979"

        page.goto(link)

        bot = RmpBot()


        # --------------------
        # SELECT COURSE CODE
        # --------------------
        bot.select_course_code(page)
        

        # --------------------
        # QUALITY (5 stars)
        # --------------------
        bot.select_quality(page)

        # --------------------
        # DIFFICULTY (1 star)
        # --------------------
        bot.select_difficulty(page)

        # --------------------
        # WOULD YOU TAKE AGAIN? (YES)
        # --------------------

        bot.select_would_take_again(page)

        # --------------------
        # TAKEN FOR CREDIT? (YES)
        # --------------------
        bot.select_taken_for_credit(page)

        # --------------------
        # USES TEXTBOOKS? (NO)
        # --------------------
        bot.select_uses_textbooks(page)

        # --------------------
        # ATTENDANCE MANDATORY? (NO)
        # --------------------
        bot.select_attendance_mandatory(page)

        # --------------------
        # SELECT GRADE RECEIVED
        # --------------------
        bot.select_grade_received(page)


        # --------------------
        # SELECT 3 TAGS
        # --------------------
        bot.select_tags(page)


        # --------------------
        # WRITE A REVIEW
        # --------------------
        bot.select_write_review(page)

        
        # --------------------
        # CLICK SUBMIT
        # --------------------
        bot.click_submit(page)

        # --------------------
        # EXIT REVIEW
        # --------------------
        bot.exit_review(page, browser)


if __name__ == '__main__':

    count = RmpBot.get_count_amount(self=None)
    countt = 1
    while count > 0:
        test_submit_rating()
        print(f"Completed submission #{countt}")
        count -= 1
        countt += 1
