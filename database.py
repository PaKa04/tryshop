import psycopg2


class Market:

    def __init__(self):
        self.c = psycopg2.connect(
            host='localhost',
            dbname='name',
            user='postgres',
            password='password',
            port=5432
        )
        self.cursor = self.c.cursor()

    def registration(self, sid, name, surname, login):
        with self.c:
            self.cursor.execute("INSERT INTO users (name, surname, tg_id, login) VALUES (%s, %s, %s, %s)", (name, surname, sid, login,))

    def inbucket(self, sid, product):
        with self.c:
            self.cursor.execute("INSERT INTO bucket (id, product) VALUES (%s, %s)", (sid, product))

    def showbucket(self, sid):
        with self.c:
            # self.cursor.execute("SELECT * FROM bucket WHERE id=(%s)", (sid))
            self.cursor.execute("SELECT bucket.id, bucket.product, tovar.price FROM tovar "
                                "JOIN bucket ON tovar.product=bucket.product "
                                "WHERE id=(%s)", [sid])
            dick = self.cursor.fetchall()
            dicks = 'Корзина:\n'
            summ = 0
            for complex in dick:
                ftgid = complex[0]
                fproduct = complex[1]
                fprice = complex[2]
                cum = f'{fproduct}: {fprice}BYN\n'
                dicks += cum
                summ += fprice
            return f'{dicks}\n Общая сумма товаров в корзине: {summ} BYN'

    def clear_bucket(self, sid):
        with self.c:
            self.cursor.execute("DELETE FROM bucket WHERE id=(%s)", [sid])

    def zakaz(self, sid):
        with self.c:
            self.cursor.execute("SELECT login FROM users WHERE tg_id=(%s)", [sid])
            cool = self.cursor.fetchone()
            return cool[0]
