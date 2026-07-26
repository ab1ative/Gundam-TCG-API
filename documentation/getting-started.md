# Getting Started

This guide walks you through making your first request to the Gundam Card Game TCG API.

## Base URL

All API requests are made to: https://gundam-tcg-api.onrender.com

## Authentication

No authentication is required. All endpoints are publicly accessible.

## Prerequisites

You need one of the following to make API requests:

- **curl** — available in any terminal or command prompt
- **Postman** — recommended for exploring the API interactively
- Any HTTP client or programming language with HTTP support, including your web browser

## Your First Request

Retrieve all red cards in the database:

**curl**
```bash
curl "https://gundam-tcg-api.onrender.com/cards?color=red"
```

**Postman**
1. Open Postman and create a new HTTP request
2. Set the method to **GET**
3. Enter the URL: `https://gundam-tcg-api.onrender.com/cards?color=red`
4. Click **Send**

**Response**
```json
[
  {
        "name": "LaGOWE",
        "color": "Red",
        "level": "3",
        "cost": "2",
        "ap": "2",
        "hp": "3",
        "id": 256,
        "type": "UNIT",
        "rarity": "R",
        "trait": "(ZAFT)",
        "link": "(ZAFT) Trait",
        "skill": "【Attack】If this Unit has 5 or more AP and it is attacking an enemy Unit, choose 1 enemy Unit. Deal 2 damage to it.",
        "source": "GD01",
        "card_number": "050",
        "edition": "1"
    },
]
```

## Combining Filters

You can combine multiple query parameters to narrow results:

```bash
curl "https://gundam-tcg-api.onrender.com/cards?color=red&type=unit"
```

This returns all red unit cards.

**Response**
```json
[
    {
        "name": "Kshatriya",
        "color": "Red",
        "level": "5",
        "cost": "4",
        "ap": "5",
        "hp": "4",
        "id": 246,
        "type": "UNIT",
        "rarity": "LR",
        "trait": "(Neo Zeon)",
        "link": "[Marida Cruz]",
        "skill": "【When Paired･(Cyber-Newtype)/(Newtype) Pilot】Choose 1 to 2 enemy Units. Deal 1 damage to them.",
        "source": "GD01",
        "card_number": "044",
        "edition": "1"
    }
]
```

## Response Format

All responses are returned as JSON. Successful requests return either:

- An **array** of card objects (for list endpoints)
- A **single card object** (for exact name lookups)
- An **error object** if the requested resource is not found:

```json
{
  "error": "Card not found"
}
```

## HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 404 | Card or set not found |
| 500 | Server error |

## Next Steps

- See [Endpoints](endpoints.md) for the full API reference
- See [Data Model](data-model.md) for a description of every card field****
