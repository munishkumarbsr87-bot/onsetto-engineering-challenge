import { expect, Page } from "@playwright/test";

export class LoginPage {

    constructor(private readonly page: Page) {}

    readonly email = this.page.locator("#email");

    readonly password = this.page.locator("#password");

    readonly signIn = this.page.getByRole("button", {
        name: "Sign in"
    });

    readonly otp = this.page.locator('input[data-input-otp="true"]');

    readonly verify = this.page.getByRole("button", {
        name: "Verify"
    });

   async navigate(baseUrl: string) {
    await this.page.goto(baseUrl);

    await this.page.getByRole("button", {
        name: "Log in",
        exact: true
    }).last().click();

    await expect(this.email).toBeVisible();
}

    async login(email: string, password: string) {

        await this.email.fill(email);

        await this.password.fill(password);

        await this.signIn.click();

    }

   async verifyMFA() {
    await this.page.locator("input[data-input-otp]").fill("1234");

    await this.page.getByRole("button", {
        name: "Verify",
        exact: true
    }).click();

    await this.page.waitForLoadState("networkidle");

    // Navigate to Account page
    await this.page.goto(
        "https://marketplace.dev-challenge.com/app/account"
    );

    await expect(
        this.page.locator("[data-testid='banking-section']")
    ).toBeVisible({
        timeout: 10000
    });
}

}