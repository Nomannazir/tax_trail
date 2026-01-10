# Tax Trail - Backend Developer Guide

This directory contains the Django backend for the "Tax Trail" game module. It handles the game logic (TaxationMarketEngine), CRA metadata compliance generation, and provides APIs for the frontend.

## Prerequisites
- Python 3.12+
- `pip` (Python package manager)

## Setup & partial installation

1.  **Navigate to the project root:**
    ```bash
    cd d:/upwork/projects/tax_trail
    ```

2.  **Activate Virtual Environment:**
    ```bash
    # Windows
    venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r backend/requirements.txt
    ```
    *(Note: If strict requirements file doesn't exist, ensure `django`, `djangorestframework`, `drf-yasg`, `django-cors-headers` are installed)*.

4.  **Run Migrations:**
    ```bash
    cd backend
    python manage.py migrate
    ```

## Running the Server

Start the development server:

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

## API Documentation (Swagger)

We use `drf-yasg` for automatic OpenAPI documentation.

- **Swagger UI:** `http://127.0.0.1:8000/swagger/`
- **ReDoc:** `http://127.0.0.1:8000/redoc/`
- **JSON Spec:** `http://127.0.0.1:8000/swagger.json/`

### Key Endpoints

- **`POST /api/simulate/`**: Engine calculation.
    - **Input:** `{"tax_rate": 0.15, "spending_plan": {}}`
    - **Output:** Status (`under_funded`, `balanced_budget`, `excessive_taxation`), Revenue, Coach Message.
- **`GET /api/cra-metadata/`**: Compliance JSON generator.

## Testing

Run the unit tests to verify the `TaxationMarketEngine` logic and Compliance generation:

```bash
python manage.py test game
```

## Project Structure

- `game/market_engine.py`: Core logic for calculating fiscal impact.
- `game/compliance.py`: Generates the CRA JSON payload.
- `game/serializers.py`: DRF Serializers for validation.
- `game/views.py`: API ViewSets.
