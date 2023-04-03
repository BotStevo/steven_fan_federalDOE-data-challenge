# File Guide
 
## Step 2
Database schema generation scripts:
-  `data/people_schema.sql`
-  `data/places_schema.sql`
- Scripts are mounted in `docker-compose.yml`
## Step 3
Docker configuration data for docker image: 
- `images/data_ingestor/Dockerfile`

Data ingestion script:
- `images/data_ingestor/data_ingestor.py`

## Step 4
Docker configuration data for docker image: 
- `images/summary_generator/Dockerfile`

Data processing script:
- `images/summary_generator/summary_generator.py`

Summary data files:
-  `data/summary_output.json`
-  `data/bonus_summary_output.json`