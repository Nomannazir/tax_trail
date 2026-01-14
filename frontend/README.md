# Tax Trail - Frontend (Next.js)

This is the frontend for the "Tax Trail" game module, built with Next.js 15, Tailwind CSS v4.

## Setup

1.  **Navigate to directory:**
    ```bash
    cd tax_trail/frontend
    ```

2.  **Install dependencies:**
    ```bash
    npm install
    ```

## Development

Run the development server:

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

## Configuration

- **API URL**: Configured in `lib/api.ts` -> `http://127.0.0.1:8000/api`. Ensure the Backend server is running on port 8000.
- **Styling**: `app/globals.css` contains the Life Hub design tokens using Tailwind v4 `@theme`.
- **Fonts**: uses `next/font/google` for Poppins.

## Project Structure

- `components/TaxGame.tsx`: Main game controller.
- `components/ui/`: Reusable UI elements (Slider).
- `components/AICoach.tsx`: Chat bubble feedback.
- `components/VisaCard.tsx`: Reward visualization.
