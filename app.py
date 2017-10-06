import io
import flask
import random
import string
import pickle
import qrcode
from PIL import Image

app = flask.Flask(__name__)

try:
	with open("tokens.db", "rb") as f:
		tokens = pickle.load(f)
except:
	tokens = set()

@app.route("/qr.png", methods=["GET"])
def get_qr():
	# publish new token
	token = "".join([random.choice(string.ascii_letters + string.digits) for i in range(32)])
	tokens.add(token)
	
	# save token database
	with open("tokens.db", "wb") as f:
		pickle.dump(tokens, f)
	
	# generate QR code
	raw = qrcode.make(f"https://ctf-no.pro/show/{token}")
	
	# create transparent QR image
	img = Image.new("RGBA", raw.size, color=(0, 0, 0, 0))
	for y in range(raw.size[1]):
		for x in range(raw.size[0]):
			if raw.getpixel((x, y)) == 0:
				img.putpixel((x, y), (0, 0, 0, 255))
	
	# get byte image
	imgbuf = io.BytesIO()
	img.save(imgbuf, format="png")
	imgbuf.seek(0)
	
	# send image
	return flask.send_file(imgbuf, mimetype="image/png")

@app.route("/show/<token>", methods=["GET"])
def show(token):
	if token not in tokens:
		return flask.render_template("closed.html")
	
	tokens.remove(token)
	return flask.render_template("paper.html")

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8000, debug=False)
