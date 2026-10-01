import asyncio
from playwright.async_api import async_playwright
async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        ignored = (".png", ".jpg", ".svg", ".css", ".js", ".woff2", ".mp3")
        def handle_request(req):
            url = req.url
            if not url.endswith(ignored) and ("/api/" in url or "/v1/" in url or "youtubei" in url):
                print("FOUND API ->", url)
        page.on("request", handle_request)
        url = input("enter url twin: ").strip()
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        await page.goto(url)
        await page.wait_for_timeout(5000)
        await browser.close()
asyncio.run(run())
