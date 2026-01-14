import React from 'react';
import { clsx } from 'clsx';

interface VisaCardProps {
    balance: number;
    glow?: boolean;
}

export const VisaCard: React.FC<VisaCardProps> = ({ balance, glow = false }) => {
    return (
        <div className={clsx(
            "relative w-full aspect-[1.586] rounded-xl overflow-hidden text-white p-4 flex flex-col justify-between transition-all duration-500",
            "bg-gradient-to-br from-navy to-primary shadow-lg",
            glow && "shadow-glow-high ring-2 ring-secondary/50 scale-105"
        )}>
            {/* Background decoration */}
            <div className="absolute top-0 right-0 w-32 h-32 bg-secondary/10 rounded-full -translate-y-1/2 translate-x-1/2 blur-2xl" />

            <div className="flex justify-between items-start z-10">
                <span className="font-bold tracking-wider opacity-80">Life Hub Visa</span>
                <div className="text-xs font-bold border border-white/40 px-1 rounded opacity-60">VISA</div>
            </div>

            <div className="z-10">
                <p className="text-xs opacity-70 mb-1">Current Balance</p>
                <p className="text-2xl font-bold font-mono tracking-widest">
                    ${balance.toFixed(2)}
                </p>
            </div>

            {/* Chip */}
            <div className="absolute top-1/2 left-4 -translate-y-1/2 w-8 h-6 bg-yellow-200/20 rounded border border-yellow-200/40" />
        </div>
    );
};
