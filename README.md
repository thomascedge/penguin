# Penguin

Penguin is a Fetch Rewards App copycat. The service allows a user to scan a receipt and gain points based on our scoring criteria. This document serves as an outline to the project.

## Architecture

This is a python-based project that uses FastAPI endpoints to connect to the scoring service backend. The user takes a photo of their receipt, the information is processed by Chick, the image processing service, scored, and saved in the backend. Once the receipt is processed, the score is returned to the client.

```mermaid
flowchart LR
	A[Client]
	B{Penguin API}
	C([Chick])
	D([Scoring Service])
	E[(Database)]
	
	A --> B
	B --> C
	C --> B
	B --> D
	D --> E
```

## Database

The database uses a SQL-style approach with three tables: USER, RECEIPT, and ITEM. The schema (attempts) at 3NF, relating `user_id` between USER and RECEIPT tables and `receipt_id` between RECEIPT and ITEM tables.
```mermaid
erDiagram	
  USER ||--o{ RECEIPT : scans
	RECEIPT ||--|{ ITEM : contains

	USER {
		string id PK
		string name
		string birthday
		string address_street
		string address_state
		string address_country
		string address_zip_code
		string email
		datetime account_create_datetime
		date dwh_created_date
		date dwh_update_date
		string dwh_table_name
		string dwh_primary_key
	}
	
	RECEIPT {
		string id PK
		string user_id FK
		datetime receipt_entry_date
		string receipt_retailer
		date receipt_purchase_date
		time receipt_purchase_time
		integer receipt_total
		datetime account_create_datetime
		date dwh_created_date
		date dwh_update_date
		string dwh_table_name
		string dwh_primary_key
	}
	
	ITEM {
		string id PK
		string receipt_id FK
		string description
		integer total
		datetime account_create_datetime
		date dwh_created_date
		date dwh_update_date
		string dwh_table_name
		string dwh_primary_key
	}
```
