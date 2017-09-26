from flask import Flask, render_template
app = Flask(__name__)

#assign following fxn to run when
#root route requested
@app.route("/")
def hello_world():
    return "No hablo queso!"

coll = [0,1,1,2,3,5,8]

@app.route("/first_template")
def test_templt():
    return render_template( 'first_template.html', foo = "fooo", collection = coll )

if __name__ == "__main__":
    app.debug = True
    app.run()
