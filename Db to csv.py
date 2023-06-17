import sqlite3
import csv

def sql_to_csv(db_filename, table, csvname):
    conn = sqlite3.connect(db_filename)             #connection object
    cursor = conn.cursor()                          #cursor object
    cursor.description                              #tuple, ('company', None, None)
    cursor.execute(f'SELECT * FROM {table}')        #str, 'SELECT * FROM {table}'

    headers = []                                    #list, []
    for header in cursor.description:               #tuples, ('company', None, None)
        headers.append(header[0])

    wfh = open(csvname, 'w', newline='')            #'file' object
    writer = csv.writer(wfh)                        #csv.writer object
    writer.writerow(headers)                        #int (bytes written)

    for row in cursor:                              #tuple, ('Haddad's',PA,239.5)
        writer.writerow(row)                        #int (bytes written)

    wfh.close()


db_name = 'session_2.db'                            #str, 'session_2.db'
table_name = 'revenue'                              #str, 'revenue'
csv_filename = 'revenue_from_db.csv'                #str, 'revenue_from_db.csv'
sql_to_csv(db_name, table_name, csv_filename)








