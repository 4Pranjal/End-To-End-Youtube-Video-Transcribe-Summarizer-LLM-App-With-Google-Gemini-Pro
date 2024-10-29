# 🎬 End-To-End YouTube Video Transcribe & Summarizer App with Google Gemini Pro

Welcome to the YouTube Video Summarizer App! This application takes a YouTube video link as input, extracts the transcript, and provides a concise, meaningful summary using **Google Gemini Pro**'s Generative AI. Perfect for turning lengthy videos into quick, insightful notes!

## 📂 Table of Contents
- [🚀 Getting Started](#-getting-started)
- [⚙️ Installation](#%EF%B8%8F-installation)
- [🔑 Environment Variables](#-environment-variables)
- [🔨 Usage](#-usage)
- [📸 Preview](#-preview)
- [👥 Contributing](#-contributing)
- [📄 License](#-license)
- [👤 Credits](#-credits)

---

## 🚀 Getting Started

### Prerequisites
To get started, make sure you have:
- Python 3.8+ installed
- A **Google Cloud** account with **Google Gemini Pro** API enabled
- The **YouTube Transcript API** installed

Clone this repo to start summarizing YouTube videos effortlessly!

``` bash 
git clone https://github.com/4Pranjal/End-To-End-Youtube-Video-Transcribe-Summarizer-LLM-App-With-Google-Gemini-Pro.git
```
``` bash 
cd End-To-End-Youtube-Video-Transcribe-Summarizer-LLM-App-With-Google-Gemini-Pro
```

## ⚙️ Installation

1. **Install dependencies**: Use the following command to install required libraries from `requirements.txt`.

    ``` bash
   pip install -r requirements.txt
    ```

3. **Environment Setup**: Load environment variables by creating a `.env` file in the root directory.

    ``` bash
   GOOGLE_API_KEY=<Your_Google_Gemini_API_Key>
    ```

---

## 🔑 Environment Variables

You'll need a `.env` file with the following variable for secure access to the Google Gemini API.

1. **GOOGLE_API_KEY**: This is your unique Google Gemini API key.
   
   - **Where to get it**: Log in to your [Google Cloud Console](https://console.cloud.google.com/), enable the Gemini API, and generate your API key.
   
2. Add the `GOOGLE_API_KEY` value to the `.env` file:
   
   ```bash
   GOOGLE_API_KEY=your-google-api-key
   ```

---

## 🔨 Usage

Once set up, run the application to start summarizing YouTube videos:

```bash
streamlit run app.py
```

### Step-by-Step Usage

1. **Enter YouTube Video URL**: Copy any YouTube video link and paste it into the input field in the app.
   
2. **Get Detailed Notes**: Click on the **"Get Detailed Notes"** button. The app will:
   - Fetch the transcript of the video.
   - Generate a detailed summary using **Google Gemini Pro**.

3. **View Results**: The app will display a clear, concise summary of the video content for easy reference.

---

## 📸 Preview

**App Interface**:
![d22](https://github.com/user-attachments/assets/0e3c6d37-891a-4452-88e0-e4e090b1482e)


**Example Summary**:
Once you enter a YouTube link, here’s how a summary might look:
![d33](https://github.com/user-attachments/assets/94106068-664e-4bdd-82ab-d52eb1bafe88)

---

## 👥 Contributing

Contributions are welcome! If you find any issues or want to enhance the code, feel free to open an issue or submit a pull request.

1. **Fork the repository**.
2. **Create a new branch** with a descriptive name:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Commit your changes**:
   ```bash
   git commit -m "Added new feature: your-feature-name"
   ```
6. **Push to the branch**:
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Create a Pull Request**.

---

## 👤 Credits

This repository is maintained by **4Pranjal**. Feel free to use and modify the code for educational and research purposes.

For any questions or suggestions, you can contact me through my GitHub profile: [@4Pranjal](https://github.com/4Pranjal).

Made with ❤️ by Pranjal Jain
