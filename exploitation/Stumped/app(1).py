from flask import Flask, render_template, request, flash, redirect, current_app
from werkzeug.utils import secure_filename
from tempfile import mkdtemp, mkstemp
from os import path, remove, system
import tarfile
import os

app = Flask(__name__)

app.secret_key = os.urandom(32)

app_path = "/opt/app/"


@app.route("/")
def tree():
    return render_template("tree.html")


@app.route("/show_tree", methods=["GET", "POST"])
def show_tree():
    if request.method == "POST":
        if "file" not in request.files:
            return "error: file upload failed."
        submission = request.files["file"]
        if submission.filename == "":
            return "error: did not receive file"
        # get a temporary directory for the submission
        tmp_dir = mkdtemp(dir=app_path + "trees")
        # get a temporary file for the html
        _, html_out = mkstemp(dir=app_path + "static/tree_html", suffix=".html")
        # save the submission to the temporary directory
        secure_path = path.join(tmp_dir, secure_filename(submission.filename))
        submission.save(secure_path)
        # try to extract the submission
        try:
            archive = tarfile.open(secure_path)
            archive.extractall(path=tmp_dir)
            archive.close()
        except tarfile.ReadError:
            return "error: could not open tar file"
        # remove the archive
        remove(secure_path)
        # call tree on the extracted archive
        system(
            f"cd {tmp_dir} && tree -R -L 3 -H . --nolinks -o {html_out} && rm -rf {tmp_dir}"
        )
        return current_app.send_static_file(f"tree_html/{path.basename(html_out)}")
