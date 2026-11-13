import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        errs=[]
        for name, vp in [("m", {"width":390,"height":844}), ("d", {"width":1280,"height":900})]:
            pg = await b.new_page(viewport=vp)
            pg.on("pageerror", lambda e: errs.append(str(e)))
            pg.on("console", lambda m: errs.append(m.text) if m.type=="error" else None)
            await pg.goto("http://127.0.0.1:8765/"); await pg.click("#k-ex"); await pg.click("#t-ex")
            await pg.screenshot(path=f"shot-home-{name}.png", full_page=False)
            await pg.goto("http://127.0.0.1:8765/przelew-mpp-numer-ksef/"); await pg.click("#m-ex")
            await pg.screenshot(path=f"shot-mpp-{name}.png", full_page=True)
            await pg.goto("http://127.0.0.1:8765/przelew-z-faktury-xml-ksef/"); await pg.click("#x-ex"); await pg.wait_for_timeout(400)
            await pg.screenshot(path=f"shot-xml-{name}.png", full_page=False)
            await pg.goto("http://127.0.0.1:8765/kod-qr-ksef/"); await pg.click("#g-ex"); await pg.wait_for_timeout(600); await pg.click("#d-ex-bad")
            await pg.screenshot(path=f"shot-qr-{name}.png", full_page=True)
            await pg.goto("http://127.0.0.1:8765/nie-ma/")
            await pg.screenshot(path=f"shot-404-{name}.png")
        print("errors:", errs)
        await b.close()
asyncio.run(main())
