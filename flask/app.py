from flask import Flask, render_template,request
import os
import shutil

def cleanup(source_loc):
    list_dest_ext=["txt/","png/"]

    for item in list_dest_ext:
        if not os.path.isdir('New_folder'):
            if not os.path.exists(source_loc+item):
                os.mkdir(source_loc+item)

    for file in os.listdir(source_loc):
        filename = os.fsdecode(file)
        if filename.endswith(".png"):
            shutil.move(source_loc+filename, source_loc + "png/" + filename)
            continue

app=Flask(__name__)

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/data/',methods=['POST','GET'])
def data():
    if request.method =='GET':
        return f"The URL /data is accessed directly. Try going to '/' submit form"
    if request.method =='POST':
        form_data = request.form
        source_location=request.form.get("location")
        cleanup(source_location)
        return f"cleaning done"
app.run(debug =True)


