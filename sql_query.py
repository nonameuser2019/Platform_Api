

sql_qet_all_categories = f"SELECT COUNT(category_guid) AS cnt\
                    FROM categories"


sql_get_categories_guid = f"SELECT category_guid FROM categories"

sql_get_categories_name = f"SELECT url, category_guid FROM categories"