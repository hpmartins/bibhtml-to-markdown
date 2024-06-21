from bs4 import BeautifulSoup, SoupStrainer
import markdown

with open("input.html", "r", encoding="utf-8") as input_file:
    contents = " ".join(input_file.readlines())

only_csl_entries = SoupStrainer("div", class_="csl-entry")
soup = BeautifulSoup(contents, "html.parser", parse_only=only_csl_entries)

MY_NAMES = ["H. P. Martins", "H. Martins"]

md_items = ''
for div in soup.find_all("div"):
    for link in div.find_all("a"):
        link = link.unwrap()

    item = "".join([str(x) for x in div.contents]) + "\n\n"
    item = item.replace("“", '"').replace("”", '"').replace('"*,', ',"*')

    # Custom: highlighting my name
    for name in MY_NAMES:
        item = item.replace(name, f'<u>{name}</u>')

    md_items = md_items + item

with open("output.md", "w", encoding="utf-8") as output_md:
    output_md.write(md_items)

with open("output.html", "w", encoding="utf-8") as output_html:
    output_html.write(markdown.markdown(md_items))