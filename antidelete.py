import pywikibot
from pywikibot import pagegenerators
from pywikibot import family
class Family(family.Family):
    name = 'miraheze'
    langs = {
        'wikiarchive': 'wikiarchive.miraheze.org',
    }
site = pywikibot.Site('en', 'wikipedia')
cat = pywikibot.Category(site,'Category:All articles proposed for deletion')
gen = pagegenerators.CategorizedPageGenerator(cat)
for page in gen:
    site = pywikibot.Site('en', 'wikipedia')
    text = page.text
    site = pywikibot.Site('wikiarchive', 'miraheze')
    p = pywikibot.Page(site, page)
    p.text = text
    p.save('Recovered from Wikipedia')
