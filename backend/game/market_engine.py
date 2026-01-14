class TaxationMarketEngine:
    def __init__(self):
        self.community_needs = 1000  # Cost of essential services
        self.taxable_base = 8000     # Total community income

    def calculate_fiscal_impact(self, user_tax_rate, user_spending_plan=None):
        
        # Calculates the impact of the tax rate on the community.
        # :param user_tax_rate: Float (e.g., 0.15 for 15%)
        # :param user_spending_plan: Dictionary (optional) for future expansion
        # :return: dict with status, revenue, fiscal_ratio, and coach_message
        
        # Logic: Revenue = Rate * Base
        revenue = user_tax_rate * self.taxable_base
        fiscal_ratio = revenue / self.community_needs
        
        # Score calculation: 1.0 is perfect balance.
        # Formula: score = max(0, 1 - distance_from_1)
        score = max(0.0, 1.0 - abs(1.0 - fiscal_ratio))
        score = round(score, 2)

        result = {
            "revenue": revenue,
            "fiscal_ratio": fiscal_ratio,
            "score": score,
            "status": "balanced_budget",
            "coach_message": ""
        }

        # Trigger Infiniti AI Coach for unbalanced budgets
        if fiscal_ratio < 0.7:
            result["status"] = "under_funded"
            result["coach_message"] = (
                "<b>Budget Deficit Alert!</b>\n\n"
                "Your tax revenue is too low to cover essential services like schools and road maintenance. "
                "This is called a <b>Budget Deficit</b>. Try increasing the tax rate slightly to ensure our community has what it needs!"
            )
        elif fiscal_ratio > 1.5:
            # Check if rate > 40% of small business income logic from spec
            # Spec says "Trigger: TaxRate > 40% of SmallBusinessIncome"
            # Here we just use the ratio as a proxy or check the rate directly.
            # Let's check the rate directly as well if it's very distinct.
            # But the primary trigger in the python snippet involved fiscal_ratio > 1.5
            
            result["status"] = "excessive_taxation"
            result["coach_message"] = (
                "<b>Economic Warning!</b>\n\n"
                "Whoa! Taxes are very high. This puts a strain on local businesses, giving them less money to grow and hire people. "
                "This can stall the economy. Try lowering the tax rate to encourage growth!"
            )
        else:
            result["status"] = "balanced_budget"
            result["coach_message"] = (
                "<b>Fiscal Architect Achievement!</b>\n\n"
                "Perfect balance! You've raised enough revenue to fund public services without overburdening the economy. "
                "You've earned $3.50 on your Life Hub Visa Rewards Card!"
            )

        return result
