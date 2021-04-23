# import MySQLdb
#
#
# def test_pymysql():
#     conn=MySQLdb.connect(
#         host='localhost',
#         port=3306,
#         user='root',
#         db='mysql'
#     )
#
#     cur=conn.cursor()
#     cur.execute('''
#     CREATE TABLE price(
#     timestamp TIMESTAMP NOT NULL,
#     BTCUSD FLOAT(8,2),
#     PRIMARY KEY(timestamp)
#     );
#     ''')
#
#     cur.execute('''
#     INSERT INTO price VALUES(
#     '2021-04-19 16:37:02',
#     11980.15);
#     ''')
#
#
#     conn.commit()
#     conn.close()
#
# test_pymysql()
import peewee
from peewee import MySQLDatabase

db = MySQLDatabase('mysql', user='root')


class Price2(peewee.Model):
    timestamp = peewee.DateTimeField(primary_key=True)
    BTCUSD = peewee.FloatField()

    class Meta:
        database = db


class Person(peewee.Model):
    id_cert = peewee.CharField()
    name = peewee.CharField()
    is_relative = peewee.BooleanField()

    class Meta:
        database = db


def test_peewee():
    db.create_tables([Price2, Person])
    price = Price2(timestamp='2021-04-19 16:48:19', BTCUSD='12345.67')
    price.save()
    # Person.create_table()
    person = Person(id_cert='1234', name='lilin', is_relative=True)
    person.save()


# person1 = Person(id_cert='0987', name='changlili', is_relative=True)
# person1.save()

test_peewee()
# price = Price2(timestamp='2021-04-19 16:48:19', BTCUSD='12345.67')
# price.save()


def last_test_pymysql():
    conn=MySQLDatabase.connect(
        host='localhost',
        port=3306,
        user='root',
        db='mysql'
    )
