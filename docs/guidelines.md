# SwNE Annotation Guidelines

Our annotation generally follows the [OntoNotes Named Entity Guidelines](ontonotes_named_entity_guidelines-v14.pdf).

> Jim bought 300 shares of Apple in 2006.<br>
> [Jim PER] bought [300 shares QUAN] of [Apple ORG] in [2006 DATE].  

## Named Entity Tags

* **PER** (person)
Proper names, nicknames. Include generational markers (jr., IV), but not honorifics or titles.
	* [Jim]
	* Congressman [Jim Brown, Sr.]
	* Mr. [Brown]
* **NORP** (nationality, other, religion, political)
Adjectival forms of nationality, religion, politics.
	* the [Democratic] candidate
	* three [Christians]
	* [American] forces
	* [Eastern European] cuisine
* **FAC** (facility)
Man-made infrastructure. If buildings are referred to by the company name, mark with FAC if they refer to the physical structure of the building.
	* the [Lincoln Memorial]
	* [5th Avenue]
	* [I-95]
	* [Hartsfield-Jackson International Airport]
* **ORG** (organization)
Names of companies, educational institutions, sports teams, terrorist groups.
	* the [New York Times]
	* [Emory University]
	* the [Supreme Court]
	* [Bank of America]
* **GPE** (geographical political entities)
Names of countries, cities, provinces. Directional modifiers are not marked.
	* southern [California]
	* **[Dallas, Texas]**
* **LOC** (location)
Geographical locations that aren't GPEs like mountain ranges, planets, bodies of water, neighborhoods, named regions. Deictics such as here/there/everywhere are not marked. Directional modifiers are not marked unless they are part of the location name.
	* northern [Chinatown]
	* [Eastern Europe]
	* **[SoCal]**
* **REL** (politics, religion)
Any named religion, political leaning in a noun form.
	* practicing [Christianity]
	* the [Republicans]
* **PRODUCT** 
Model name and number. Credit cards, checking accounts, etc are not marked.
	* Apple [iPhone]
	* [Post-it]
	* Ford [Focus]
* **DATE**
References to dates or periods **longer than 24 hours**. Rate expressions such as "once per year" are not marked. Do not separate mentions into their component parts.
	* [seventies] fashion
	* [2 days ago]
	* the [spring of 2016]
	* [tomorrow]
	* [Monday]
	* for [several years]
	* **every [weekend]**
* **TIME**
**References to periods of time less than 24 hours.** Do not separate mentions into their component parts.
	* [three hours]
	* [evening]
	* [1:00 am]
	* **[1:00 in the morning]**
* **MONEY**
Include monetary unit but do not mark unit in rate expressions such as "$3 per share". General references to money should not be marked.
	* [50 yen]
	* [one million dollars] apiece
* **QUAN** (quantity)
Measurements with explicit standardized units. **Include the whole statement of quantity, but standalone numbers with implicit units of measurment are not marked.**
	* [4 ounces]
	* [4 miles]
	* **it was [50 degrees] yesterday, but today it is 35**
	* **[one hundred or so pounds]**
	* **[30 or 40 miles] inland**
* **CARD** (cardinal)
Numbers that don't fall under measurments, money, date, or time. **Mark any standalone numbers, except when used in a referential sense**
	* [thousands] of books
	* **it was 50 degrees yesterday, but today it is [35]**
	* **that wasn't the one I wanted**
* **EVENT**
Named hurricanes, wars, sports events, and battles.
	* [2007 World Series]
	* the [Oscars]
	* [Hurricane Katrina]
	* [9/11]
* **WOA** (work of art)
Titles of books, songs, television programs, awards.
	* the [Bible]
	* her [Oscar] nomination
	* [Toy Story]
* **LAW**
Any document that has been made into law including treaties and legal documents.
	* the [Bill of Rights]
	* [IRS code 4]
	* the [1988 trade act]
* **LANG** (language)
Any named language
	* [Catalan]
	* [Xhosa]
	* [Latin]


## Notes

* Determiners are not included unless part of the official name:
  > the [Supreme Court]
* If an entity can be classified into multiple tags, choose the most specific one:
  > [40 minutes] is `TIME` not `QUANTITY`
* General references are not annotated:
  > [his time in jail] is not annotated as `TIME`
  > [the money he invested] is not annotated as `MONEY`
* Don't mark syntactic expletives:
  > [Jesus Christ] is not `PER` unless the actual person is being referred to