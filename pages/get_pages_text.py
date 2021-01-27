from config import headers
from loader import session


class Get_Pages_TEXT:
    def __init__(self, link):
        self.link = link

    async def chek_link(self):
        code = session.get(url=self.link, headers=headers)
        print(code.text)
