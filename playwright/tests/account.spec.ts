import { test } from "@playwright/test";

import { LoginPage } from "../pages/LoginPage";
import { AccountPage } from "../pages/AccountPage";

import { env } from "../utils/env";
import { bankDetails, cardDetails } from "../data/testData";

test("Update banking details and payment method", async ({ page }) => {
  const login = new LoginPage(page);
  const account = new AccountPage(page);

  await login.navigate(env.baseUrl);

  await login.login(env.username, env.password);

  await login.verifyMFA(env.mfaCode);

  await account.updateBanking(
    bankDetails.routingNumber,
    bankDetails.accountNumber
  );

  await account.updatePayment(
    cardDetails.holderName,
    cardDetails.cardNumber,
    "12",
    "2032",
    cardDetails.cvc
  );
});