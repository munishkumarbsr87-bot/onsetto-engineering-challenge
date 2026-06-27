import { test, expect } from '@playwright/test';

test('Open Website', async ({ page }) => {
  await page.goto('https://challenge.onsetto.dev');

  await expect(page).toHaveTitle(/Challenge/i);
});