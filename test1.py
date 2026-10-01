import asyncio
from playwright.async_api import async_playwright
async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        page.on("request", lambda req: print("->", req.url))        
        url = input("enter url twin: ").strip()
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        await page.goto(url)
        await page.wait_for_timeout(5000)
        await browser.close()
asyncio.run(run())
