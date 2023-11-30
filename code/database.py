import mysql.connector

conn = mysql.connector.connect(host='localhost',
                               database='xcareers',
                               user='root',
                               password='1234')
cursorObject = conn.cursor()
def load_job_data():
    query = "SELECT id,title, location, about, salary, created_at  FROM jobs ORDER BY created_at DESC LIMIT 5 "
    cursorObject.execute(query)
    myresult = cursorObject.fetchall()
    return myresult

def load_job_data_db(id):
    query = "SELECT *  FROM jobs WHERE id ='"+str(id)+"';"
    cursorObject.execute(query)
    myresult = cursorObject.fetchall()
    return myresult

def search_job_data_db(search_data):
    query = "SELECT id,title, location, about, salary, created_at FROM jobs WHERE MATCH(title, location, about, requirements, responsibilities) AGAINST('"+str(search_data)+"');"
    cursorObject.execute(query)
    myresult = cursorObject.fetchall()
    return myresult
def store_application_in_db(name,email,lkin,leetc,eduDet,workExp,job_id):
    query="INSERT INTO applications (applier_name,applier_email,applier_linkedin_url,applier_leetcode_url,applier_education_detail,applier_work_experience,job_application_id) VALUES ('" + str(name) + "','" + str(email) + "','" + str(lkin) + "','" + str(leetc) + "','" + str(eduDet) + "','" + str(workExp) + "'," + str(job_id) + ");"
    cursorObject.execute(query)
    cursorObject.fetchall()
# query = "SELECT requirements FROM jobs LIMIT 5"
# cursorObject.execute(query)
#
# myresult = cursorObject.fetchall()

# print(myresult)
