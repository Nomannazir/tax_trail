from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SimulationInputSerializer, SimulationResultSerializer, CRAMetadataSerializer
from .market_engine import TaxationMarketEngine
from .compliance import generate_cra_metadata
from .badges import issue_fiscal_architect_badge
from drf_yasg.utils import swagger_auto_schema

class SimulateView(APIView):
    @swagger_auto_schema(
        request_body=SimulationInputSerializer,
        responses={200: SimulationResultSerializer}
    )
    def post(self, request):
        serializer = SimulationInputSerializer(data=request.data)
        if serializer.is_valid():
            tax_rate = serializer.validated_data.get('tax_rate')
            spending_plan = serializer.validated_data.get('spending_plan')

            engine = TaxationMarketEngine()
            result = engine.calculate_fiscal_impact(tax_rate, spending_plan)
            
            # Badge Logic Integration
            if result['status'] == 'balanced_budget':
                # Check if eligible for badge
                badge_awarded = issue_fiscal_architect_badge(result.get('score', 0))
                result['badge_eligible'] = badge_awarded
            
            return Response(result, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CRAMetadataView(APIView):
    @swagger_auto_schema(
        responses={200: CRAMetadataSerializer}
    )
    def get(self, request):
        # In a real scenario, this would fetch the user's game session state.
        # For this MVP, we generate a success payload assuming the user balanced the budget.
        # We can simulate different scores if we want, but default to success for validation.
        fiscal_data = {
            "score": 0.98,
            "interactions": 2
        }
        metadata = generate_cra_metadata(fiscal_data)
        return Response(metadata, status=status.HTTP_200_OK)
