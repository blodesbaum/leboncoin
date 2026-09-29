from playwright.sync_api import sync_playwright

# Define cookies with possible corrections
cookies = [
    {
        "url": "https://leboncoin.fr/",
        "domain": ".leboncoin.fr",
        "name": "luat",
        "value": "YOUR_LONG_JWT_TOKEN_HERE",
        "hostOnly": False,
        "path": "/",
        "secure": True,
        "httpOnly": False,
        "sameSite": "unspecified",
        "session": False,
        "expirationDate": 1784281921
    },
    {
        "url": "https://auth.leboncoin.fr/",
        "domain": ".auth.leboncoin.fr",
        "name": "__Secure-Login",
        "value": "ANOTHER_JWT_TOKEN_HERE",
        "hostOnly": False,
        "path": "/",
        "secure": True,
        "httpOnly": True,
        "sameSite": "no_restriction",
        "session": False,
        "expirationDate": 1803030720.377209
    }
]

url = "https://www.leboncoin.fr/vehicule/afficher-mon-iban?agreementId=3787198a-6701-4faa-a246-95b07f6dc89a&from=messagerie&listId=3127895670&source=messaging&pathType=direct_purchase"

with sync_playwright() as p:
    try:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()

        # Add cookies to context
        context.add_cookies(cookies)

        page = context.new_page()

        # Navigate to the specified URL
        page.goto(url, wait_until="networkidle")

        # Write page content to file
        with open("iban_page.html", "w", encoding="utf-8") as f:
            f.write(page.content())

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        browser.close()

