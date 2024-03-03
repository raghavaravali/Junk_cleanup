from flask import Flask, render_template,request
import os
import shutil
import platform

def cleanup(source_loc):
    lext=[".txt",".png",".exe",".jpeg",".gif",".mp4","html",".dll"]
    ldest=["txt/","png/","exee/","jpeg/","gif/","mp4/","html/","dll/"]


    for item in ldest:
        if not os.path.isdir('New_folder'):
            if not os.path.exists(source_loc+item):
                os.mkdir(source_loc+item)
    for lext, ldest in zip(lext,ldest):
        for file in os.listdir(source_loc):
            filename = os.fsdecode(file)
            if filename.endswith(lext):
                shutil.move(source_loc+filename, source_loc + ldest)
                continue


app=Flask(__name__)

@app.route('/')
def form():
    if platform.system() == "Windows":
        return render_template('index_win.html')
    if platform.system() == "Linux":
        return render_template('index_linux.html')

@app.route('/data/',methods=['POST','GET'])
def data():
    if request.method =='GET':
        return f"The URL /data is accessed directly. Try going to '/' submit form"

    if request.method =='POST':
        if request.form != "":
            source_location=request.form.get("location")
            new_source_location = source_location + "/"
            cleanup(new_source_location)
            return f"cleaning done"




        


        
        
        
        
app.run(debug =True)


