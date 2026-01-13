from flask import Flask

# client_id = "ed9d618c-d308-4a82-8199-fe4f68e9c730"
# client_secret = "pi98Q~wlDsuM_ypqQ_2AzBZ82X5Qw-~RthtpEdd8"

app = Flask(__name__)
app.app.config.from_mapping(
  CLIENT_ID="ed9d618c-d308-4a82-8199-fe4f68e9c730",
  CLIENT_SECRET="pi98Q~wlDsuM_ypqQ_2AzBZ82X5Qw-~RthtpEdd8"
)
app.config.from_prefixed_end()

@app.route("/")
def index():
  return {"status": "ok"}
