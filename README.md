# Web-Based-Insurance-Calculator
Created a web application that allows users to input relevant data (age, coverage type, duration, etc.) and calculates insurance premiums using actuarial logic.

### 1. UI Dashboard — Household & Plan Overview
- Panels for primary groups: Single Adult, Couple, Family of 4, Senior
- Within each panel, display income ranges vs. estimated premium & subsidy details (e.g., from ACA or essential plans)
- Hardcode example data—for example: ACA benchmark rates and subsidy limits for different MAGI cut-offs
- Use a neat grid layout with CSS Flex or Grid.

### 2. Input Form — Guided Data Entry
Below the dashboard, display a form like:
- Household Size & Ages
- Income (MAGI)
- Insurance Types: Medical, Term Life, Vehicle, Business
- Health Status: smoker, pre-existing conditions
- Coverage Needs: coverage amount, term length, deductible preferences
Enhance UX with dynamic logic (e.g., if "Medical" chosen show health fields).

### 3. Backend & External Data Retrieval
When user submits, your app should:
1. Calculate eligibility & subsidy
- Use ACA Marketplace calculators to estimate health premiums/subsidies
2. Pull real quotes from:
- HealthSherpa API or Healthcare.gov preview engine 
- Major carriers (e.g., BCBS, UHC) for plan details
3. Life insurance quotes from top-rated carriers using aggregated source data:
- Banner Life, SBLI, State Farm, Guardian, etc.
- Get average monthly quotes based on age, term, coverage.
4. Vehicle or Business coverage can be placeholder or leverage external APIs (e.g., Insurtech).

### 4. Generate Personalized Recommendations
Based on user data and pulled quotes:
- Compare quotes & subsidies:
    - For health: order by premium after subsidy
    - For term life: show lowest quotes by age/coverage

### 5. Tech Stack & Implementation
- Frontend: HTML/CSS dashboard & form, JS to POST to backend
- Backend: Python + Flask
   - Form submission endpoint → calculation logic + API calls → JSON response
- External API usage:
   - ACA subsidy & plan pricing calculators
   - HealthSherpa or Healthcare.gov preview
   - Life insurance aggregator API (if available) or hard-coded data

