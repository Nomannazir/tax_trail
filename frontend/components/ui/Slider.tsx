import React from 'react';
import { clsx } from 'clsx';
import { twMerge } from 'tailwind-merge';

interface SliderProps extends React.InputHTMLAttributes<HTMLInputElement> {
    label: string;
    value: number;
    min: number;
    max: number;
    onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
    formatValue?: (val: number) => string;
}

export const Slider: React.FC<SliderProps> = ({
    label,
    value,
    min,
    max,
    onChange,
    formatValue,
    className,
    ...props
}) => {
    const percentage = ((value - min) / (max - min)) * 100;

    return (
        <div
            className={twMerge("flex flex-col gap-3 w-full p-4 rounded-2xl border border-border-light", className)}
            style={{ backgroundColor: 'var(--color-input-bg)' }}
        >
            <div className="flex justify-between items-center text-foreground">
                <label className="font-semibold text-xs uppercase tracking-widest opacity-70">{label}</label>
                <span className="font-bold text-primary font-mono">{formatValue ? formatValue(value) : value}</span>
            </div>
            <div className="relative w-full h-4">
                {/* Track Background - Now distinct from the container bg */}
                <div className="absolute top-1/2 -translate-y-1/2 left-0 w-full h-1.5 bg-navy/10 rounded-full" />

                {/* Fill Track */}
                <div
                    className="absolute top-1/2 -translate-y-1/2 left-0 h-1.5 bg-secondary rounded-full"
                    style={{ width: `${percentage}%` }}
                />

                <input
                    type="range"
                    min={min}
                    max={max}
                    step={0.01}
                    value={value}
                    onChange={onChange}
                    className="absolute top-1/2 -translate-y-1/2 left-0 w-full h-4 opacity-0 cursor-pointer z-10"
                    {...props}
                />

                <div
                    className="absolute top-1/2 -translate-y-1/2 w-5 h-5 bg-white border-2 border-primary rounded-full shadow-glow-primary pointer-events-none transition-all duration-75 ease-out"
                    style={{ left: `calc(${percentage}% - 10px)` }}
                />
            </div>
        </div>
    );
};
