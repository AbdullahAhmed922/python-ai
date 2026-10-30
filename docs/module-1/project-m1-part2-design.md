# Module 1, Checkpoint 2 — Design & Rule Tests (Sweet Crumbs Bakery)

## 1. Intents Table

| Intent | Keywords | Reply |
| :--- | :--- | :--- |
| **Complaint (First)** | `refund`, `complaint`, `late` | Sorry about that. A manager will call you within 1 hour. |
| **Human Handover (Bonus)** | `human`, `agent` | Connecting you to a human... *(ends chat)* |
| **Greeting** | `== "hi"`, `== "hello"`, `== "salam"`, `== "hey"` or `.startswith()` | Hello {name}! Welcome to Sweet Crumbs bakery. Ask about our hours, menu, location, or type /quote. |
| **Hours** | `hour`, `open`, `close`, `timing` | We are open 9 am to 10 pm, every day. |
| **Location** | `location`, `where`, `branch`, `shop` | We are located on Main Boulevard, Gulberg, Lahore. |
| **Delivery & Fees** | `deliver`, `shipping`, `fee`, `charges` | Standard delivery is 200 PKR, and FREE on orders of 3,000 PKR or more (after discount)! |
| **Menu & Prices** | `menu`, `price`, `items`, `cost` | Our menu: Cupcake (250 PKR), Brownie (300 PKR), Chocolate Cake (1,500 PKR). Type /quote for an exact price! |

## 2. Business Rules Table

| Rule | Value |
| :--- | :--- |
| **Item prices** | `cupcake`: 250 PKR, `brownie`: 300 PKR, `chocolate cake`: 1,500 PKR |
| **Bulk discount** | 10% off when buying 10 or more of an item |
| **Delivery** | 200 PKR standard fee; free when discounted subtotal is 3,000 PKR or more |
| **Rule order in `/quote`** | Subtotal -> subtract 10% bulk discount -> check if discounted subtotal >= 3,000 PKR for free delivery |
| **Private words** | `phone`, `cnic`, `address` (routed to `llama3.2 (local, private)` at 0 PKR cost) |
| **Cloud pricing** | 0.10 PKR per 1,000 tokens (`small cloud model (cheap)`) |

## 3. Rule Tests

| You type | Expected | Actual Output | Pass? |
| :--- | :--- | :--- | :--- |
| `  WHAT are your hours ` | Hours (capitals and spaces handled) | `We are open 9 am to 10 pm, every day.` | Pass |
| `which cake is best?` | Fallback, **not** a greeting ("hi" hides in "which") | Routed to `small cloud model (cheap)` (~5 tokens) | Pass |
| `my order is late` | Manager reply (complaint rule first) | `Sorry about that. A manager will call you within 1 hour.` | Pass |
| `/quote`, `1` of your most expensive item (`chocolate cake`) | Delivery fee charged (1,500 + 200 = 1,700 PKR) | `Discount: -0 PKR \| Delivery: 200 PKR \| Total: 1,700 PKR` | Pass |
| `/quote`, a big order above the free-delivery limit (`chocolate cake`, `3`) | Delivery free (4,500 PKR >= 3,000 PKR) | `Discount: -0 PKR \| Delivery: 0 PKR \| Total: 4,500 PKR` | Pass |
| `/quote`, 10 or more items (`cupcake`, `12`) | 10% discount applied (-300 PKR), delivery 200 PKR charged since 2,700 < 3,000 | `12 x cupcake = 3,000 PKR \| Discount: -300 PKR \| Delivery: 200 PKR \| Total: 2,900 PKR` | Pass |
| `/quote`, an item not on your menu (`pizza`, `2`) | "Not on our menu", no crash | `Sorry, pizza is not on our menu.` | Pass |
| A question with `"phone"` or `"cnic"` (`can I change my phone number on the order?`) | Routed to the local model, cost 0 | `Routed to: llama3.2 (local, private) (~10 tokens)` | Pass |
| Press Enter with no text | Asks again | `Please type a message, /quote, or bye.` | Pass |
| `BYE` | Goodbye + session report | `Goodbye, Ali Raza!` + Session report | Pass |
