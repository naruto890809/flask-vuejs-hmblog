from app import creat_app,db
from app.models import User

app = creat_app()

@app.shell_context_processor
def make_shell_context():
    return{'db':db,'User':User}
