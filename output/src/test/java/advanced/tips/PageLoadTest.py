import { chromium } from 'playwright';

describe('Page Load Test', () => {
  let browser;
  let page;

  before(async () => {
    browser = await chromium.launch();
  });

  after(async () => {
    await browser.close();
  });

  it('Check page load', async () => {
    page = await browser.newPage();
    await page.goto('https://www.saucedemo.com/');
  });
});