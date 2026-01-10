from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

class SimulationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('simulate')

    def test_under_funded(self):
        data = {'tax_rate': 0.05} # 5% tax -> 400 revenue -> 0.4 ratio (<0.7)
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'under_funded')
        self.assertIn("Budget Deficit", response.data['coach_message'])

    def test_balanced_budget(self):
        data = {'tax_rate': 0.13} # 13% -> 1040 revenue -> 1.04 ratio (Balanced)
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'balanced_budget')
        self.assertIn("Fiscal Architect", response.data['coach_message'])

    def test_excessive_taxation(self):
        data = {'tax_rate': 0.30} # 30% -> 2400 revenue -> 2.4 ratio (>1.5)
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'excessive_taxation')
        self.assertIn("Economic Warning", response.data['coach_message'])

class ComplianceTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('cra-metadata')

    def test_cra_metadata_structure(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['event_type'], "CRA_QUALIFYING_LEARNING_ACTIVITY")
        self.assertEqual(response.data['financial_impact']['edu_job_payout'], 3.5)
