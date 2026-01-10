import datetime

def generate_cra_metadata(fiscal_data):
    
    # Generates the CRA compliance JSON payload.
    # :param fiscal_data: Dict containing score, interactions, etc.
    # :return: Dict (JSON-ready)
    
    return {
        "event_type": "CRA_QUALIFYING_LEARNING_ACTIVITY",
        "partner_id": "OLD_NATIONAL_BANK_001",
        "program": "LIFE_HUB_INFINITI_GTM_2026",
        "timestamp": datetime.datetime.now().isoformat(),
        "learner_metadata": {
            "age_range": "6-18",
            "lmi_status": "VERIFIED_LOW_MODERATE_INCOME_CENSUS_TRACT",
            "location": "CHICAGO_METRO_AREA"
        },
        "skill_mastery": {
            "topic": "Civic Responsibility & Taxation",
            "industry_context": "Public Finance / Community Reinvestment",
            "assessment_score": fiscal_data.get("score", 0.0),
            "ai_coach_interactions": fiscal_data.get("interactions", 0)
        },
        "financial_impact": {
            "edu_job_payout": 3.50,
            "disbursement_method": "LIFE_HUB_VISA_REWARDS_CARD",
            "compliance_code": "CRA_REGULATION_BB_SEC_11"
        }
    }
