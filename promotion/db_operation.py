"""奖品服务"""
import pymysql


class AwardService:
    mydb = None
    cursor = None

    def __init__(self):
        try:
            self.mydb = pymysql.connect(host='localhost',
                                        user='root',
                                        port=3306,
                                        password='root',
                                        database='big_market')
            self.cursor = self.mydb.cursor()
        except Exception as e:
            print(f"数据库连接失败: {e}")

    def get_all_tables(self):
        self.cursor.execute("SHOW TABLES")
        tables = [table[0] for table in self.cursor.fetchall()]
        return tables

    def get_award(self, award_id):
        self.cursor.execute("SELECT * FROM award WHERE award_id = %s", (award_id,))
        award = self.cursor.fetchone()
        return award

    def page_award(self, page_num, page_size):
        self.cursor.execute("SELECT * FROM award LIMIT %s, %s", (page_num, page_size))
        awards = self.cursor.fetchall()
        return awards

    def update_award(self, award):
        try:
            sql = "UPDATE award SET  award_desc = %s WHERE award_id = %s"
            self.cursor.execute(sql, (award.award_desc, award.award_id))
            self.mydb.commit()
        except Exception as e:
            print(f"数据库更新失败: {e}")
            self.cursor.rollback()

    def insert_award(self, award):
        try:
            sql = "INSERT INTO award (award_id, award_key, award_config, award_desc) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(sql, (award.name, award.type, award.description))
            self.mydb.commit()
        except Exception as e:
            print(f"数据库插入失败: {e}")
            self.cursor.rollback()


if __name__ == '__main__':
    try:
        award_service = AwardService()
        print(award_service.get_all_tables())
        print(award_service.get_award(101))
        print(award_service.page_award(0, 10))
    except Exception as e:
        print(f"数据库操作失败: {e}")
