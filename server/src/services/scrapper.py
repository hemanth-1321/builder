# scraper.py


from playwright.async_api import async_playwright
import os

async def scrape_landing_page(url, output_dir="output"):
    os.makedirs(output_dir, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1440, "height": 900})

        print(f"🔍 Navigating to {url}")
        await page.goto(url, timeout=60000)
        await page.wait_for_load_state("networkidle")  # Ensure full render

        html = await page.content()

        # Save HTML
        html_path = os.path.join(output_dir, "page.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✅ Saved HTML to {html_path}")

        # Screenshot full page
        screenshot_path = os.path.join(output_dir, "screenshot.png")
        await page.screenshot(path=screenshot_path, full_page=True)
        print(f"📸 Screenshot saved to {screenshot_path}")

        await browser.close()

