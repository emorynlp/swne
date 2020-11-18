# SwNE Annotation Guidelines

Our annotation generally follows the [OntoNotes Named Entity Guidelines](ontonotes_named_entity_guidelines-v14.pdf).

> Jim bought 300 shares of Apple in 2006.<br>
> &rarr; [Jim PER] bought [300 shares QUAN] of [Apple ORG] in [2006 DATE].  


## Named Entity Tags

* **PER** (person): proper names, nicknames<br>
  Include generational markers (jr., IV), but not honorifics or titles.
  > [Jim]<br>
  > Congressman [Jim Brown, Sr.]<br>
  > Mr. [Brown]
* **NORP** (nationality, other, religion, political): adjectival forms of nationality, religion, politics
  > the [Democratic] candidate<br>
  > three [Christians]<br>
  > [American] forces<br>
  > [Eastern European] cuisine
* **FAC** (facility): man-made infrastructure<br>
  If buildings are referred to by the company name, mark with FAC if they refer to the physical structure of the building.
  > the [Lincoln Memorial]
  > [5th Avenue]
  > [I-95]
  > [Hartsfield-Jackson International Airport]
* **ORG** (organization): names of companies, educational institutions, sports teams, terrorist groups
  > the [New York Times]
  > [Emory University]
  > the [Supreme Court]
  > [Bank of America]
* **GPE** (geographical political entities): names of countries, cities, provinces<br>
  : Directional modifiers are not marked.
  > southern [California]
  > **[Dallas, Texas]**
* **LOC** (location): geographical locations that aren't GPEs like mountain ranges, planets, bodies of water, neighborhoods, named regions<br>
  : Deictics such as here/there/everywhere are not marked<br>
  : Directional modifiers are not marked unless they are part of the location name
  > northern [Chinatown]<br>
  > [Eastern Europe]<br>
  > **[SoCal]**
* **REL** (politics, religion): any named religion, political leaning in a noun form
  > practicing [Christianity]<br>
  > the [Republicans]
* **PRODUCT**: model name and number<br>
  : Credit cards, checking accounts, etc are not marked
  > Apple [iPhone]<br>
  > [Post-it]<br>
  > Ford [Focus]
* **DATE**: references to dates or periods _longer than 24 hours_<br>
  : Rate expressions such as "once per year" are not marked<br>
  : Do not separate mentions into their component parts
  > [seventies] fashion<br>
  > [2 days ago]<br>
  > the [spring of 2016]<br>
  > [tomorrow]<br>
  > [Monday]<br>
  > for [several years]<br>
  > every **[weekend]**
* **TIME**:
references to periods of time _less than 24 hours_<br>
  : Do not separate mentions into their component parts
  > [three hours]<br>
  > [evening]<br>
  > [1:00 am]<br>
  > **[1:00 in the morning]**
* **MONEY**: include monetary unit but do not mark unit in rate expressions such as "$3 per share"<br>
  : General references to money should not be marked
  > [50 yen]<br>
  > [one million dollars] apiece
* **QUAN** (quantity): measurements with explicit standardized units<br>
  : Include the whole statement of quantity, but standalone numbers with implicit units of measurement are not marked.
  > [4 ounces]<br>
  > [4 miles]<br>
  > it was **[50 degrees]** yesterday, but today it is 35<br>
  > **[one hundred or so pounds]**<br>
  > **[30 or 40 miles]** inland
* **CARD** (cardinal): numbers that don't fall under measurments, money, date, or time<br>
  : Mark any standalone numbers, except when used in a referential sense
  > [thousands] of books<br>
  > it was 50 degrees yesterday, but today it is **[35]**<br>
  > that wasn't the **one** I wanted
* **EVENT**: named hurricanes, wars, sports events, and battles<br>
  > [2007 World Series]<br>
  > the [Oscars]<br>
  > [Hurricane Katrina]<br>
  > [9/11]
* **WOA** (work of art): titles of books, songs, television programs, awards<br>
  > the [Bible]<br>
  > her [Oscar] nomination<br>
  > [Toy Story]
* **LAW**: any document that has been made into law including treaties and legal documents<br>
  > the [Bill of Rights]<br>
  > [IRS code 4]<br>
  > the [1988 trade act]
* **LANG** (language): any named language<br>
  > [Catalan]<br>
  > [Xhosa]<br>
  > [Latin]


## Notes

* Determiners are not included unless part of the official name:
  > the [Supreme Court]
* If an entity can be classified into multiple tags, choose the most specific one:
  > [40 minutes] is `TIME` not `QUANTITY`
* General references are not annotated:
  > [his time in jail] is not annotated as `TIME`<br>
  > [the money he invested] is not annotated as `MONEY`
* Don't mark syntactic expletives:
  > [Jesus Christ] is not `PER` unless the actual person is being referred to