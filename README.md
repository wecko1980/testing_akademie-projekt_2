# Testing akademie projekt 2
Ahoj, připravil jsem 3 automatizované testy s využitím knihovny pytest-playwright. Testuji na webu engeto.cz.
Ve všech 3 testech používám fixtury pro vytvoření vlastní instance prohlížeče a nové stránky. Probíhající test lze pak vidět v otevřeném okně browseru (headless=False a rozumně nastavený parametrem slow_mo). Jelikož má engeto.cz cookies lištu, tak v definici testovací funkce automaticky vybírám souhlas s nezbytnými cookies.  
  
## Test "test_odber_newsletter_engeto_cz.py"
Na webu engeto.cz testuje, zda se při zadání nevalidní e-amailové adresy do inputu pro odběr newsletteru zobrazí odpovídající chybová hláška.  

## Test

## Test
