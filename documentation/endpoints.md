markdown
# API Reference

Complete reference for all Gundam Card Game TCG API endpoints.

**Base URL:** `https://gundam-tcg-api.onrender.com`

---

## GET /cards

Returns all cards in the database. Supports optional filtering by color, type,
and name.

### Query Parameters


|
 Parameter 
|
 Type 
|
 Required 
|
 Description 
|
|
-----------
|
------
|
----------
|
-------------
|
|
`color`
|
 string 
|
 No 
|
 Filter by card color. Case-insensitive. 
|
|
`type`
|
 string 
|
 No 
|
 Filter by card type. Case-insensitive. 
|
|
`name`
|
 string 
|
 No 
|
 Search by partial card name. Case-insensitive. 
|

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
    "AP": "3",
    "Card #": "GD01-001",
    "Color": "Green",
    "Cost": "2",
    "Edition": "1",
    "HP": "3",
    "Level": "3",
    "Link": "Pilot Name",
    "Name": "Heavyarms",
    "Rarity": "R",
    "Skill": "【Deploy】Choose 1 enemy Unit with 3 or less HP. Deal 2 damage to it.",
    "Source": "GD01",
    "Trait": "(Operation Meteor)",
    "Type": "UNIT",
    "Zone": "Space Earth"
  }
]
```

### Returns

An array of card objects matching the specified filters. Returns all cards if
no filters are provided. Returns an empty array if no cards match.

---

## GET /cards/{name}

Returns a single card by exact name match.

### Path Parameters


|
 Parameter 
|
 Type 
|
 Required 
|
 Description 
|
|
-----------
|
------
|
----------
|
-------------
|
|
`name`
|
 string 
|
 Yes 
|
 The exact name of the card. Case-insensitive. 
|

### Example Request

```bash
curl "https://gundam-tcg-api.onrender.com/cards/White Base"
```

### Example Response

```json
[
  {
    "AP": "-",
    "Card #": "ST01-015",
    "Color": "Blue",
    "Cost": "2",
    "Edition": "1",
    "HP": "5",
    "Level": "3",
    "Link": "-",
    "Name": "White Base",
    "Rarity": "C",
    "Skill": "【Burst】Deploy this card. 【Deploy】Add 1 of your Shields to your hand. 【Activate･Main】【Once per Turn】②：Deploy 1 [Gundam] Unit token if you have 0 Units in play.",
    "Source": "ST01",
    "Trait": "(Earth Federation) (White Base Team) (Warship)",
    "Type": "BASE",
    "Zone": "Space Earth"
  }
]
```

### Returns

An array of matching card objects. Returns multiple results if the same card
name appears across different sets or editions.

### Error Response

```json
{
  "error": "Card not found"
}
```

---

## GET /sets

Returns a sorted list of all available set codes.

### Example Request

```bash
curl "https://gundam-tcg-api.onrender.com/sets"
```

### Example Response

```json
[
  "GD01",
  "ST01",
  "ST02",
  "ST03",
  "ST04"
]
```

### Returns

A sorted array of set code strings.

---

## GET /sets/{set_code}/cards

Returns all cards belonging to a specific set.

### Path Parameters


|
 Parameter 
|
 Type 
|
 Required 
|
 Description 
|
|
-----------
|
------
|
----------
|
-------------
|
|
`set_code`
|
 string 
|
 Yes 
|
 The set code. Case-insensitive. 
|

### Example Request

```bash
curl "https://gundam-tcg-api.onrender.com/sets/GD01/cards"
```

### Example Response

```json
[
  {
    "AP": "-",
    "Card #": "GD01-099",
    "Color": "Blue",
    "Cost": "2",
    "Edition": "1",
    "HP": "-",
    "Level": "4",
    "Link": "-",
    "Name": "Intercept Orders",
    "Rarity": "R",
    "Skill": "【Burst】Choose 1 enemy Unit with 5 or less HP. Rest it. 【Main】/【Action】Choose 1 to 2 enemy Units with 3 or less HP. Rest them.",
    "Source": "GD01",
    "Trait": "-",
    "Type": "COMMAND",
    "Zone": "-"
  }
]
```

### Returns

An array of all card objects in the specified set.

### Error Response

```json
{
  "error": "Set not found"
}
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
| `source` | string | The set code, e.g. `GD01` |
| `card_number` | string | The card's number within its set |
| `edition` | string | Print edition: `1`, `β`, or `P` |

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
    "zone": "Space Earth",
    "trait": "(Earth Federation) (White Base Team)",
    "source": "GD01"
  }'
```

### Example Response

```json
{
  "id": 501,
  "name": "RX-78-2 Gundam",
  "color": "Blue",
  "type": "UNIT",
  "level": "3",
  "cost": "3",
  "ap": "3",
  "hp": "3",
  "zone": "Space Earth",
  "trait": "(Earth Federation) (White Base Team)",
  "link": "",
  "skill": "",
  "source": "GD01",
  "card_number": "",
  "edition": "",
  "rarity": ""
}
```

### Returns

The newly created card object with its assigned `id`. Returns HTTP 201 on success.

---

## PUT /cards/{id}

Updates an existing card by its database ID. Only the fields you include in the request body will be updated — all other fields remain unchanged.

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
  "id": 501,
  "name": "RX-78-2 Gundam",
  "color": "Blue",
  "type": "UNIT",
  "level": "3",
  "cost": "3",
  "ap": "5",
  "hp": "5",
  "zone": "Space Earth",
  "trait": "(Earth Federation) (White Base Team)",
  "link": "",
  "skill": "",
  "source": "GD01",
  "card_number": "",
  "edition": "",
  "rarity": ""
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
