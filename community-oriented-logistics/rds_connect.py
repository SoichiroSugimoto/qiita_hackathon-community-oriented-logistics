import boto3
import os

# RDS接続情報
rds_host = os.environ['RDS-HOST-ENDPOINT']
rds_port = 3306
rds_database = os.environ['DATABASE_NAME']
rds_username = os.environ['USERNAME']
rds_password = os.environ['PASSWORD']

# boto3クライアント
client = boto3.client('lambda')

def create_item(name, age):
    """
    RDSにデータを追加する
    """
    try:
        # RDS接続
        with connect_to_rds() as conn:
            # カーソル取得
            cursor = conn.cursor()

            # INSERT文
            sql = "INSERT INTO your_table (name, age) VALUES (%s, %s)"

            # パラメータ
            params = (name, age)

            # 実行
            cursor.execute(sql, params)

            # コミット
            conn.commit()
    except Exception as e:
        print(f"Create Error: {e}")

def read_item(name):
    """
    RDSからデータを取得する
    """
    try:
        # RDS接続
        with connect_to_rds() as conn:
            # カーソル取得
            cursor = conn.cursor()

            # SELECT文
            sql = "SELECT * FROM your_table WHERE name = %s"

            # パラメータ
            params = (name,)

            # 実行
            cursor.execute(sql, params)

            # 結果取得
            for row in cursor.fetchall():
                print(f"Name: {row[0]}")
                print(f"Age: {row[1]}")
    except Exception as e:
        print(f"Read Error: {e}")

def update_item(name, age):
    """
    RDSのデータを更新する
    """
    try:
        # RDS接続
        with connect_to_rds() as conn:
            # カーソル取得
            cursor = conn.cursor()

            # UPDATE文
            sql = "UPDATE your_table SET age = %s WHERE name = %s"

            # パラメータ
            params = (age, name)

            # 実行
            cursor.execute(sql, params)

            # コミット
            conn.commit()
    except Exception as e:
        print(f"Update Error: {e}")

def delete_item(name):
    """
    RDSからデータを削除する
    """
    try:
        # RDS接続
        with connect_to_rds() as conn:
            # カーソル取得
            cursor = conn.cursor()

            # DELETE文
            sql = "DELETE FROM your_table WHERE name = %s"

            # パラメータ
            params = (name,)

            # 実行
            cursor.execute(sql, params)

            # コミット
            conn.commit()
    except Exception as e:
        print(f"Delete Error: {e}")

def connect_to_rds():
    """
    RDSに接続する
    """
    try:
        return connect(
            host=rds_host,
            port=rds_port,
            database=rds_database,
            user=rds_username,
            password=rds_password,
        )
    except Exception as e:
        print(f"RDS Connect Error: {e}")
