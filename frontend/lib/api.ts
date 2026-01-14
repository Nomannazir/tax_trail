import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000/api';

export interface SimulationResult {
    revenue: number;
    fiscal_ratio: number;
    score: number;
    status: 'under_funded' | 'excessive_taxation' | 'balanced_budget';
    coach_message: string;
    badge_eligible?: boolean;
}

export const simulateGame = async (taxRate: number, spendingPlan: Record<string, number> = {}) => {
    const response = await axios.post<SimulationResult>(`${API_BASE_URL}/simulate/`, {
        tax_rate: taxRate,
        spending_plan: spendingPlan,
    });
    return response.data;
};

export const getCRAMetadata = async () => {
    const response = await axios.get(`${API_BASE_URL}/cra-metadata/`);
    return response.data;
}
