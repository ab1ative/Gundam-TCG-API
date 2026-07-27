# Data Model

Every card object returned by the API contains the following fields.

## Card Object

```json
{
  "Name": "White Base",
  "Color": "Blue",
  "Rarity": "C",
  "Level": "3",
  "Cost": "2",
  "Type": "BASE",
  "AP": "-",
  "HP": "5",
  "Trait": "(Earth Federation) (White Base Team) (Warship)",
  "Link": "-",
  "Skill": "【Burst】Deploy this card...",
  "Set": "ST01",
  "Number": "015",
  "Printing": "1"
}
```

## Field Descriptions


|
 Field 
|
 Type 
|
 Description 
|
|
-------
|
------
|
-------------
|
|
`id`
|
integer
|
Unique database identifier assigned automatically on creation
|
|
`Name`
|
 string 
|
 The card's full name as printed 
|
|
`Color`
|
 string 
|
 The card's color identity. See 
[
Colors
](
#colors
)
. 
|
|
`Rarity`
|
 string 
|
 The card's rarity. See 
[
Rarities
](
#rarities
)
. 
|
|
`Level`
|
 string 
|
 The card's level, used for deployment requirements 
|
|
`Cost`
|
 string 
|
 The resource cost to play the card 
|
|
`Type`
|
 string 
|
 The card type. See 
[
Card Types
](
#card-types
)
. 
|
|
`AP`
|
 string 
|
 Attack Points. Applies to Unit and Pilot cards. 
`-`
 for cards with no AP value. 
|
|
`HP`
|
 string 
|
 Hit Points. Applies to Unit and Base cards. 
`-`
 for cards with no HP value. 
|
|
`Zone`
|
 string 
|
 The zones where this card can be deployed: 
`Space`
, 
`Earth`
, or 
`Space Earth`
. 
`-`
 for cards with no zone restriction. 
|
|
`Trait`
|
 string 
|
 Faction and keyword traits in parentheses, e.g. 
`(Zeon) (Newtype)`
. 
`-`
 if none. 
|
|
`Link`
|
 string 
|
 The Pilot name required to Link with this card. 
`-`
 if not applicable. 
|
|
`Skill`
|
 string 
|
 The card's full effect text as printed, including timing keywords in 【】brackets. 
|
|
`Source`
|
 string 
|
 The set code this card was printed in. See 
[
Sets
](
#sets
)
. 
|
|
`Card #`
|
 string 
|
 The card's number within its set 
|
|
`Edition`
|
 string 
|
 The print edition. 
`1`
 for first edition, 
`β`
 for beta edition, 
`P`
 for promotional. 
|

---

## Colors


|
 Value 
|
 Description 
|
|
-------
|
-------------
|
|
`Red`
|
 Aggressive color focused on dealing damage 
|
|
`Blue`
|
 Control color focused on resting and disrupting enemy units 
|
|
`Green`
|
 Resource and ramp color focused on deployment advantage 
|
|
`White`
|
 Defensive color focused on Blocker units and returning cards 
|

---

## Card Types


|
 Value 
|
 Description 
|
|
-------
|
-------------
|
|
`UNIT`
|
 Mobile suit cards that battle in the unit zone. Have AP and HP values. 
|
|
`PILOT`
|
 Pilot cards that Link with Units to enhance them. Have AP and HP values that add to the linked Unit. 
|
|
`COMMAND`
|
 Spell-like cards played for immediate effects. No AP or HP. 
|
|
`BASE`
|
 Warship and stronghold cards that provide ongoing effects. Have HP but no AP. 
|

---

## Rarities


|
 Value 
|
 Description 
|
|
-------
|
-------------
|
|
`C`
|
 Common 
|
|
`C +`
|
 Common foil 
|
|
`U`
|
 Uncommon 
|
|
`U +`
|
 Uncommon foil 
|
|
`R`
|
 Rare 
|
|
`R +`
|
 Rare foil 
|
|
`RR`
|
 Double Rare 
|
|
`RR +`
|
 Double Rare foil 
|

---

## Sets


|
 Code 
|
 Name 
|
|
------
|
------
|
|
`ST01`
|
 Starter Deck 01 — Heroic Beginnings: Gundam 
|
|
`ST02`
|
 Starter Deck 02 — Operation Meteor: Wing Gundam 
|
|
`ST03`
|
 Starter Deck 03 — Char's Ambition: Sazabi 
|
|
`ST04`
|
 Starter Deck 04 — Destiny's Call: Strike Freedom 
|
|
`GD01`
|
 Booster Set 01 — Mobile Suit Gundam 
|

---

## Skill Text Conventions

Skill text uses the following timing keywords enclosed in 【】brackets:


|
 Keyword 
|
 Description 
|
|
---------
|
-------------
|
|
`【Burst】`
|
 Triggers when this card is revealed from the shield area 
|
|
`【Deploy】`
|
 Triggers when this card enters play 
|
|
`【Main】`
|
 Can be activated during your main phase 
|
|
`【Action】`
|
 Can be activated during either player's turn 
|
|
`【Activate･Main】`
|
 Rest this card to activate during main phase 
|
|
`【Once per Turn】`
|
 This effect can only be used once per turn 
|
|
`【Pilot】`
|
 Indicates the Pilot card that can Link with this Unit 
|
