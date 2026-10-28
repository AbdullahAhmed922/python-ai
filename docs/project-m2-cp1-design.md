# AI Content Studio — Design & Test Plan (Sweet Crumbs)

## 1. Facts Table

| Key | Value |
| :--- | :--- |
| `name` | Sweet Crumbs |
| `city` | Lahore |
| `hours` | 9 am to 10 pm |
| `delivery` | 200 PKR across Lahore (including DHA), free for orders from 3,000 PKR |
| `custom_orders` | 24 hours advance notice for custom birthday and celebration cakes |
| `prices` | chocolate cake: 1,500 PKR, cupcake: 250 PKR, brownie: 300 PKR, mango tart: 0 PKR (coming soon) |

## 2. Tones Table

| Tone | Description sent to the AI |
| :--- | :--- |
| `fun` | playful and full of energy, short sentences |
| `premium` | elegant and calm, focused on quality |
| `urgent` | fresh-out-of-the-oven limited batch alert, encouraging orders before sellout |

## 3. Which Model for Which Job

| Job | Model and temperature | Why |
| :--- | :--- | :--- |
| Menu descriptions (`/menu`) | `creative_llm`, `0.8` | Marketing text should be varied and appetizing so every pastry sounds fresh. |
| Social media posts (`/post`) | `creative_llm`, `0.8` | Instagram captions need distinct personality and stylistic flair across tones. |
| Roman Urdu post translation (Bonus) | `precise_llm`, `0.2` | Translation must keep the exact PKR prices and bakery hours from the English post without inventing details. |
| Price lookup (`/price`) | No AI (Python dictionary `.get()`) | Exact price lookups are deterministic; reading the dictionary is instant, 100% accurate, and costs 0 tokens. |
| Customer chat | `precise_llm`, `0.2` | Customer support must stay strictly grounded in bakery facts and never make up prices or menu items. |

## 4. Feature Tests

| You type | Expected | Pass? |
| :--- | :--- | :--- |
| `/menu` | Price-0 item skipped, numbered menu, prices with commas, cloud cost estimate printed | Yes |
| `/post` with each of your tones | Post streams word by word, in a different style each time, followed by Roman Urdu version | Yes |
| `/post pirate` (a tone that does not exist) | Default tone used, no `KeyError` | Yes |
| `/price` with a real item in CAPITALS | Correct price (`CUPCAKE` -> `250 PKR`) | Yes |
| `/price` with your price-0 item | `"Coming soon"` (`mango tart`) | Yes |
| `/price` with an item not on your menu | `"Not on our menu"`, no crash | Yes |
| `My name is Ali`, then `What is my name?` | Remembers the name (`Ali`) | Yes |
| `/reset`, then `What is my name?` | Does not know the name anymore | Yes |
| Press Enter with no text | Asks again without calling AI | Yes |
| `BYE` | Goodbye + session report with all 6 numbers | Yes |
