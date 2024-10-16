from neo4j import GraphDatabase
import logging

logger = logging.getLogger(__name__)

class Neo4jDriver:
    def __init__(self, uri, user, password, db_name):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        self.db_name = db_name  # Lưu db_name là thuộc tính của lớp

    def execute_query(self, query, parameters=None):
        with self.driver.session(database=self.db_name) as session:
            try:
                result = session.run(query, parameters)
                if result.peek() is None:  # Kiểm tra nếu không có bản ghi nào
                    logger.error(f"Query returned no results: {query}, parameters: {parameters}")
                    return None
                return result.data()  # Trả về danh sách các bản ghi
            except Exception as e:
                logger.error(f"Error executing query: {str(e)}")
                return None

    def close(self):
        self.driver.close()
        logger.info("Neo4j driver closed")
