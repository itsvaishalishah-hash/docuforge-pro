<div align="center">

# DocuForge Pro

### The companion code repository for *Build a Secure PDF Toolkit Using Python and Streamlit*
**Book Two in The Weekend Developer Series**

*A Weekend Project to Merge, Split, Watermark, Encrypt, and OCR PDFs Without the Cloud*

[![Live Demo](https://img.shields.io/badge/Live%20Demo-docuforge--pro.streamlit.app-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://docuforge-pro.streamlit.app/)
[![Buy on Amazon](https://img.shields.io/badge/Buy%20the%20Book-Amazon-FF9900?style=for-the-badge&logo=amazon&logoColor=white)](https://amzn.in/d/0dnI5DVY)
[![Leave a Review](https://img.shields.io/badge/Leave%20a%20Review-Amazon-FF9900?style=for-the-badge&logo=amazon&logoColor=white)](https://www.amazon.in/review/create-review/?ie=UTF8&channel=glance-detail&asin=B0H5W2PYS1)
[![Weekend Developer Series](https://img.shields.io/badge/Weekend%20Developer%20Series-See%20All%20Titles%20on%20Kindle-1B3358?style=for-the-badge)](https://www.amazon.in/dp/B0H56RF778?binding=kindle_edition&qid=1781778249&sr=1-1&ref=dbs_dp_rwt_sb_pc_tkin)

![Python](https://img.shields.io/badge/Python-3.14.5+-3776AB?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Offline](https://img.shields.io/badge/100%25-Offline-success?style=flat-square)

</div>

---

## Try It Before You Build It

Don't take our word for it — open the finished application right now:

**[https://docuforge-pro.streamlit.app/](https://docuforge-pro.streamlit.app/)**

Drop in a PDF, merge it, watermark it, lock it behind a password, or pull text out of a scanned page. Everything you see live is exactly what this repository teaches you to build, piece by piece, chapter by chapter.

---

## What Is DocuForge Pro?

DocuForge Pro is a secure, fully offline desktop application that handles the everyday document operations people normally hand over to free, browser-based PDF converters — except every byte stays on your own machine. Nothing is ever uploaded anywhere.

| Capability | What it does |
|---|---|
| **Merge & Split** | Combine multiple PDFs or surgically extract individual pages, entirely in memory |
| **Watermark & Brand** | Stamp precisely positioned, transparent watermarks using Cartesian coordinate geometry |
| **Secure & Optimize** | Scrub hidden author/producer metadata and apply real AES-256 password protection |
| **OCR Recovery** | Extract readable text from scanned faxes and photographed documents via a local Tesseract OCR engine |
| **Zero Cloud Footprint** | Every operation runs in volatile memory on your machine — no file ever leaves it |

---

## Built Chapter by Chapter

This repository follows the book's deliberate single-file architecture — by design, the entire application routes through one master `app.py`, rather than being split across a maze of imported modules. It's organized to match the four-section, nine-chapter build:

- **Section I — The Blueprint** — product scope, isolated environment setup, and the branded Streamlit interface
- **Section II — The Engine** — in-memory merge/split pipelines and coordinate-based watermarking
- **Section III — The Vault** — metadata forensics, AES-256 encryption, and the local OCR pipeline
- **Section IV — The Launch** — packaging, deployment to Streamlit Community Cloud, and the architecture deep-dive

```
docuforge/
├── app.py
├── DocuForge Pro.lnk
├── packages.txt
├── requirements.txt
└── run_app.bat
```

`.env` and the git-ignored `.venv/` virtual environment never get pushed to GitHub — `.gitignore` keeps them sealed off, exactly as the book sets up in Chapter 2. `DocuForge Pro.lnk` is the pinned Windows shortcut from Chapter 8's desktop packaging walkthrough; macOS/Linux users will have a `run_app.sh` in its place instead.

---

## Getting Started

```bash
# Clone the repository
git clone <your-repo-url>
cd docuforge

# Create an isolated environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

Once it's set up, you don't need to touch the terminal again — `run_app.bat` (Windows) or `run_app.sh` (macOS/Linux) launches the app silently in the background with a single double-click, exactly as the book sets it up in Chapter 8.

**One extra step this book walks through in detail:** Tesseract OCR is a system-level binary, not a Python package, so it must be installed separately on your machine before Chapter 7's OCR pipeline will work — full platform-by-platform setup instructions are in Chapter 2. If you deploy to Streamlit Community Cloud instead of running locally, `packages.txt` handles that same Tesseract installation automatically on the cloud container.

---

## This Is Book Two of The Weekend Developer Series

The Weekend Developer Series is built on one promise: start on a Saturday morning, and you'll have a fully functional, real-world application running — deployed, not just demoed — before Monday. No academic detours, no padded theory chapters, just a complete build from a blank file to a finished product.

DocuForge Pro is the second title in the series. If this is your first time here, you'll want to see the rest of the lineup:

**[Browse the full series catalog →](https://sharanamshah.com/mymusings/the-weekend-developer-series-on-kindle/)**

**[See every Weekend Developer Series title on Kindle →](https://www.amazon.in/dp/B0H56RF778?binding=kindle_edition&qid=1781778249&sr=1-1&ref=dbs_dp_rwt_sb_pc_tkin)**

---

## Get the Book

The full book walks through every line of code in this repository with real-world analogies, exact terminal commands, complete unredacted code, and a rigorous test plan for each chapter.

**[Buy *Build a Secure PDF Toolkit Using Python and Streamlit* on Amazon →](https://amzn.in/d/0dnI5DVY)**

Already read it? A review takes two minutes and helps far more than you'd think — it's what gets a book like this in front of the next developer searching for exactly this project.

**[Leave a review on Amazon →](https://www.amazon.in/review/create-review/?ie=UTF8&channel=glance-detail&asin=B0H5W2PYS1)**

---

## About the Authors

Sharanam and Vaishali Shah are Mumbai-based authors with over 23 years of hands-on experience in application architecture and enterprise software. Together they have co-authored over 40 technical books, built on one belief: the best way to learn is to build.

Questions, feedback, or a framework you'd like to see covered next? Write to **enquiries@sharanamshah.com** — every message is read.

---

## License

The code in this repository accompanies the book and is provided for educational use.

<div align="center">

**If this repository helped you, consider starring it — and [leaving a review on Amazon](https://www.amazon.in/review/create-review/?ie=UTF8&channel=glance-detail&asin=B0H5W2PYS1) helps other developers find the book.**

</div>
