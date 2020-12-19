import pywikibot
from pywikibot import pagegenerators
family = "miraheze"
mylang = "wikiarchive"
usernames["miraheze"]["wikiarchive"] = "ArchiverBot"
site = "en.wikipedia.org"
cat = pywikibot.Category(site,'Category:All articles proposed for deletion')
gen = pagegenerators.CategorizedPageGenerator(cat)
for page in gen:
    site = "en.wikipedia.org"
    text = page.text
    site = "wikiarchive.miraheze.org"
    mtext = text
    page.save(u"Recovered from Wikipedia")
