from app import create_app
from dotenv import load_dotenv
from app.db import prisma
from marshmallow import Schema, fields

load_dotenv()
app = create_app()


@app.before_request
def connect_db():
    prisma.connect()


@app.teardown_appcontext
def disconnect_db(exception):
    prisma.disconnect()


@app.route("/users", methods=["GET"])
def home():
    users = prisma.user.find_many()

    # serialize users to JSON
    """
    model User {
        id        Int          @id @default(autoincrement())
        username  String       @unique
        email     String       @unique
        password  String
        games     GamePlayer[]
        createdAt DateTime     @default(now())
    }
    """

    class UserSchema(Schema):
        id = fields.Int()
        username = fields.Str()
        email = fields.Str()
        createdAt = fields.DateTime()

    user_schema = UserSchema(
        many=True
    )  # many=True because we are serializing a list of users; many=False would be used for a single user
    return user_schema.dump(
        users
    )  # dump() is used to serialize the users to JSON; load() would be used to deserialize JSON to a Python object


if __name__ == "__main__":
    app.run(debug=True)
