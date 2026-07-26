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
