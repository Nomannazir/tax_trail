import React from 'react';
import Image from 'next/image';

interface BadgeProps {
    unlocked: boolean;
}

export const Badge: React.FC<BadgeProps> = ({ unlocked }) => {
    if (!unlocked) return (
        <div className="flex flex-col items-center opacity-40 grayscale group">
            <div className="w-16 h-16 rounded-xl border-2 border-dashed border-muted flex items-center justify-center">
                🔒
            </div>
            <span className="text-xs font-semibold mt-2 text-muted">Fiscal Architect</span>
        </div>
    );

    return (
        <div className="flex flex-col items-center animate-in zoom-in spin-in-1 duration-700">
            <div className="relative w-16 h-16 bg-secondary/20 rounded-xl border-2 border-secondary flex items-center justify-center shadow-[0_0_15px_rgba(18,254,162,0.6)]">
                <Image src="/icons/check-circle.png" alt="Trophy" width={64} height={64} />
            </div>
            <span className="text-xs font-bold mt-2 text-primary bg-primary/10 px-2 py-0.5 rounded-full border border-primary/20">Fiscal Architect</span>
        </div>
    );
};
