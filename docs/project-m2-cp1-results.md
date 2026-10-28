# AI Content Studio — Quality Test Results (Sweet Crumbs)

## 1. Three Chat Quality Tests

### Test 1: A question our facts answer (Delivery & Hours)
- **Question:** `Do you deliver to DHA and what are your timings?`
- **AI Answer:** `Yes! Delivery across Lahore (including DHA) is 200 PKR, and free for orders from 3,000 PKR. We are open from 9 am to 10 pm.`
- **Judgement:** **Correct** — used the exact delivery charges and opening hours from `facts` without inventing details.

### Test 2: A question about a price
- **Question:** `How much is the chocolate cake and the mango tart?`
- **AI Answer:** `Our Chocolate Cake is 1,500 PKR, and the Mango Tart is coming soon.`
- **Judgement:** **Correct** — stated the exact 1,500 PKR price and recognized the price-0 item as "coming soon".

### Test 3: A question our facts CANNOT answer (Product we do not sell)
- **Question:** `Do you sell pizza?`
- **AI Answer:** `Sorry, I only know about our Sweet Crumbs bakery items, and pizza is not one of them.`
- **Judgement:** **Correct (Did not hallucinate)** — stayed strictly inside the system prompt boundaries and refused to make up an item or price.

---

## 2. Best `/post` Output & Tone Evaluation

### Best Output (`/post premium`)
> **English:**
> Some moments deserve more than ordinary.
> Our chocolate cake, baked by hand every morning, 1,500 PKR.
> Sweet Crumbs, Lahore. Open 9 am to 10 pm.
>
> **Roman Urdu (Bonus):**
> Kuch lamhay khaas mithaas ke haqdaar hotay hain.
> Hamara taaza handmade Chocolate Cake, har subah तैयार kiya jata hai, sirf 1,500 PKR mein.
> Sweet Crumbs, Lahore. Subah 9 baje se raat 10 baje tak khula hai.

### Which tone worked best and why?
The **`premium`** tone worked best for **Sweet Crumbs** because customers buying a 1,500 PKR artisan chocolate cake respond better to calm, quality-focused descriptions of fresh morning baking than loud promotional hype.
