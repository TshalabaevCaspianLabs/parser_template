from config import link
from loader import asinc
from pages import Get_Pages_TEXT

pages = Get_Pages_TEXT(link)
for _ in range(8):
    asinc.run(pages.chek_link())
