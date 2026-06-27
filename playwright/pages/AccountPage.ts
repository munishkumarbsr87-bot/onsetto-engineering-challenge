import { expect, Page } from "@playwright/test";

export class AccountPage {
  constructor(private readonly page: Page) {}

  // Banking
  readonly routingNumber = this.page.locator("#bank-routing");
  readonly accountNumber = this.page.locator("#bank-account");
  readonly saveBankButton = this.page.locator("#bank-save");

  // Payment
  readonly cardHolder = this.page.locator("#card-holder");
  readonly cardNumber = this.page.locator("#card-number");
  readonly expMonth = this.page.locator("#card-exp-month");
  readonly expYear = this.page.locator("#card-exp-year");
  readonly cvc = this.page.locator("#card-cvc");
  readonly saveCardButton = this.page.locator("#card-save");

  // Summary
  readonly bankSummary = this.page.locator("[data-testid='bank-saved-info']");
  readonly paymentSummary = this.page.locator("[data-testid='payment-saved-info']");

  async updateBanking(routing: string, account: string) {
    await this.routingNumber.fill(routing);
    await this.accountNumber.fill(account);

    await this.saveBankButton.click();

    await expect(this.bankSummary).toBeVisible();


    await expect(this.bankSummary).toContainText(routing.slice(-4));
    await expect(this.bankSummary).toContainText(account.slice(-4));
  }

  async updatePayment(
    holder: string,
    number: string,
    month: string,
    year: string,
    cvc: string
  ) {
    await this.cardHolder.fill(holder);
    await this.cardNumber.fill(number);
    await this.expMonth.fill(month);
    await this.expYear.fill(year);
    await this.cvc.fill(cvc);

    await this.saveCardButton.click();

    await expect(this.paymentSummary).toContainText(number.slice(-4));
    await expect(this.paymentSummary).toContainText(`${month}/${year}`);
  }
}