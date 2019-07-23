import psycopg2

class database:
    
    def creation_table_principale(self):
        """En gros on stock les verbe et les mots"""


        conn = psycopg2.connect(database='mot',
                                user='postgres',
                                host='127.0.0.1',
                                password='tiotiotio333')

        cursor = conn.cursor()
        
        cursor.execute("""create table boxx1(
                        id serial PRIMARY KEY,
                        mot varchar(100),
                        mot_fonction text,
                        verbe varchar(100),
                        verbe_fonction varchar(100),
                        phrase text);""")

        conn.commit()






    def creation_table_librarie(self):
        """en gros la faudra dire ouvrire image 1:ouverture lecture ect"""
        conn = psycopg2.connect(database='mot',
                                user='postgres',
                                host='127.0.0.1',
                                password='tiotiotio333')

        cursor = conn.cursor()
        
        cursor.execute("""create table librarie(
                        id serial PRIMARY KEY,
                        mot varchar(100),
                        librarie varchar(100));""")

        conn.commit()






















database = database()
database.creation_table_principale()
database.creation_table_librarie()
