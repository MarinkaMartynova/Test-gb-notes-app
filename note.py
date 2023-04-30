class Note(object):

    def __init__(self, note_id, date, title, body):
        self.note_id = note_id
        self.date = date
        self.title = title
        self.body = body

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, body):
        self._body = body

    @property
    def note_id(self):
        return self._note_id

    @note_id.setter
    def note_id(self, note_id):
        self._note_id = note_id

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    def __str__(self):
        return f'\nЗаметка: {self._note_id}\nДата создания(редактирования):' \
               f' {self._date}\nЗаголовок: {self._title}\nТело: {self._body}\n '