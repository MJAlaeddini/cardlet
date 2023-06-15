# cardlet

## O projektu
Projekt Cardlet představuje open-source verzi projektů kartičkových didaktických softwarů typu Quizlet. Cílem je poskytnout jednoduchou webovou aplikaci, do které si učitel nahraje v TOML formátu otáčecí kartičky a během hodiny s nimi didakticky pracuje. Aplikace je jedna z chystaných aplikací, které budou volně dostupné na serveru přírodovědecké fakulty UJEP pro učitele. 

Projekt vzniká z iniciativy zaměstnance katedry informatiky Pavla Beránka, kterému se nelíbí komercializace didaktických online aplikací, které byly dlouhou dobu zdarma, byly pro ně vytvářené školení a nově jsou zpoplatněné. Projekt je vyvíjen dobrovolníky a studenty kurzů z Bee IT a UJEP. Jedná se o jeden z projektů, který díky své jednoduchosti, slouží pro nácvik procesu vývoje softwaru.

## Technologický zásobník
Pro projekt byla zvolen mikro pracovní rámec Flask v jazyce Python jako hlavní programovací jazyk na straně serveru. Stylovací pracovní rámec bude Bootstrap 5 a potřebné interakce budou řešené jednoduchým Javascriptem. V případě vzniku složitějších požadavků bude použit pracovní rámec React.

## Stav projektu (15.6.2023)
Aktuálně je stav projektu v úplných začátcích, chybí design, architektura, programátoři. Zkrátka vše. Výsledný produkt se bude inspirovat aplikací knowt.io, která ovšem není optimalizovaná pro využití do výuky (full-screen nevede na karty přes celý displej aj.).

Každá karta má svou odkrytou stranu, kterou mají studenti před očima.
<img src="nápady/knowt_obrázky/odkrytá_strana_karty.png">

Při kliku nebo zmáčknutí dedikované klávesy se karta obrátí a ukáže svou skrytou stranu (typicky odpověď na otázku z odkryté strany).
<img src="nápady/knowt_obrázky/skrytá_strana_karty.png">

Software musí poskytovat editor sady karet.
<img src="nápady/knowt_obrázky/editor_sady_karet.png">

Prozatimní verze nebude předpokládat ukládání dat na stranu serveru, takže musí jít sada vytvořených karet uložit do snadno přenositelného souboru, který lze kdykoliv nahrát zpět. Zvoleným formátem bude TOML díky jeho snadné integraci do jazyka Python.


