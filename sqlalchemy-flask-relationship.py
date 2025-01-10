from flask import request
from sqlalchemy.orm import relationship

app = Flask(__name__)


@app.route("/t/01")
def t1() -> None:
    from .models import Child
    from .models import Parent

    tainted = request.args.get("param")

    # ruleid: sqlalchemy-flask-relationship
    Parent.children = relationship(Child, primaryjoin=f"Parent.id == {tainted}")

    # ruleid: sqlalchemy-flask-relationship
    Parent.children = relationship(Child, foreign_keys=f"Parent.id == {tainted}")
