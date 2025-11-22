# User Stories – Sprint 1  
**Financial Transactions Summary Tool**

---

## US-1 – Load Dataset  
**As a** data analyst,  
**I want** to load the transactions dataset,  
**so that** I can begin analysis.

### Acceptance Criteria
- File loads from `/data/financial_transactions.csv`.
- Function returns a pandas DataFrame.
- Meaningful error if path is incorrect.

### Story Points: 2

### Tasks
- T1.1 Implement `load_transactions()`
- T1.2 Test CSV loading
- T1.3 Update README instructions

---

## US-2 – Clean Dataset  
**As a** team member,  
**I want** the dataset cleaned and standardized,  
**so that** all summaries are accurate.

### Acceptance Criteria
- Convert `date` → datetime.
- Convert `amount` → numeric.
- Drop rows with missing values.
- Normalize `type` column.

### Story Points: 3

### Tasks
- T2.1 Implement `clean_transactions()`
- T2.2 Validate dropped rows
- T2.3 Document cleaning logic

---

## US-3 – Summary by Type  
**As a** user,  
**I want** to see total amounts by type,  
**so that** I understand inflow/outflow quickly.

### Acceptance Criteria
- Returns totals for credit and debit.
- Based on cleaned DataFrame.

### Story Points: 3

### Tasks
- T3.1 Implement `total_by_type()`
- T3.2 Test with subset
- T3.3 Add example in demo script

---

## US-4 – Summary by Customer  
**As a** business stakeholder,  
**I want** to see total amounts per customer,  
**so that** I can identify top customers.

### Acceptance Criteria
- Returns customer totals.
- Sorted from highest to lowest.

### Story Points: 5

### Tasks
- T4.1 Implement `total_by_customer()`
- T4.2 Validate top 5 customers
- T4.3 Screenshot results for report

---

## US-5 – Monthly Summary  
**As a** user,  
**I want** a monthly breakdown,  
**so that** I can track trends.

### Acceptance Criteria
- Groups into YYYY-MM format.
- Sorted chronologically.

### Story Points: 5

### Tasks
- T5.1 Implement `monthly_summary()`
- T5.2 Check month ordering
- T5.3 Prepare sample output

---

## US-6 – Overall Summary  
**As a** non-technical user,  
**I want** a simple overall summary,  
**so that** I understand the financial situation quickly.

### Acceptance Criteria
- Returns total_credit, total_debit, net_flow.
- Uses existing functions (no duplicate code).

### Story Points: 3

### Tasks
- T6.1 Implement `overall_summary()`
- T6.2 Test against manual calculation
- T6.3 Integrate into demo script
