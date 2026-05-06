# my_ml_service
My Machine Learning Web Service

## Features

- **Income Classifier API**: Predicts if income is <=50K or >50K using Random Forest and Extra Trees algorithms
- **A/B Testing**: Compare two ML algorithms to find the better performing one
- **REST API with Django REST Framework**: Well-structured API endpoints
- **Dockerized Application**: Easy deployment with Docker and docker-compose

## Algorithms

1. **Random Forest** (Production)
2. **Extra Trees** (Testing)

## Local Development

### Prerequisites
- Python 3.8+
- Docker and docker-compose

### Running without Docker

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Apply migrations:
```bash
cd backend/server
python manage.py migrate
```

3. Run the server:
```bash
python manage.py runserver
```

4. Open your browser at http://localhost:8000

### Running with Docker

1. Build and start containers:
```bash
docker-compose up --build
```

2. Open your browser at http://localhost:8000

3. To stop containers:
```bash
docker-compose down
```

## API Endpoints

- `/api/v1/endpoints` - List all API endpoints
- `/api/v1/mlalgorithms` - List all registered ML algorithms
- `/api/v1/mlalgorithmstatuses` - List all ML algorithm statuses
- `/api/v1/mlrequests` - List all prediction requests
- `/api/v1/abtests` - List and create A/B tests
- `/api/v1/income_classifier/predict` - Predict income classification
- `/api/v1/stop_ab_test/<ab_test_id>` - Stop an A/B test and compute results

## License

MIT

