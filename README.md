# RateMyProfessors Bot

A Playwright-based automation tool for programmatically submitting professor ratings on [RateMyProfessors.com](https://www.ratemyprofessors.com). Built for educational purposes, QA automation practice, and exploring form interaction with dynamic React components.

---

## Features

- **Full form automation** — Handles every required field: course code, quality/difficulty sliders, radio buttons, grade selection, tags, and review text
- **Randomized review comments** — Pulls from a curated `reviews.json` file of 100+ human-sounding reviews; a new one is selected randomly on each run
- **Modular class design** — All interactions are encapsulated in the `RmpBot` class, making the bot easy to extend, test, and maintain
- **Dynamic React component handling** — Uses bounding box clicking, scroll-into-view, and React-Select dropdown techniques

---

## Project Structure

```
RMP_Bot/
├── main.py          # Orchestrates the full end-to-end submission using RmpBot
├── bot.py           # Standalone single-file version of the automation
├── RmpBot.py        # Class with all form interaction methods
├── reviews.json     # Pool of 100+ human-sounding review comments
└── README.md        # Project documentation
```

---

## Prerequisites

- Python 3.8+
- Microsoft Edge installed
- [Playwright for Python](https://playwright.dev/python/)

Install dependencies:

```bash
pip install playwright
playwright install
```

---

## Usage

Run the bot from the project root directory:

```bash
python main.py
```

A browser window will open, automatically fill out the rating form, submit it, and close.

> **Note:** `bot.py` is a self-contained single-function version. `main.py` uses the `RmpBot` class from `RmpBot.py` for a cleaner, more extensible structure.

---

## How It Works

1. **Launch browser** — Opens Microsoft Edge in a maximized, non-headless window
2. **Navigate** — Goes to the target professor's rating page
3. **Fill form** — Each `RmpBot` method handles one section of the form, called in sequence
4. **Submit** — Scrolls to and clicks the submit button
5. **Close** — Waits briefly, then closes the browser

---

## RmpBot Class Methods

| Method | Description |
|---|---|
| `select_course_code(page)` | Selects course from the React-Select dropdown |
| `select_quality(page)` | Clicks the quality slider (5 stars) |
| `select_difficulty(page)` | Clicks the difficulty slider (1 star) |
| `select_would_take_again(page)` | Selects "Yes" for Would Take Again |
| `select_taken_for_credit(page)` | Selects "Yes" for Taken for Credit |
| `select_uses_textbooks(page)` | Selects "No" for Uses Textbooks |
| `select_attendance_mandatory(page)` | Selects "No" for Attendance Mandatory |
| `select_grade_received(page)` | Selects grade "A" from the dropdown |
| `select_tags(page)` | Randomly selects 3 tags from available options |
| `select_write_review(page)` | Picks a random review from `reviews.json` and fills the textarea |
| `click_submit(page)` | Scrolls to and clicks the submit button |
| `exit_review(page, browser)` | Waits, then closes the browser |

---

## Customization

The bot is designed to be easily modified. Common things to adjust:

- **Professor** — Change the professor ID in the URL inside `main.py`
- **Course code** — Update the `get_by_text(...)` call in `select_course_code`
- **Grade** — Change the target grade in `select_grade_received`
- **Quality / Difficulty** — Adjust the `* 0.9` multiplier in slider methods (0.1 = leftmost, 0.9 = rightmost)
- **Number of tags** — Change `random.sample(range(count), 3)` to select a different count
- **Review pool** — Add more entries to `reviews.json` under the `"reviews"` key

### reviews.json format

```json
{
  "reviews": [
    "Fantastic professor who explains everything clearly.",
    "Really appreciated how organized the lectures were."
  ]
}
```

---

## Tech Stack

- [Playwright (Python)](https://playwright.dev/python/) — Browser automation
- Microsoft Edge (Chromium) — Rendering target
- Python standard library — `json`, `random`

---

## Disclaimer

This project is intended strictly for **educational purposes**, automation practice, and learning how to interact with dynamic React-based web forms using Playwright. Use responsibly and in accordance with the terms of service of any website you interact with.
