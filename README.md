# Website Contact Scraper 📧

## 📌 Project Overview

The **Website Contact Scraper** is a Python desktop application that extracts publicly available contact information from company websites. It uses web scraping techniques to collect email addresses, mobile numbers, landline numbers, and other phone numbers.

The application is built with **CustomTkinter**, providing a graphical user interface (GUI) where users can enter multiple website URLs, start scraping, view results, and export the collected information to an Excel file.

## ✨ Features

- **Bulk Website Scraping:** Enter multiple website URLs to process them in one run.
- **Email Extraction:** Finds email addresses available on website pages.
- **Mobile Number Extraction:** Identifies valid mobile numbers using the `phonenumbers` library.
- **Landline Extraction:** Separates valid fixed-line phone numbers.
- **Additional Phone Numbers:** Stores other recognized phone number types separately.
- **Contact Page Scanning:** Searches the homepage and relevant internal pages containing keywords such as Contact, About, Support, and Company.
- **Graphical User Interface:** Simple interface built using CustomTkinter.
- **Progress Tracking:** Displays scraping status and progress.
- **Excel Export:** Saves results in `.xlsx` format with separate columns for each contact category.
- **Error Handling:** Reports website and page errors without necessarily stopping the entire scraping process.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| CustomTkinter | Desktop graphical user interface |
| Requests | Sends HTTP requests to websites |
| BeautifulSoup | Parses HTML content |
| Regular Expressions (`re`) | Extracts email addresses |
| phonenumbers | Validates and classifies phone numbers |
| OpenPyXL | Exports results to Excel |
| Threading | Runs scraping in a background thread |
| urllib.parse | Processes URLs and constructs page links |

## 📋 Requirements

- Python 3.12 recommended for this project.
- Internet connection.
- A code editor such as Visual Studio Code.
- Required Python libraries.

## ⚙️ Installation

### Step 1: Install Python libraries

Open the VS Code terminal or Command Prompt and run:

```bash
py -3.12 -m pip install customtkinter requests beautifulsoup4 openpyxl phonenumbers
```

Alternatively, use `pip` if your Python environment is configured correctly:

```bash
pip install customtkinter requests beautifulsoup4 openpyxl phonenumbers
```

### Step 2: Download or clone the project

If you are using Git:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Alternatively, download the project files and open the project folder in VS Code.

### Step 3: Run the application

Save your Python code in a file named `ScrappingApp.py` and run:

```bash
py -3.12 ScrappingApp.py
```

The Website Contact Scraper window will open.

## 🚀 How to Use

1. Run the Python application.
2. Enter one or more website URLs in the **Enter Website URLs** text box, with one URL per line.
3. Click **Start Scraping**.
4. Monitor the progress and view the extracted contact information in the results panel.
5. After scraping finishes, click **Save Results**.
6. Select a location and save the results as an Excel workbook.

### Example Website Input

```text
https://example.com
https://www.python.org
https://www.wikipedia.org
```

These are example URLs for demonstrating the input format. Contact details may not be available on every website.

## 📊 Excel Output

The application exports the collected data to an Excel workbook named `Company Contact Data.xlsx` by default.

The workbook contains a worksheet named `Company Contacts` with the following columns:

| Column | Description |
|---|---|
| Sr. No. | Serial number |
| Company Website | Website URL |
| Email Addresses | Extracted email addresses |
| Mobile Numbers | Valid numbers classified as mobile |
| Landline Numbers | Valid fixed-line numbers |
| Other Phone Numbers | Other recognized phone number types |

If a contact category has no results, the application records `Not found`.

## 🔍 How It Works

1. The user enters website URLs into the application.
2. The program checks and normalizes the URL format.
3. Requests downloads the website's HTML content.
4. BeautifulSoup parses the HTML.
5. The scraper searches for email addresses and phone numbers.
6. It identifies relevant internal pages using keywords such as Contact, About, Support, and Company.
7. It scans up to five selected pages per website, including the homepage.
8. The extracted information is organized by website.
9. The results can be exported to Excel using OpenPyXL.

## 📁 Project Structure

```text
Website-Contact-Scraper/
│
├── ScrappingApp.py
├── README.md
└── Company Contact Data.xlsx
```

`Company Contact Data.xlsx` is generated when the user saves the results; it does not need to exist before running the application.

## ⚠️ Limitations

- Some websites may block automated requests or require JavaScript to display contact details.
- Some websites may be unavailable because of network, DNS, or server errors.
- The scraper only scans a limited number of selected pages per website.
- Phone number classification uses the India region (`IN`) and may not correctly classify numbers from other countries.
- Email addresses or phone numbers hidden behind forms, images, logins, or dynamically loaded content may not be detected.
- Extracted information may be incomplete or outdated.

## 🔐 Responsible Use

Use this application responsibly. Collect only publicly available business contact information, respect website terms of service and applicable privacy laws, and avoid excessive requests. Do not use the collected information for spam, unsolicited bulk messaging, or unauthorized marketing.

## 🔮 Future Improvements

- Add a Stop Scraping button.
- Support configurable scanning limits.
- Add CSV export functionality.
- Improve international phone number support.
- Add duplicate contact detection.
- Display more detailed per-website results.
- Package the application as a Windows executable using PyInstaller.

## 👩‍💻 Project Information

**Project Name:** Website Contact Scraper

**Language:** Python

**Application Type:** Desktop GUI Application

**Main Purpose:** To automate the collection and organization of publicly available contact information from websites.

---

⭐ If you find this project useful, consider giving the repository a star on GitHub.
