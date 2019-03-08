#MVC Controller
import web
from Models import RegisterModel, LoginModel, PostsModel
urls = ('/', 'Home', 
'/register', 'Register', 
'/registration', 'Registration', 
'/login', 'Login', 
'/logout', 'Logout',
'/login/check', 'CheckLogin',
'/postactivity', 'PostActivity',
'/profile/(.*)/info', 'ProfileInfo',
'/profile/(.*)', 'Profile',
'/settings/update', 'SettingsUpdate',
'/settings', 'Settings')

web.config.debug = False
app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={'user': None})
session_data = session._initializer
render = web.template.render("Views/Templates", base="Layout", globals={'session': session_data, 'currentUser': session_data["user"]})

# Classes/Routes
class Home:
    def GET(self):
        if session_data['user'] != None:
            id = session_data['user']['_id']
            posts_model = PostsModel.PostsModel()
            posts = posts_model.get_posts(id)
            return render.Home(posts)
        else:
            return render.Home([])


class Register:
    def GET(self):
        return render.Register()

class Registration:
    def POST(self):
        data = web.input() 
        reg_model = RegisterModel.RegisterModel(data)
        return data.username

class Login:
    def GET(self):
        return render.Login()

class Logout:
    def GET(self):
        session['user'] = None
        session_data['user'] = None
        session.kill()
        return "success"

class CheckLogin:
    def POST(self):
        data = web.input()
        login_model = LoginModel.LoginModel()
        response = login_model.check_user(data)
        if response != "error":
            session_data['user'] = response
        return response

class PostActivity:
    def POST(self):
        data = web.input()
        userid = session_data['user']['_id']
        print(userid)
        data['user_id'] = userid
        posts_model = PostsModel.PostsModel(data)
        return "success"

class UserProfile:
    def GET(self, username):
        if username == session_data['user']['username']:
            user_id = session_data['user']['_id']
            posts_model = PostsModel.PostsModel()
            posts = posts_model.get_posts(user_id)
            return render.Profile(posts)

class UserInfo:
    def GET(self):
        user_id = session_data['user']['_id']
        info_model = InfoModel.InfoModel()
        info = posts_model.get_info(user_id)
        return render.ProfileInfo(info)

class Settings:
    def GET(self):
        return render.Settings()
   
class SettingsUpdate:
    def Post(self):
        data = web.input()
        userid = session_data['user']['_id']
        data['user_id'] = userid
        info_model = InfoModel.infoModel()
        if info_model.insert_info(data):
            return "success"
        else: 
            return "error has occured"
   
if __name__ == "__main__":
    app.run()