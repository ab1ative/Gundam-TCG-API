# Gundam Card Game TCG API

A REST API for accessing Gundam Card Game TCG card data. Returns card details, and supports filtering by color, type, name, AP, HP, and rarity. Currently the API only supports GD01, Beta, and ST01-04; you can help expand the API using POST commands to incorporate new cards into the database.

This is a personal project

**Base URL:** `https://gundam-tcg-api.onrender.com`

> **Note:** This API is hosted on Render's free tier. If the service has been
> inactive, the first request may take up to 50 seconds.

## Quick Start

The following, input into command prompt, will return a list of all red cards in the database:

```bash
curl "https://gundam-tcg-api.onrender.com/cards?color=red"
```

## Endpoints

Gundam TCG API supports GET, POST, PUT, and DELETE endpoints.

GET returns an array of cards in the database matching user-chosen parameters.
POST creates a new card with a unique id at the end of the database based on JSON code.
PUT revises a card 

|
 Method 
|
 Endpoint 
|
 Description 
|
|
--------
|
----------
|
-------------
|
|
 GET 
|
`/cards`
|
 Returns all cards, with optional filters 
|
|
 GET 
|
`/cards/{name}`
|
 Returns a specific card by exact name 
|
|
 GET 
|
`/sets`
|
 Returns all available set codes 
|
|
 GET 
|
`/sets/{set_code}/cards`
|
 Returns all cards in a set 
|

## Filtering

The `/cards` endpoint supports query parameters:


|
 Parameter 
|
 Description 
|
 Example 
|
|
-----------
|
-------------
|
---------
|
|
`color`
|
 Filter by card color 
|
`?color=red`
|
|
`type`
|
 Filter by card type 
|
`?type=unit`
|
|
`name`
|
 Search by partial name 
|
`?name=gundam`
|

## Running Locally

**Requirements:** Python 3.8+

```bash
git clone https://github.com/ab1ative/gundam-card-api.git
cd gundam-card-api
pip install -r requirements.txt
python app.py
```

The API will run at `http://127.0.0.1:5000`.

## Data

Thank you to the [deleted] Redditor who put this spreadsheet together, which I exported as a .csv and made into gundam.db: https://docs.google.com/spreadsheets/d/1bN1HV-gAkbjbuHfZTTQPNlRjwohG2zcEloiw1lOn-x0/edit?gid=913580340#gid=913580340.

## Built With

- Python
- Flask
- Deployed on Render
