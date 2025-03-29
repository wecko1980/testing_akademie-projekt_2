# Testing akademie projekt 2
Ahoj, připravil jsem **3 automatizované testy s využitím knihovny pytest-playwright**. Testuji na webu **engeto.cz.**
Ve všech 3 testech používám fixturu pro vytvoření vlastní instance prohlížeče(postupně Chromium, Firefox, Webkit(Safari)) a fixturu pro vytvoření nové stránky. Probíhající test lze pak vidět v otevřeném okně browseru (headless=False a rozumně nastavený parametrem slow_mo). Jelikož má engeto.cz cookies lištu, tak v definici testovací funkce automaticky vybírám souhlas s nezbytnými cookies.  
  
## 1. Test: "test_odber_newsletter_engeto_cz.py"
Testuje, zda se při zadání nevalidní e-amailové adresy do inputu pro odběr newsletteru zobrazí odpovídající chybová hláška.  

## 2. Test: "test_hover_menu_drop_down.py"
Zde testuji, zda se po najetí myší (hover) na položku "Kurzy" v horním menu zobrazí drop down podmenu.

## Test
