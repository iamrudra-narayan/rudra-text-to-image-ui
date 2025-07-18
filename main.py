from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_BASE = "https://rudra-text-to-image.onrender.com"

ASPECT_RATIOS = {
    "16:9": {"width": 1344, "height": 768},
    "9:16": {"width": 768, "height": 1344},
    "1:1": {"width": 1024, "height": 1024},
    "4:3": {"width": 1280, "height": 960},
    "3:4": {"width": 960, "height": 1280},
    "2:3": {"width": 1024, "height": 1536},
    "3:2": {"width": 1536, "height": 1024},
    "21:9": {"width": 1440, "height": 600},
    "9:21": {"width": 600, "height": 1440}
}

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", aspect_ratios=ASPECT_RATIOS.keys())

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt")
    token = data.get("token")
    seed_enabled = data.get("use_seed", False)
    seed_value = int(data.get("seed") or 9896923949) if seed_enabled else 9896923949

    aspect_ratio = data.get("aspect_ratio", "1:1")
    batch_size = int(data.get("batch_size") or 1)
    resolution = ASPECT_RATIOS.get(aspect_ratio, {"width": 1344, "height": 768})

    payload = {
        "highPixels": False,
        "model_id": "23887bba-507e-4249-a0e3-6951e4027f2b",
        "prompt": prompt,
        "negative_prompt": "",
        "resolution": {
            "width": resolution["width"],
            "height": resolution["height"],
            "batch_size": batch_size
        },
        "model_ability": {},
        "seed": seed_value,
        "steps": 6,
        "cfg": 1,
        "sampler_name": "euler",
        "scheduler": "normal",
        "ponyTags": {},
        "denoise": 1,
        "hires_fix_denoise": 0.5,
        "hires_scale": 2,
        "multi_img2img_info": {"style_list": []},
        "img_control_info": {"style_list": []},
        "continueCreate": False
    }

    try:
        res = requests.post(f"{API_BASE}/generate-image?authorization_token={token}", json=payload, timeout=120)
        res.raise_for_status()
        mark_id = res.json().get("mark_id")
        return jsonify({"mark_id": mark_id})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/check")
def check_image():
    mark_id = request.args.get("mark_id")
    token = request.args.get("token")

    try:
        check_res = requests.post(f"{API_BASE}/check-image?mark_id={mark_id}&authorization_token={token}", timeout=60)
        data = check_res.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)