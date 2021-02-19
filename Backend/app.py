import os
from flask import Flask
from flask_cors import CORS
from flask_restful import Resource ,Api

from flask import request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
api = Api(app)
app.config['SECRET_KEY']='mysecretkey'


##################################################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']        = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#################################
class Meme(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fullName = db.Column(db.Text)
    caption = db.Column(db.Text)
    url = db.Column(db.Text)


    def __init__(self,fullName,caption,url):
        self.fullName=fullName
        self.caption = caption
        self.url = url

    def json(self):
        return {
            'id':self.id,
            'name':self.fullName,
            'url':self.url,
            'caption':self.caption
        }
    def json_id(self):
        return{
            'id':self.id
        }
##################################

class GetMemes(Resource):
    def get(self):
        memes = Meme.query.all()

        if memes:
            return [meme.json() for meme in memes]
        else:
            return {'name':None},404
class Specific(Resource):
    def get(self,id):
        meme = Meme.query.get(id)

        if meme:
            return meme.json()
        else:
            return {'name':None},404
class AddMeme(Resource):
    def post(self):
        data = request.get_json()
        name = data['name']
        caption = data['caption']
        url = data['url']
        meme = Meme(fullName=name,caption=caption,url=url)
        db.session.add(meme)
        db.session.commit()
        return meme.json_id()
class UpdateMeme(Resource):
    def patch(self,id):
        updated_meme = Meme.query.get(id)
        data = request.get_json()
        arr = []
        for i in data:
            arr.append([i,data[i]])
        ans = []
        new_caption = ''
        new_url = ''
        if updated_meme:
            for i in arr:
                if i[0]=='caption':
                    new_caption=i[1]
                if i[0]=='url':
                    new_url = i[1]
            if new_caption != '':
                updated_meme.caption = new_caption
            if new_url !='' :
                updated_meme.url = new_url
            db.session.commit()

        else:
            return {'name':None},404

class DeleteMeme(Resource):
    def delete(self,id):
        meme = Meme.query.get(id)
        if meme:
            db.session.delete(meme)
            db.session.commit()
            return  {'note':'delete sucess'}
        return {'name':None},404


api.add_resource(AddMeme,'/memes')
api.add_resource(Specific,'/memes/<int:id>')
api.add_resource(UpdateMeme,'/memes/<int:id>')
api.add_resource(DeleteMeme,'/memes/delete/<int:id>')
api.add_resource(GetMemes,'/memes')


if __name__=='__main__':
    app.run(host="localhost", port=8081)
