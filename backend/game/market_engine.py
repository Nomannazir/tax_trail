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
        
        # Score calculation: 1.0 is perfect, penalize deviation.
        # For MVP, we can just use the ratio logic or a simple distance metric.
        # Request suggested: result["score"] = round(min(fiscal_ratio, 1.0), 2)
        # However, if ratio is 0.5 (underfunded), score should be low. 
        # If ratio is 1.5 (excessive), score should also be reflected.
        # Let's stick to the user's suggestion for simplicity or refine it to be "Balance Score".
        # If fiscal_ratio is > 1, we might want to penalize 'excessive'. 
        # But per instruction: "result["score"] = round(min(fiscal_ratio, 1.0), 2)"
        # This implies standardizing 1.0 as max. 
        score = round(min(fiscal_ratio, 1.0), 2) if fiscal_ratio <= 1.0 else round(max(0, 2.0 - fiscal_ratio), 2)
        # Actually, let's just use the suggested simple version for now to match their expectation of "score".
        # But "balanced" is 1.0 +/- tolerance.
        if 0.7 <= fiscal_ratio <= 1.5:
             score = 0.95 # Base high score for balanced
             if 0.9 <= fiscal_ratio <= 1.1:
                 score = 1.0
        else:
             score = 0.5 # Low score otherwise

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
                "🚨 **Budget Deficit Alert!** 🚨\n\n"
                "Your tax revenue is too low to cover essential services like schools and road maintenance. "
                "This is called a **Budget Deficit**. Try increasing the tax rate slightly to ensure our community has what it needs!"
            )
        elif fiscal_ratio > 1.5:
            # Check if rate > 40% of small business income logic from spec
            # Spec says "Trigger: TaxRate > 40% of SmallBusinessIncome"
            # Here we just use the ratio as a proxy or check the rate directly.
            # Let's check the rate directly as well if it's very distinct.
            # But the primary trigger in the python snippet involved fiscal_ratio > 1.5
            
            result["status"] = "excessive_taxation"
            result["coach_message"] = (
                "📉 **Economic Warning!** 📉\n\n"
                "Whoa! Taxes are very high. This puts a strain on local businesses, giving them less money to grow and hire people. "
                "This can stall the economy. Try lowering the tax rate to encourage growth!"
            )
        else:
            result["status"] = "balanced_budget"
            result["coach_message"] = (
                "🎉 **Fiscal Architect Achievement!** 🎉\n\n"
                "Perfect balance! You've raised enough revenue to fund public services without overburdening the economy. "
                "You've earned $3.50 on your Life Hub Visa Rewards Card!"
            )

        return result
