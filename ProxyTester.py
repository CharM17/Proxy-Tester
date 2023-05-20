import asyncio
from arsenic import get_session, browsers, services
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)
with open('proxies.txt', 'r') as f:
    proxies = f.readlines()

# Set the maximum number of concurrent tasks
max_concurrent = 10

async def test_proxy(proxy, sem):
    # Remove any whitespace from the proxy string
    proxy = proxy.strip()

    # Configure the browser with proxy settings
    browser = browsers.Chrome()
    browser.capabilities['goog:chromeOptions'] = {
        'args': [
            '--headless',
            '--disable-dev-shm-usage',  # Avoid issues with ChromeDriver in certain environments
            f'--proxy-server={proxy}'
        ]
    }

    service = services.Chromedriver()

    async with get_session(service, browser) as session:
        try:
            # Open google and detect page loading
            await session.get('https://www.google.com')
            css = '#APjFqb'
            await session.wait_for_element(5, css)
            goodproxies = open('goodproxies.txt', 'a')
            goodproxies.write(f"{proxy} \n")
        except:
            print(f'{proxy} - FAIL')
        finally:
            sem.release()

async def main():
    sem = asyncio.Semaphore(max_concurrent)
    # Create a list of tasks for each proxy test
    tasks = []
    for proxy in proxies:
        await sem.acquire()
        task = asyncio.create_task(test_proxy(proxy, sem))
        tasks.append(task)
    await asyncio.gather(*tasks)

asyncio.run(main())
