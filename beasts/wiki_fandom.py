from bs4 import BeautifulSoup


def wiki_fandom_beast(html, url):
    soup = BeautifulSoup(html, 'html.parser')
    drop_tables = soup.find_all(class_='dtable')

    name = soup.find(class_='page-header__title').text
    rare_drop_table = soup.find(class_='rdtable') is not None

    drops = []

    for drop_table in drop_tables:
        for trs in drop_table:
            tds = trs.find_all('td')
            if tds == [] or tds is None:
                continue

            drop = {
                'name': tds[1].text.strip() if tds[1] else None,
                'quantity': tds[2].text.strip() if tds[2] else None,
                'rarity': tds[3].text.strip() if tds[3] else None,
                'rate': tds[3].text.split("(")[1][:-1].strip() if "(" in tds[3].text else None,
            }

            drops.append(drop)

    return {
        name: {
            'drops': drops,
            'rare_drop_table': rare_drop_table,
            'url': url
        }
    }
