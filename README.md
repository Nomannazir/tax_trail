# tax_trail

## Backend Setup

    ```bash
    cd tax_trail

    # Windows
    python -m venv venv
    venv\Scripts\activate

    cd backend
    pip install -r requirements.txt

    python manage.py migrate

    python manage.py runserver
    ```

The API will be available at `http://127.0.0.1:8000/`.


## Frontend Setup

    ```bash
    cd tax_trail/frontend
    
    npm install
    
    npm run dev
    ```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.





# Migration Guide: Tax Trail to Life Hub Core

This guide outlines the steps to migrate the standalone "Tax Trail" module into the main Life Hub application (Next.js + Django / Microservices).

## Backend Migration

1.  **Copy the App**:
    - Copy the `backend/game` folder into your main Django repository's `apps/` directory.

2.  **Register App**:
    - Add `'apps.game'` to `INSTALLED_APPS` in your main `settings.py`.

3.  **URLs**:
    - Include the game URLs in your main `urls.py`:
    ```python
    path('api/tax-trail/', include('apps.game.urls')),
    ```

4.  **Dependencies**:
    - Ensure `drf-yasg` is installed if you want the Swagger docs to persist.


## Frontend Migration

1.  **Copy Components**:
    - Copy `frontend/components/TaxGame.tsx`, `AICoach.tsx`, `VisaCard.tsx`, `Badge.tsx` to your main repo's components folder (e.g., `src/features/tax-trail/`).
    - Copy `frontend/components/ui/Slider.tsx` to your shared UI library or keep local.

2.  **Styles**:
    - **Check `globals.css`**: Ensure the CSS variables (`--color-primary`, `--font-poppins`) are defined in your main app. If you use Tailwind v3, you may need to port the v4 `@theme` config to `tailwind.config.js` `theme.extend`.

3.  **API Integration**:
    - Copy `frontend/lib/api.ts` to your services folder.
    - Update `API_BASE_URL` to point to your main backend (e.g., process.env.NEXT_PUBLIC_API_URL).

