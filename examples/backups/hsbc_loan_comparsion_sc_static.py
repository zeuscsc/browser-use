import asyncio
import datetime
import os
from urllib.parse import urlparse, unquote

from crawlee.crawlers import PlaywrightCrawler, PlaywrightCrawlingContext


def save_html_snapshot(content, url, output_dir="snapshots/html"):
    """
    Saves an HTML snapshot with a directory structure reflecting the URL's path.

    Args:
        content: HTML content to save.
        url: The URL of the content.
        output_dir: Base output directory.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    now = datetime.datetime.now()
    date_dir = now.strftime("%Y%m%d")
    date_output_dir = os.path.join(output_dir, date_dir)
    if not os.path.exists(date_output_dir):
        os.makedirs(date_output_dir)
    try:
        parsed_url = urlparse(url)
        site_dir = parsed_url.netloc
        if not site_dir:
            site_dir = "unknown_site"
        url_path = parsed_url.path
        if not url_path:
            url_path = "/"
        url_path = unquote(url_path)
        path_parts = url_path.strip("/").split("/")
    except Exception as e:
        print(f"Error parsing URL: {url}. Using 'unknown_site' and root path. Error: {e}")
        site_dir = "unknown_site"
        path_parts = ["unknown_path"]
    domain_output_dir = os.path.join(date_output_dir, site_dir)
    if not os.path.exists(domain_output_dir):
        os.makedirs(domain_output_dir)
    current_dir = domain_output_dir
    for part in path_parts:
        if part:
            current_dir = os.path.join(current_dir, part)
            if not os.path.exists(current_dir):
                os.makedirs(current_dir)
    timestamp = now.strftime("%H%M%S")
    filename = f"snapshot_{timestamp}.html"
    filepath = os.path.join(current_dir, filename)
    if not os.path.exists(filepath):
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"HTML snapshot saved to: {filepath}")
    else:
        print(f"HTML snapshot already exists: {filepath}")
    return filepath


async def main() -> None:
    crawler = PlaywrightCrawler()

    @crawler.router.default_handler
    async def request_handler(context: PlaywrightCrawlingContext) -> None:
        context.log.info(f'Processing {context.request.url}')

        await context.page.wait_for_selector('table')

        content = await context.page.content()

        save_html_snapshot(content, context.request.url)

    STANDARD_CHARTERED = "https://www.sc.com/hk/loans/personal-instalment-loan/"

    await crawler.run([STANDARD_CHARTERED])

def today_craw_already():
    output_dir = "snapshots/html"
    now = datetime.datetime.now()
    date_dir = now.strftime("%Y%m%d")
    date_output_dir = os.path.join(output_dir, date_dir)
    if os.path.exists(date_output_dir):
        return True
    return False

if __name__ == '__main__':
    date_dir = datetime.datetime.now().strftime("%Y%m%d")
    if not today_craw_already():
        asyncio.run(main())
        print(f"Crawler ran and created snapshots for {date_dir}.")
    else:
        print(f"Snapshots already exist for {date_dir}.  Crawler will not run.")