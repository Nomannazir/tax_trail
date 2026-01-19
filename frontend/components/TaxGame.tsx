"use client";

import React, { useState, useEffect, useCallback } from "react";
import { simulateGame, type SimulationResult } from "@/lib/api";
import { Slider } from "./ui/Slider";
import { AICoach } from "./AICoach";
import { VisaCard } from "./VisaCard";
import { Badge } from "./Badge";
import Image from "next/image";

export const TaxGame: React.FC = () => {
    // State
    const [taxRate, setTaxRate] = useState<number>(0.15); // Start at 15%
    const [result, setResult] = useState<SimulationResult | null>(null);
    const [loading, setLoading] = useState(false);
    const [earnings, setEarnings] = useState(0.00);

    // Debounced simulation
    const runSimulation = useCallback(async (rate: number) => {
        setLoading(true);
        try {
            const data = await simulateGame(rate);
            setResult(data);
            if (data.status === 'balanced_budget') {
                setEarnings(3.50);
            } else {
                setEarnings(0.00);
            }
        } catch (error) {
            console.error("Simulation failed", error);
        } finally {
            setLoading(false);
        }
    }, []);

    // Effect to run simulation on rate change (debounced)
    useEffect(() => {
        const timer = setTimeout(() => {
            runSimulation(taxRate);
        }, 600);
        return () => clearTimeout(timer);
    }, [taxRate, runSimulation]);

    return (
        <div className="w-full min-h-screen bg-background flex flex-col items-center">
            {/* Header - Strictly attached to top, 36px bottom radius for 'tab' effect */}
            <header className="w-full bg-[image:var(--image-header-surface)] p-6 rounded-b-[36px] border-b border-white/60 shadow-sm relative z-20 flex justify-between items-center max-w-5xl">
                <div>
                    <h1 className="text-xl md:text-2xl font-bold">
                        <span className="text-navy">The</span> <span className="text-primary">Tax Trail</span>
                    </h1>
                    <p className="text-sm text-muted">Balance the budget to earn!</p>
                </div>
                <div className="flex items-center gap-2 bg-white px-4 py-2 rounded-xl shadow-inner border border-gray-100">
                    <span className="text-xs font-semibold text-muted uppercase tracking-wider">Earnings</span>
                    <span className="text-lg font-bold text-primary font-mono">${earnings.toFixed(2)}</span>
                </div>
            </header>

            <main className="w-full max-w-5xl p-4 md:p-10 space-y-10">
                <div className="grid grid-cols-1 md:grid-cols-12 gap-8 md:gap-10">
                    {/* LEFT COLUMN: Controls & City */}
                    <div className="md:col-span-7 space-y-10">
                        {/* Game Board / City Map Placeholder */}
                        <div className="relative aspect-video bg-white rounded-3xl border border-indigo-100 overflow-hidden flex flex-col items-center justify-center group shadow-glow-high">
                            <div className={`w-16 h-16 mb-4 rounded-full flex items-center justify-center text-2xl transition-colors duration-500 ${result?.status === 'balanced_budget' ? 'bg-secondary/20 text-secondary' : 'bg-muted/10 text-muted/50'}`}>
                                <Image src="/icons/building.png" alt="Building" width={128} height={128} />

                            </div>
                            <h3 className="text-lg font-semibold text-navy/80">Community Map</h3>
                            <p className="text-xs text-muted max-w-[200px] text-center mt-2">
                                {result?.status === 'under_funded' ? 'Roads are broken. Schools need funding.' :
                                    result?.status === 'excessive_taxation' ? 'Shops are closing. Economy is likely to stall.' :
                                        'Thriving! Public services are funded.'}
                            </p>
                        </div>

                        {/* Controls */}
                        <div className="bg-white p-8 rounded-3xl shadow-glow-primary border border-white space-y-6">
                            <h2 className="text-lg font-bold text-navy flex items-center gap-2">
                                <Image src="/icons/Fiscal.png" alt="Building" width={36} height={36} />
                                Fiscal Controls
                            </h2>

                            <Slider
                                label="Corporate Tax Rate"
                                min={0}
                                max={0.60}
                                value={taxRate}
                                onChange={(e) => setTaxRate(parseFloat(e.target.value))}
                                formatValue={(v) => `${(v * 100).toFixed(0)}%`}
                            />

                            <p className="text-xs text-muted italic">
                                Adjust the slider to find the "Sweet Spot" between funding services and encouraging growth.
                            </p>
                        </div>
                    </div>

                    {/* RIGHT COLUMN: Feedback & Rewards */}
                    <div className="md:col-span-5 space-y-10 flex flex-col">
                        {/* AI Coach */}
                        <div className="flex-1">
                            <AICoach
                                message={result?.coach_message || "Adjust the sliders to start the simulation..."}
                                visible={true}
                            />
                        </div>

                        {/* Rewards Section */}
                        <div className="bg-white p-8 rounded-3xl border border-white relative overflow-hidden shadow-glow-primary">
                            <div className="relative z-10 space-y-8">
                                <h3 className="text-sm font-bold text-navy uppercase tracking-wider flex items-center gap-2">
                                    <Image src="/icons/trophy.png" alt="Trophy" width={36} height={36} />
                                    Your Wallet
                                </h3>

                                <VisaCard
                                    balance={earnings}
                                    glow={result?.status === 'balanced_budget'}
                                />

                                <div className="flex justify-center pt-2">
                                    <Badge unlocked={!!result?.badge_eligible} />
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </main>
        </div>
    );
};
