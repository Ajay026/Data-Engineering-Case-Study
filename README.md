# Data-Engineering-Case-Study
# AdvertiseX Data Engineering Case Study

## Project Structure
- `data_ingestion/`: Scripts for ingesting data from various formats (JSON, CSV, Avro).
- `data_processing/`: Scripts for transforming, correlating, and validating data.
- `data_storage/`: Scripts for setting up data storage and optimizing queries.
- `error_handling/`: Scripts for error logging and alerting.
- `tests/`: Unit tests for all components.
- `scripts/`: Shell scripts for running and setting up the project.

## Setup Instructions

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/advertisex-data-engineering.git
    cd advertisex-data-engineering
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the ingestion scripts:
    ```sh
    python data_ingestion/json_ingestion.py
    python data_ingestion/csv_ingestion.py
    python data_ingestion/avro_ingestion.py
    ```

4. Run the data processing scripts:
    ```sh
    python data_processing/transform_data.py
    python data_processing/correlate_data.py
    python data_processing/validate_data.py
    ```

5. Set up storage:
    ```sh
    python data_storage/setup_storage.py
    ```

6. Optimize queries:
    ```sh
    python data_storage/query_optimization.py
    ```

7. Monitor for errors:
    ```sh
    python error_handling/error_monitoring.py
    python error_handling/alerting_system.py
    ```

## Testing

Run the unit tests:
```sh
pytest tests/
