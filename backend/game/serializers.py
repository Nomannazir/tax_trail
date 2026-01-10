from rest_framework import serializers

class SimulationInputSerializer(serializers.Serializer):
    tax_rate = serializers.FloatField(min_value=0.0, max_value=1.0, help_text="Tax rate as a decimal (e.g., 0.15 for 15%)")
    spending_plan = serializers.JSONField(required=False, help_text="Optional breakdown of spending", default={})

class SimulationResultSerializer(serializers.Serializer):
    status = serializers.CharField()
    revenue = serializers.FloatField()
    fiscal_ratio = serializers.FloatField()
    coach_message = serializers.CharField()

class CRAMetadataSerializer(serializers.Serializer):
    event_type = serializers.CharField()
    partner_id = serializers.CharField()
    program = serializers.CharField()
    learner_metadata = serializers.DictField()
    skill_mastery = serializers.DictField()
    financial_impact = serializers.DictField()
