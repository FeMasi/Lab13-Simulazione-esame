from database.DB_connect import DBConnect
from model.sighting import Sighting
from model.states import State
class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllSightings():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT * FROM sighting s ORDER BY `datetime` ASC"""
        cursor.execute(query)

        for row in cursor:
            result.append(Sighting(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllShapes():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT shape FROM sighting s WHERE shape != "" """
        cursor.execute(query)

        for row in cursor:
            result.append(row['shape'])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllStates():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT * FROM state s """
        cursor.execute(query)

        for row in cursor:
            result.append(State(row["id"], row["Name"], row["Capital"], row["Lat"], row["Lng"], row["Area"], row["Population"], row["Neighbors"]))
            #result.append(State(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllWeightedNeigh(a, s):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT n.state1, n.state2 , count(*) as N
                    FROM sighting s , neighbor n 
                    where year(s.`datetime`) = %s
                    and s.shape = %s
                    and (s.state = n.state1 or s.state = n.state2 )
                    and n.state1 < n.state2
                    group by n.state1 , n.state2 """

        cursor.execute(query, (a, s))

        for row in cursor:
            result.append((row['state1'], row['state2'], row["N"]))

        cursor.close()
        conn.close()
        return result