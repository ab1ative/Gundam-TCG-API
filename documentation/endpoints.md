# API Reference

Complete reference for all Gundam Card Game TCG API endpoints.

**Base URL:** `https://gundam-tcg-api.onrender.com`

---

## GET /cards

Returns all cards in the database. Supports optional filtering by color, type,
and name.

### Query Parameters


| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `color` | string | No | Filter by card color. Case-insensitive. |
| `type` | string | No | Filter by card type. Case-insensitive. |
| `name` | string | No | Search by partial card name. Case-insensitive. |
| `level` | string | No | Filter by card level. Exact match. |

### Example Requests

**All cards**
```bash
curl "https://gundam-tcg-api.onrender.com/cards"
```

**Filter by color**
```bash
curl "https://gundam-tcg-api.onrender.com/cards?color=blue"
```

**Filter by type**
```bash
curl "https://gundam-tcg-api.onrender.com/cards?type=command"
```

**Search by name**
```bash
curl "https://gundam-tcg-api.onrender.com/cards?name=zaku"
```

**Combine filters**
```bash
curl "https://gundam-tcg-api.onrender.com/cards?color=green&type=unit"
```

### Example Response

```json
[
  {
    "Name": "Heavyarms",
    "Id": 1,
    "Color": "Green",
    "Rarity": "R",
    "Level": "3",
    "Cost": "2",
    "Type": "UNIT",
    "AP": "3",
    "HP": "3",
    "Trait": "(Operation Meteor)",
    "Link": "(Operation Meteor) Trait",
    "Skill": "【Deploy】Choose 1 enemy Unit with 3 or less HP. Deal 2 damage to it.",
    "Set": "GD01",
    "Number": "001",
    "Printing": "1"
  }
]
```

### Returns

An array of card objects matching the specified filters. Returns all cards if
no filters are provided. Returns an empty array if no cards match.

### Error Response

```json
{
  "error": "No cards found matching the specified filters"
}
```

---

## GET /cards/{id}

Returns a single card by its database ID.

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | integer | Yes | The card's database ID. |

### Example Request

```bash
curl "https://gundam-tcg-api.onrender.com/cards/15"
```

---

## GET /sets

Returns a sorted list of all available set codes.

### Example Request

```bash
curl "https://gundam-tcg-api.onrender.com/sets"
```

---

## GET /sets/{set_code}/cards

Returns all cards belonging to a specific set.

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `set_code` | string | Yes | The set code. Case-insensitive. |

### Example Request

```bash
curl "https://gundam-tcg-api.onrender.com/sets/GD01/cards"
```

---

## POST /cards

Creates a new card and adds it to the database.

### Request Body

Send a JSON object with the following fields. All fields are optional except `name`.

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | **Required.** The card's name |
| `color` | string | The card's color: `Red`, `Blue`, `Green`, or `White` |
| `rarity` | string | The card's rarity, e.g. `C`, `U`, `R` |
| `level` | string | The card's level |
| `cost` | string | The resource cost to play the card |
| `type` | string | The card type: `UNIT`, `PILOT`, `COMMAND`, or `BASE` |
| `ap` | string | Attack Points. Use `-` if not applicable. |
| `hp` | string | Hit Points. Use `-` if not applicable. |
| `zone` | string | Deployment zone: `Space`, `Earth`, or `Space Earth` |
| `trait` | string | Faction and keyword traits in parentheses |
| `link` | string | Pilot name required to Link. Use `-` if not applicable. |
| `skill` | string | The card's full effect text |
| `set` | string | The set code, e.g. `GD01` |
| `number` | string | The card's number within its set |
| `printing` | string | Print edition: `1`, `β`, or `P` |

### Example Request

```bash
curl -X POST https://gundam-tcg-api.onrender.com/cards \
  -H "Content-Type: application/json" \
  -d '{
    "name": "RX-78-2 Gundam",
    "color": "Blue",
    "type": "UNIT",
    "level": "3",
    "cost": "3",
    "ap": "3",
    "hp": "3",
    "trait": "(Earth Federation) (White Base Team)",
    "set": "GD01"
  }'
```

### Example Response

```json
{
  "Name": "RX-78-2 Gundam",
  "Id": 501,
  "Color": "Blue",
  "Type": "UNIT",
  "Level": "3",
  "Cost": "3",
  "AP": "3",
  "HP": "3",
  "Trait": "(Earth Federation) (White Base Team)",
  "Link": "",
  "Skill": "",
  "Set": "GD01",
  "Number": "",
  "Orinting": "",
  "Rarity": ""
}
```

### Returns

The newly created card object with its assigned `id`. Returns HTTP 201 on success.

---

## PUT /cards/{id}

Updates an existing card by its database ID. Only the fields included in the request body will be updated. All other fields remain unchanged.

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | integer | Yes | The card's database ID |

### Request Body

A JSON object containing only the fields you want to update.

### Example Request

```bash
curl -X PUT https://gundam-tcg-api.onrender.com/cards/501 \
  -H "Content-Type: application/json" \
  -d '{
    "ap": "5",
    "hp": "5"
  }'
```

### Example Response

```json
{
  "Name": "RX-78-2 Gundam",
  "Id": 501,
  "Color": "Blue",
  "Type": "UNIT",
  "Level": "3",
  "Cost": "3",
  "AP": "5",
  "HP": "5",
  "Trait": "(Earth Federation) (White Base Team)",
  "Link": "",
  "Skill": "",
  "Set": "GD01",
  "Number": "",
  "Printing": "",
  "Rarity": ""
}
```

### Returns

The full updated card object. Returns 404 if the card ID does not exist.

### Error Response

```json
{
  "error": "Card not found"
}
```

---

## DELETE /cards/{id}

Deletes a card from the database by its ID.

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | integer | Yes | The card's database ID |

### Example Request

```bash
curl -X DELETE https://gundam-tcg-api.onrender.com/cards/501
```

### Example Response

```json
{
  "message": "Card 501 deleted successfully"
}
```

### Returns

A confirmation message on success. Returns 404 if the card ID does not exist.

### Error Response

```json
{
  "error": "Card not found"
}
```
