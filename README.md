# 🖼️ Text-to-Image Generator (Flask UI)
UI Website: https://rudra-text-to-image-ui.onrender.com
This project provides a simple web-based UI using Flask to generate AI images from text prompts via an external API ([https://rudra-text-to-image.onrender.com](https://rudra-text-to-image.onrender.com)). You can select various aspect ratios, enable seeds, and preview/download generated images directly in the same interface.

---

## 🚀 Features

* 🔤 Text Prompt to AI-generated Image
* 🎛️ Aspect Ratio & Batch Size Selection
* 🌱 Seed control for reproducibility
* 🔁 Live status polling
* 📥 Instant preview & download on same page
* 🧑‍💻 Fully client-driven UI with Bootstrap

---

## 🏗️ Technologies Used

* Python 3.9+
* Flask
* HTML5 + Bootstrap 5
* JavaScript (Fetch API)

---

## 📂 Project Structure

```
.
├── main.py               # Flask server
├── templates/
│   └── index.html        # Main UI page
├── static/               # Optional for CSS or assets
└── requirements.txt      # Python dependencies
```

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourname/text-to-image-flask-ui.git
cd text-to-image-flask-ui
```

### 2. Create Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
python main.py
```

Then open `http://127.0.0.1:5000` in your browser.

---

## 🌐 Deploy on Render (Free Tier)

1. Create a free account on [https://render.com](https://render.com)

2. Click **"New Web Service"** > **"Deploy from GitHub"**

3. Connect your repo and choose:

   * Runtime: Python
   * Build Command: `pip install -r requirements.txt`
   * Start Command: `python main.py`

4. Set `PORT` environment variable = `10000` (Render auto-maps it)

5. Deploy and test the live endpoint 🎉

---

## 📝 Example Prompt

```
An astronaut relaxing under a tree on Mars, cinematic lighting, ultra-realistic
```

---

## 🛠️ Customization

* You can change the default model ID or API base URL in `main.py`
* Bootstrap UI elements can be styled further in `index.html`

---

## 🙏 Credits

* API: [rudra-text-to-image.onrender.com](https://rudra-text-to-image.onrender.com)
* UI: Inspired by OpenAI Playground, HuggingFace

---

## 📄 License

MIT License. Feel free to fork and customize.
