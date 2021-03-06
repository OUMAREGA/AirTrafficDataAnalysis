import os
from modules.util.tables import TABLES
from modules.util.parser import parse_csv 
import pymysql as db
from sqlalchemy import create_engine
from dotenv import load_dotenv
from os.path import dirname, join

racine = dirname(dirname(__file__))

class Connection:
   
    def __init__(self):

        load_dotenv(".env")
        self.host = os.environ.get("DB_HOST")
        self.database= os.environ.get("DB_NAME")
        self.port = int(os.environ.get("DB_PORT"))
        self.user = os.environ.get("DB_USER")
        self.password = os.environ.get("DB_PWD")
        self.db = self.connection()
        self.cursor = self.db.cursor()
    
    def query(self,query: str,multiple=True):
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall() if multiple is True else self.cursor.fetchone()
            return result
        except Exception as e:
            print(e)

    def connection(self):
        """
            Méthode retournant l'objet MySQLConnection
            afin de pouvoir manipuler la base de données
            MariaDB/MySQL
        """
        connection = db.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
            cursorclass=db.cursors.DictCursor
        )

        return connection


    def create(self,table_name:str):
        """
            Méthode permettant de créer une table SQL
            en s'appuyant sur le dictionnaire tables dans util

            Parameters
            ----------
                table_name (str) : nom de la table
        """
        if table_name in TABLES:
            columns = ""
            total_columns = len(TABLES[table_name]["columns"])
            for index,column in enumerate(TABLES[table_name]["columns"]):
                column_dict: dict = column
                column_name = column["name"]
                column_data = column_dict["structure"]
                columns = columns + column_name + " " + column_data["type"] + ("("+column_data["length"]+") " if "length" in column_data else " ")
                if "options" in column_data:
                    columns = columns + (" ".join(column_data["options"]))
                if total_columns != index + 1: #si ce n'est pas la dernière colonne, on ajoute une virgule à la requête CREATE TABLE
                    columns = columns + ","
            if "constraints" in TABLES[table_name]:
                columns = columns + "," + ",".join(TABLES[table_name]["constraints"])
            query = f"CREATE TABLE IF NOT EXISTS {table_name}({columns})"
            print(query)
            self.cursor.execute(query)
           
        else:
            raise Exception("Table à créer non répertoriée")


    def load_csv_data(self,table_name:str,csv_path:str):
        """
            Méthode permettant de charger des données
            CSV dans une table

            Parameters
            ----------
                table_name (str) : nom de la table qui doit recevoir les données
                csv_file (str) : nom du fichier CSV
        """

        sqlEngine = create_engine('mysql+pymysql://'+os.environ.get("DB_USER")+':'+os.environ.get("DB_PWD")+'@'+
            os.environ.get("DB_HOST")+':'+os.environ.get("DB_PORT")+'/'+os.environ.get('DB_NAME'))
        
        dbConnection = sqlEngine.connect()

        dataframe = parse_csv(dbConnection,table_name,csv_path)
        dataframe.to_sql(table_name,con=sqlEngine,if_exists='append',index=False)

        

