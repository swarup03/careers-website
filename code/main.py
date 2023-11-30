from flask import Flask, render_template,request
from database import load_job_data,load_job_data_db,search_job_data_db,store_application_in_db
# app = Flask(__name__)
app = Flask(__name__, static_folder="static")


@app.route("/")
def home():
    JOBS = load_job_data()
    return render_template("index.html",jobs = JOBS,home='active')

@app.route("/about")
def about():
    return render_template("about.html",about='active')

@app.route("/job/<id>")
def jobs(id):
    job = load_job_data_db(id)
    if not job:
        return render_template("error.html")
    return render_template("job_details.html",job=job)

@app.route("/job/<id>/apply",methods=["GET","POST"])
def jobs_application(id):
    if request.method == "POST":
        applier_name = request.form.get("applier_name")
        applier_email = request.form.get("applier_email")
        applier_linkedin_url = request.form.get("applier_linkedin_url")
        applier_leetcode_url = request.form.get("applier_leetcode_url")
        applier_education_detail = request.form.get("applier_education_detail")
        applier_work_experiencl = request.form.get("applier_work_experiencl")
        store_application_in_db(applier_name, applier_email, applier_linkedin_url, applier_leetcode_url, applier_education_detail, applier_work_experiencl,id)
        return render_template("application_success.html", applier_name=applier_name, applier_email=applier_email,
                               applier_linkedin_url=applier_linkedin_url, applier_leetcode_url=applier_leetcode_url,
                               applier_education_detail=applier_education_detail,
                               applier_work_experiencl=applier_work_experiencl)
    else:
        return render_template("error.html")

@app.route("/search",methods=["GET","POST"])
def search():
    if request.method == "POST":
        search_text = request.form.get("search")
        search_result = search_job_data_db(search_text)
        return render_template("searchresult.html",search_result =search_result, search_text=search_text)
    else:
        return render_template("error.html")

app.run(debug=True)
