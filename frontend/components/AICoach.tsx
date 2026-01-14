import React from 'react';

interface AICoachProps {
    message: string;
    visible: boolean;
}

export const AICoach: React.FC<AICoachProps> = ({ message, visible }) => {
    if (!visible || !message) return null;

    return (
        <div className="relative animate-in fade-in slide-in-from-bottom-5 duration-500 max-w-md">
            {/* Coach Avatar/Icon */}
            <div className="absolute -left-3 -top-3 bg-white p-2 rounded-full shadow-glow-accent border border-secondary z-10 w-10 h-10 flex items-center justify-center text-xl">
                ✨
            </div>

            {/* Bubble */}
            <div className="bg-white p-6 rounded-3xl rounded-tl-sm border border-gray-100 shadow-glow-primary">
                <h4 className="text-xs font-bold text-secondary uppercase tracking-wider mb-1">Infiniti AI Coach</h4>
                <div
                    className="text-sm text-foreground/90 whitespace-pre-line leading-relaxed"
                    dangerouslySetInnerHTML={{ __html: message.replace(/\n/g, '<br />') }}
                />
            </div>
        </div>
    );
};
