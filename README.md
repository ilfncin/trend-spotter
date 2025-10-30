# 🧠 Trend Spotter AI Agent

This project is based on a tutorial that demonstrates how to build your first AI agent using the **Agent Developer Kit (ADK)**.

> 📚 **Original tutorial**: [Your First AI Agent – A Beginner’s Guide to Building an AI Trend Finder with ADK (Google Cloud)](https://medium.com/google-cloud/your-first-ai-agent-a-beginners-guide-to-building-an-ai-trend-finder-with-adk-3a7c6a93ff33)

---

## 📦 About the Project

This agent identifies emerging trends and generates highly relevant, verifiable reports about the latest developments in AI agents — specifically those impacting developers. It also provides a local web interface for interactive testing and experimentation.


---

## 🗂️ Project Structure

```
trend-spotter/
├── trend_spotter/
│   ├── __init__.py
│   ├── agent.py         # Main agent implementation
│   └── prompt.py        # Prompt template used by the agent
├── .env                 # Environment variables for local config
├── pyproject.toml       # Project metadata for poetry or pip
├── requirements.txt     # Python dependencies
└── README.md            # This file
```
---
## ☁️ Installing Google Cloud SDK on Ubuntu
Before installing the Google Cloud SDK, make sure your system meets the following prerequisites:

### ✅ Pre-requirements

1. Your OS is a supported Ubuntu or Debian release (not end-of-life).

2. You’ve recently updated your package list:
```bash
sudo apt-get update
```

3. You have the following packages installed:
```bash
sudo apt-get install apt-transport-https ca-certificates gnupg curl
```


### 🔧 Steps Followed

To run the agent locally and authenticate with Google Cloud, the **Google Cloud SDK** must be installed. Below is the setup process used for Debian-based systems (e.g., Ubuntu):

**1. Import the Google Cloud public key**
   ```bash
   curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg
   ```

   > **Explanation**: _This command downloads the official Google Cloud public GPG key and converts it into a .gpg format using gpg --dearmor. This key is used to verify the authenticity of packages downloaded from the Google repository, ensuring they haven’t been tampered with. The result is stored in /usr/share/keyrings/cloud.google.gpg._

**2. Add the Cloud SDK distribution URI as a package source**
   ```bash
   echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
   ```

   > **Explanation**: _This command tells the package manager (apt) where to find the Google Cloud SDK. It adds the Google Cloud package repository to your system, and links it to the GPG key imported earlier, so only trusted packages from that source will be accepted._

**3. Update and install the gcloud CLI**
   ```bash
   sudo apt-get update && sudo apt-get install google-cloud-cli
   ```

   > **Explanation**: _The google-cloud-cli (Google Cloud Command Line Interface) is the official suite of command-line tools provided by Google Cloud Platform (GCP). It allows you to manage, configure, and interact with GCP resources directly from your terminal, without relying on the web-based console. After updating your system's package list, this command installs the CLI so you can start using commands like gcloud, gsutil, and bq to manage services such as Compute Engine, Cloud Storage, BigQuery, Vertex AI, and more._

**4. Initialize the gcloud CLI**
   ```bash
   gcloud init
   ```

   > **Explanation**: _This command launches an interactive setup process where you log into your Google account, select or create a GCP project, and set default configurations (project, region, etc.). This step is essential before using gcloud commands._

**5. Common Post-Init Commands**

   After initializing gcloud, here are some useful commands to inspect your configuration:

   * **Check active configuration values**:
      ```bash
      gcloud config list
      ```
   
      Displays the current settings for your CLI environment, including the active project, account, region, and more.

   * **View detailed environment info**:
      ```bash
      gcloud info
      ```
      Shows detailed information about your gcloud setup, including SDK version, system details, config paths, and current active settings.


📚For full instructions, refer to the official guide:
[Installing Cloud SDK on Linux (Debian/Ubuntu)](https://cloud.google.com/sdk/docs/install)

---

## 🚀 Requirements

- Python 3.12+
- Google Cloud account
- A GCP project with **Vertex AI API** enabled
- Billing enabled on the GCP project

### ⚠️ Enabling Billing and Vertex AI API

To use Vertex AI models in this project, make sure that both **billing is active** and **Vertex AI API is enabled** for your project.

#### 1. Check project billing
Open the billing console: [Google Cloud Billing](https://console.cloud.google.com/billing)

- Confirm that your project (e.g. `trend-spotter-dev`) is **linked to an active billing account**.
- If not, click "Link a billing account".
- Google offers **$300 free credits** for new accounts.

#### 2. Enable the Vertex AI API
Activate the API by opening this link (replace project ID if needed):

👉 [Enable Vertex AI API](https://console.cloud.google.com/apis/api/aiplatform.googleapis.com/metrics?project=trend-spotter-dev)

Click the blue “Enable” button. This may take 1–2 minutes.

#### 3. Test if billing is enabled
You can verify billing status with this command:

```bash
gcloud billing projects describe trend-spotter-dev
```

If it returns:

```
billingEnabled: true
```

Then everything is ready.

---

## ⚙️ Environment Setup

**1. Create and activate a virtual environment**:
```bash
python -m venv .venv
source .venv/bin/activate
```

**2. Install dependencies**:
```bash
pip install -r requirements.txt
```

**3. Create your .env file**

Before running the application, make a copy of the example environment file:
```bash
cp .env.template .env
```

This will create a `.env` file based on the template provided. You can then edit it to customize environment variables such as project ID and region.

These variables are essential for connecting the **Agent Developer Kit (ADK)** to your **Google Cloud account** and enabling access to **Vertex AI models**:
```dotenv
GOOGLE_GENAI_USE_VERTEXAI=true
GOOGLE_CLOUD_PROJECT=<your-gcp-project-id>
GOOGLE_CLOUD_LOCATION=<your-gcp-project-location>
```

**What they do**:
   * **GOOGLE_GENAI_USE_VERTEXAI=true**: Tells the agent to use Vertex AI as the backend for generative models like Gemini.
   * **GOOGLE_CLOUD_PROJECT**: Specifies the default Google Cloud project ID where APIs and resources (like models) are located.
   * **GOOGLE_CLOUD_LOCATION**: Defines the region (e.g., us-central1, us-east1) where Vertex AI services are hosted — must match where the model is available.

**4. Authenticate with Google Cloud:**
   
Run the following command to authenticate your local environment with your Google account:
```bash
gcloud auth application-default login
```
This command opens a browser window for you to log in. It allows the agent to make authorized requests to Google Cloud services using your credentials.


---

## 🧪 Running Locally

1. Install the agent in editable mode:
   ```bash
   pip install -e .
   ```

2. Start the web UI:
   ```bash
   adk web
   ```

   Access it at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧠 Model Used

- **Vertex AI Publisher Model**: `gemini-2.5-flash`
- **Location (`GOOGLE_CLOUD_LOCATION`)**: `us-central1`

**⚠️ Important**: Make sure the model version you are using (e.g., `gemini-2.5-flash`) is still available in your region.
Google may update or deprecate older model versions over time.

Always verify the currently supported models and their versions at:
🔗 [Vertex AI Model Versions](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions#gemini-model-versions)


---

## 🧾 License & Credits

This project is inspired by a community-published tutorial that demonstrates how to build an AI trend finder using the Agent Developer Kit (ADK).

**📚 Reference**:  
Lador, Shir Meir. “Your First AI Agent: A Beginner’s Guide to Building an AI Trend Finder with ADK.” Google Cloud – Community, 7 Jun. 2025. Medium.
🔗 [https://medium.com/google-cloud/your-first-ai-agent-a-beginners-guide-to-building-an-ai-trend-finder-with-adk-3a7c6a93ff33](https://medium.com/google-cloud/your-first-ai-agent-a-beginners-guide-to-building-an-ai-trend-finder-with-adk-3a7c6a93ff33)

---
