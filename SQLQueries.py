from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy import text


def getSampleDataFrame(engine, table,col):
    try:
        with engine.connect() as conn:
                return conn.execute(text("""SELECT  """ +  col + """ FROM [""" + table + "] WHERE " + col + "IS NOT NULL")).fetchone()
    except:
        with open('LOG.txt', 'a', encoding='utf-8', errors='ignore') as f:
            f.write("""ERROR : SELECT  """ +  col + """ FROM [""" + table + "] WHERE " + col + "IS NOT NULL\n")
        return """ERROR : SELECT  """ +  col + """ FROM [""" + table + "] WHERE " + col + "IS NOT NULL"



def getDatabases(engine):
    dbList = []
    with engine.connect() as conn:
        result = conn.execute(text(
            """
           SELECT NAME
           FROM   SYS.DATABASES
           WHERE  STATE = 0 --Database is online
                """))
        for record in result:
            dbList.append(record[0])
    return dbList


def getCode(engine):
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT sch.NAME        AS [Schema],
                   obj.NAME        AS [Stored Procedure],
                   code.DEFINITION AS [Code]
            FROM   SYS.OBJECTS     AS obj
            JOIN    SYS.SQL_MODULES AS code
            ON     code.OBJECT_ID = obj.OBJECT_ID
            JOIN   SYS.SCHEMAS     AS sch
            ON     sch.SCHEMA_ID = obj.SCHEMA_ID
            WHERE  obj.TYPE = 'P'
        """))
    for record in result:
        with open(db + 'SP.sql', 'a', encoding='utf-8', errors='ignore') as f:
            f.write(record[2])


def getColumnsCSV(engine, fname):
    with open(fname + ".txt", 'a', encoding='utf-8', errors='ignore') as f:
        with engine.connect() as conn:
            result = conn.execute(text(
                """
            SELECT   TABLE_CATALOG,
                    TABLE_NAME,
                    COLUMN_NAME,
                    DATA_TYPE,
                    CHARACTER_MAXIMUM_LENGTH
            FROM     INFORMATION_SCHEMA.COLUMNS;
            """)).all()
        recordTable = {}
        for record in result:
            for subRecord in record:
                f.write(str(subRecord))
            f.write('\n')


def getColumns(engine):
    with open('MASTERCOLUMNSCSV.txt', 'a', encoding='utf-8', errors='ignore') as f:
        with engine.connect() as conn:
            result = conn.execute(text(
                """
            SELECT   TABLE_CATALOG,
                    TABLE_NAME,
                    COLUMN_NAME,
                    DATA_TYPE,
                    CHARACTER_MAXIMUM_LENGTH
            FROM     INFORMATION_SCHEMA.COLUMNS;
            """)).all()
            return result


def getColumnCount(engine):
    sum = 0
    with open('MASTERCOLUMNSCSV.txt', 'a', encoding='utf-8', errors='ignore') as f, engine.connect() as conn:
        result = conn.execute(text(
            """
            SELECT   TABLE_CATALOG,
                    TABLE_NAME,
                    COLUMN_NAME,
                    DATA_TYPE,
                    CHARACTER_MAXIMUM_LENGTH
            FROM     INFORMATION_SCHEMA.COLUMNS;
            """)).all()
        for record in result:
            sum += 1
        print(sum)
        return sum


def getTables(engine):
    with engine.connect() as conn:
       return  conn.execute(text(
            """
             SELECT   TABLE_CATALOG,
                    TABLE_NAME
            FROM     INFORMATION_SCHEMA.TABLES
            """)).all()

