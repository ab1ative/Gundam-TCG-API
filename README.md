# Gundam Card Game TCG API

A REST API for accessing Gundam Card Game TCG card data. Returns card details,
set information, and supports filtering by color, type, and name.

**Base URL:** `https://gundam-tcg-api.onrender.com`

> **Note:** This API is hosted on Render's free tier. If the service has been
> inactive, the first request may take up to 50 seconds.

## Quick Start

```bash
curl "https://gundam-tcg-api.onrender.com/cards?color=red"
```

## Endpoints


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

Card data sourced from the Gundam TCG community spreadsheet. Covers sets ST01,
ST02, ST03, ST04, and GD01.

## Built With

- Python
- Flask
- Deployed on Render
