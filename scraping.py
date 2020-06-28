import asyncio
from pyppeteer import launch

async def cookie_div_exist():
    browser = await launch({'headless': False})
    page = await browser.newPage()
    await page.goto('https://avaus.com/', { "waitUntil": "networkidle0" })
    elements = await page.querySelector('div')
    # sad approach 1 that definitely didn't work :( ---- section = await page.querySelector("//div[contains(., 'Cookies')]")
    #section = await page.evaluate('(element) => element.innerHTML.indexOf("This website uses cookies" !== -1', element)

    #section = await page.evaluate('(elements) => elements[i].innerHTML.indexOf("This website uses cookies" !== -1', elements)
    paragraphs = await page.evaluate('//p[contains(text(), "cookies")]')

    #print(elements)

    print(paragraphs)

    #if len(section) > 0:
    #    print('FOUND IT!')
    #else:
    #    print('no cookie :(')

    #await browser.close()


asyncio.get_event_loop().run_until_complete(cookie_div_exist())