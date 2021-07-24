# lista najnowszych ebooków z działu 'historia' księgarni ebookpoint.pl:
# lp, autor, tytuł, cena
import requests
import bs4


# funkcja pobiera stronę o adresie wskazanym przez parametr address
def get_html(address):
    try:
        res = requests.get(address)
        res.raise_for_status()
        return res.text
    except Exception as exc:
        print(f'The following problem has occurred:\n {exc}')


# główna część skryptu
if __name__ == "__main__":
    history_latest = "https://ebookpoint.pl/kategorie/historia?select=1&sort=2&formaty=&ceny=&wydawca=&jezyk="
    html = get_html(history_latest)

    historySoup = bs4.BeautifulSoup(html, "html.parser")
    books = historySoup.find_all("div", class_="book-info")

    number = 0
    for book in books:
        number += 1
        title = book.find("a", class_="full-title-tooltip")
        author = book.find("p", class_="author")
        price_par = book.findNext("p", class_=["price", "price-incart"])
        price = price_par.find("span")
        print(
            f'{number}. {author.text.strip()}, "{title.text.strip()}", {price.text.strip()}')
