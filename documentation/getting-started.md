# Getting Started

This guide walks you through making your first request to the Gundam Card Game TCG API.

## Base URL

All API requests are made to: https://gundam-tcg-api.onrender.com
No authentication is required. All endpoints are publicly accessible.

## Prerequisites

You need one of the following to make API requests:

- **curl** — available in any terminal or command prompt
- **Postman** — recommended for exploring the API interactively
- Any HTTP client or programming language with HTTP support

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
    "AP": "3",
    "Color": "Red",
    "Cost": "2",
    "Edition": "1",
    "HP": "3",
    "Level": "3",
    "Link": "-",
    "Name": "Char's Zaku II",
    "Rarity": "R",
    "Skill": "【Deploy】...",
    "Source": "ST03",
    "Trait": "(Zeon) (Newtype)",
    "Type": "UNIT",
    "Zone": "Space"
  }
]
```

## Combining Filters

You can combine multiple query parameters to narrow results:

```bash
curl "https://gundam-tcg-api.onrender.com/cards?color=red&type=unit"
```

This returns all red unit cards.

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
