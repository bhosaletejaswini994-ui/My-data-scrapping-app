# from bs4 import BeautifulSoup
# import requests
# import re
# web_development_companies = [
    # "https://www.aalpha.net/",
    # "https://www.neosofttech.com/",
    # "https://www.datamatics.com/",
    # "https://www.robosoftin.com/",
    # "https://www.ajackus.com/",
    # "https://www.theadroit.in/",
    # "https://www.matrixbricks.com/",
    # "https://www.leo9studio.com/",
    # "https://www.webenza.com/",
    # "https://www.qburst.com/",
    # "https://www.tataelxsi.com/",
    # "https://www.techmahindra.com/",
#     "https://www.persistent.com/",
#     "https://www.infosys.com/",
#     "https://www.tcs.com/",
#     "https://www.wipro.com/",
#     "https://www.capgemini.com/",
#     "https://www.cognizant.com/",
#     "https://www.ltimindtree.com/",
#     "https://www.hcltech.com/",
#     "https://www.birlasoft.com/",
#     "https://www.cybage.com/",
#     "https://www.eclerx.com/",
#     "https://hexaware.com/",
#     "https://www.zensar.com/",
#     "https://www.yash.com/",
#     "https://www.kpit.com/",
#     "https://www.infobeans.com/",
#     "https://www.valuecoders.com/",
#     "https://www.hiddenbrains.com/",
#     "https://www.mindinventory.com/",
#     "https://www.tatvasoft.com/",
#     "https://www.simform.com/",
#     "https://www.brainvire.com/",
#     "https://webandcrafts.com/",
#     "https://appinventiv.com/",
#     "https://www.clariontech.com/",
#     "https://www.technource.com/",
#     "https://radixweb.com/",
#     "https://www.brillianteweb.com/",
#     "https://www.cmsminds.com/",
#     "https://www.tecocraft.com/",
#     "https://www.scnsoft.com/",
#     "https://www.krishtechnolabs.com/",
#     "https://www.elsner.com/",
#     "https://www.magnetoitsolutions.com/",
#     "https://www.openxcell.com/",
#     "https://binmile.com/",
#     "https://www.webcluesinfotech.com/",
#     "https://krify.co/",
#     "https://www.sparxitsolutions.com/",
#     "https://www.apptha.com/",
#     "https://www.netclues.com/",
#     "https://technostacks.com/",
#     "https://www.csschopper.com/",
#     "https://htmlpanda.com/",
#     "https://www.unifiedinfotech.net/",
#     "https://www.itechindia.co/",
#     "https://www.logicspice.com/",
#     "https://www.peerbits.com/",
#     "https://www.xicom.biz/",
#     "https://www.classicinformatics.com/",
#     "https://www.pixelcrayons.com/",
#     "https://www.techaheadcorp.com/",
#     "https://www.techuz.com/",
#     "https://www.konstantinfo.com/",
#     "https://www.fexle.com/",
#     "https://www.orangemantra.com/",
#     "https://mobisoftinfotech.com/",
#     "https://www.thinkitive.com/",
#     "https://searce.com/",
#     "https://coditas.com/",
#     "https://www.ezeiatech.com/",
#     "https://www.webguru-india.com/",
#     "https://www.webskitters.com/",
#     "https://www.weblineindia.com/",
#     "https://digitalaptech.com/",
#     "https://www.iwebservices.com/",
#     "https://www.softwaredevelopersinc.com/",
#     "https://www.mindfiresolutions.com/",
#     "https://www.appcino.com/",
#     "https://www.admecindia.co.in/",
#     "https://www.indglobaldigital.com/",
#     "https://www.technoheaven.com/",
#     "https://www.pixelvalues.com/",
#     "https://www.adroitte.in/",
#     "https://www.webnexs.com/",
#     "https://www.krishangtechnolab.com/",
#     "https://www.colaninfotech.com/",
#     "https://www.mobulous.com/",
#     "https://www.infyom.com/",
#     "https://www.technosip.com/",
#     "https://www.xceltec.com/",
#     "https://www.eiosys.com/",
#     "https://www.webmigrates.com/",
#     "https://www.letsnurture.com/",
#     "https://www.girnarsoft.com/",
#     "https://www.softwebsolutions.com/",
#     "https://www.rapidops.com/",
#     "https://www.tridhya.com/"
# ]

# file = open("Scrapped Data.txt", "a")

# for url in web_development_companies:
#     try:

#         response = requests.get(url)
#         soup = BeautifulSoup(response.content, 'html.parser')
        
#         # Extract email addresses using regex
#         email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
#         emails = re.findall(email_pattern, soup.get_text())
        
#         # Print the extracted email addresses
#         print(f"Email addresses found on {url}:")
#         for email in emails:
#             print(email)
#             file.write(f"{email}\n")
#         print("\n")
#     except Exception as e:
#         print(f"Error occurred while scraping {url}: {e}")

# file.close()

# import email

# import customtkinter as ctk
# from bs4 import BeautifulSoup
# import requests
# import re
# import threading
# import time

# web_development_companies = ["https://www.aalpha.net/",
#     "https://www.neosofttech.com/",
#     "https://www.datamatics.com/",
#     "https://www.robosoftin.com/",
#     "https://www.ajackus.com/",
#     "https://www.theadroit.in/",
#     "https://www.matrixbricks.com/",
#     "https://www.leo9studio.com/",
#     "https://www.webenza.com/",
#     "https://www.qburst.com/",
#     "https://www.tataelxsi.com/",
#     "https://www.techmahindra.com/",]

# ctk.set_appearance_mode("light")
# ctk.set_default_color_theme("blue")

# window = ctk.CTk()
# window.geometry("900x600")
# window.title("Web Scrapping App")
# window.resizable(width=False, height=False)
# window.configure(fg_color="#F0F4F8")

# found_emails = set()  
# is_running = False


# header = ctk.CTkLabel(window, text="Web Scrapping App", font=("Arial", 28, "bold"), text_color="#183153")
# header.label.pack(pady=(25,5))

# subtitle_label = ctk.CTkLabel(window, text="Scrapping Emails from Web Development Companies", font=("Arial", 14), text_color="#183153")
# subtitle_label.pack(pady=(0,20))

# status_label = ctk.CTkLabel(window, text="Ready to start", font=("Arial", 14), text_color="#183153")
# status_label.pack(pady=5)

# progress_bar = ctk.CTkProgressBar(window, width=700)
# progress_bar.pack(pady=10)
# progress_bar.set(0)

# results_box = ctk.CTkTextbox(window,width=800,height=370,font=("Consolas", 13),corner_radius=12)
# results_box.pack(pady=15, padx=30)
# results_box.insert("end", "Found email addresses will appear here...\n")

# email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# def show_status(message):
#     window.after(0, lambda: status_label.configure(text=message))

# def show_emails(emails):
#     window.after(0,lambda:results_box.insert("end",email+"\n"))

# def scrape_websites():
#     global is_running

#     found_emails.clear()
#     total=len(web_development_companies)

#     results_box.delete("1.0", "end")

#     for index, item in enumerate(web_development_companies, start=1):
#         match = re.search(r"https?://(?:www\.)?([^/]+)", item)

#         if not match:
#             show_status(f"Skipping invalid URL: {item}")
#             continue
#         url = match.group(0)

#         url =url.rstrip("/")
        



#  & "C:\Users\Hp\AppData\Local\Python\pythoncore-3.14-64\python.exe" "C:\Users\Hp\Desktop\Tejaswini\ScrappingApp.py"   


# import customtkinter as ctk
# from bs4 import BeautifulSoup
# import requests
# import re
# import threading


# ctk.set_appearance_mode("light")
# ctk.set_default_color_theme("blue")

# window = ctk.CTk()
# window.geometry("1000x650")
# window.title("Website Email Scraper")
# # window.resizable(False, False)
# # window.configure(fg_color="#F0F4F8")


# found_emails = set()
# is_running = False


# header = ctk.CTkLabel(window,text="Website Email Scraper",font=("Arial", 26, "bold"),text_color="#183153")
# header.pack(pady=20)

# main_frame = ctk.CTkFrame(window,fg_color="transparent")
# main_frame.pack(fill="both", expand=True, padx=20, pady=10)

# left_frame = ctk.CTkFrame(main_frame, width=400)
# left_frame.pack(side="left",fill="both", expand=True, padx=10)
# left_frame.pack_propagate(False)


# ctk.CTkLabel(
#     left_frame,
#     text="Enter Website URL",
#     font=("Arial", 20, "bold")
# ).pack(pady=25)




# url_box = ctk.CTkTextbox(
#     left_frame,
#     width=350,
#     height=350,
#     font=("Consolas", 13)
# )
# url_box.pack(padx=15, pady=10, fill="both", expand=True)

# url_box.insert(
#     "1.0",
#     "https://www.socialbeat.in/nhttps://www.schbang.com/n"
# )

# status_label = ctk.CTkLabel(left_frame,text="Ready to start")
# status_label.pack(pady=15)

# progress_bar = ctk.CTkProgressBar(left_frame, width=300)
# progress_bar.pack(pady=10)
# progress_bar.set(0)

# right_frame = ctk.CTkFrame(main_frame, width=400)
# right_frame.pack(side="right", fill="both", expand=True, padx=10)

# ctk.CTkLabel(
#     left_frame,
#     text="Enter Website URL",
#     font=("Arial", 20, "bold")
# ).pack(pady=25)

# results_box = ctk.CTkTextbox(right_frame,width=400,height=400)
# results_box.pack(fill="both", expand=True, padx=15, pady=10)
# results_box.insert("end", "Email results will appear here...\n")

# def scrape_website(url):
#     global is_running

#     try:
#         response = requests.get(url,timeout=15,headers={"User-Agent": "Mozilla/5.0"})
#         response.raise_for_status()

#         soup = BeautifulSoup(response.text, "html.parser")

#         pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
#         emails = set(re.findall(pattern, soup.get_text(" ", strip=True)))

#         for link in soup.select('a[href^="mailto:"]'):
#             email = link["href"][7:].split("?")[0].strip()
#             if re.fullmatch(pattern, email):
#                 emails.add(email)

#         new_emails = emails - found_emails

#         for email in sorted(new_emails):
#             found_emails.add(email)
#             window.after(0,lambda e=email: results_box.insert("end", e + "\n"))

#         if not new_emails:
#             window.after(0,lambda: results_box.insert("end", "No new emails found on this page.\n"))

#         window.after(0,lambda: status_label.configure(text=f"Finished! {len(emails)} emails found on this page."))
#         window.after(0, lambda: progress_bar.set(1))
#         window.after(0, lambda: save_button.configure(state="normal"))

#     except Exception as error:
#         window.after(0,lambda: status_label.configure(text="Could not access website"))
#         window.after(0,lambda: results_box.insert("end", f"Error: {error}\n"))

#     finally:
#         is_running = False
#         window.after(0, lambda: start_button.configure(state="normal"))



# def start_scraping():
#     global is_running

#     if is_running:
#         return

#     urls = url_box.get("1.0", "end").strip().splitlines()
# urls = [url.strip() for url in urls if url.strip()]

#     if not url:
#         status_label.configure(text="Please enter a website URL")
#         return

#     if not url.startswith(("https://", "http://")):
#         url = "https://" + url

#     if not re.match(r"^https?://[^/\s]+\.[^/\s]+", url):
#         status_label.configure(text="Please enter a valid URL")
#         return

#     is_running = True
#     start_button.configure(state="disabled")
#     save_button.configure(state="disabled")
#     progress_bar.set(0)

#     results_box.delete("1.0", "end")
#     results_box.insert("end", f"Website: {url}\n\n")

#     threading.Thread(target=scrape_website,args=(url,),daemon=True).start()



# def save_results():
#     if not found_emails:
#         status_label.configure(text="No emails to save")
#         return

#     try:
#         with open("Scraped Data.txt", "w", encoding="utf-8") as file:
#             for email in sorted(found_emails):
#                 file.write(email + "\n")

#         status_label.configure(text="Results saved successfully!")

#     except OSError as error:
#         status_label.configure(text=f"Save failed: {error}")



# start_button = ctk.CTkButton(left_frame,text="Scrape Website",width=220,height=40,command=start_scraping)
# start_button.pack(pady=15)

# save_button = ctk.CTkButton(left_frame,text="Save Results",width=220,height=40,fg_color="#18865B",command=save_results,state="disabled")
# save_button.pack(pady=5)

# window.mainloop()


                         
from tkinter import filedialog, messagebox
from openpyxl import Workbook
import customtkinter as ctk
from bs4 import BeautifulSoup
import requests
import re
import threading
from urllib.parse import urlparse, urljoin
import phonenumbers


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

window = ctk.CTk()
window.geometry("1000x650")
window.title("Website Contact Scraper")
window.resizable(False, False)

found_emails = set()
contact_results = []
is_running = False


email_pattern = re.compile(
    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
)




header = ctk.CTkLabel(
    window,
    text="Website Contact Scraper",
    font=("Arial", 26, "bold"),
    text_color="#183153"
)
header.pack(pady=15)


main_frame = ctk.CTkFrame(window, fg_color="transparent")
main_frame.pack(fill="both", expand=True, padx=15, pady=5)


left_frame = ctk.CTkFrame(main_frame, width=450)
left_frame.pack(
    side="left",
    fill="both",
    expand=True,
    padx=8
)
left_frame.pack_propagate(False)

ctk.CTkLabel(
    left_frame,
    text="Enter Website URLs",
    font=("Arial", 20, "bold")
).pack(pady=15)

url_box = ctk.CTkTextbox(
    left_frame,
    width=400,
    height=300,
    font=("Consolas", 13)
)
url_box.pack(fill="both", expand=True, padx=12, pady=5)


status_label = ctk.CTkLabel(
    left_frame,
    text="Ready to start",
    wraplength=400
)
status_label.pack(pady=8)

progress_bar = ctk.CTkProgressBar(left_frame, width=300)
progress_bar.pack(pady=5)
progress_bar.set(0)


right_frame = ctk.CTkFrame(main_frame, width=450)
right_frame.pack(
    side="right",
    fill="both",
    expand=True,
    padx=8
)

ctk.CTkLabel(
    right_frame,
    text="Contact Results",
    font=("Arial", 20, "bold")
).pack(pady=15)

results_box = ctk.CTkTextbox(
    right_frame,
    width=400,
    height=400,
    font=("Consolas", 13)
)
results_box.pack(fill="both", expand=True, padx=12, pady=5)

results_box.insert("end", "Contact results will appear here...\n")



def show_result(message):
    def update():
        results_box.insert("end", message + "\n")
        results_box.see("end")

    window.after(0, update)


def show_status(message):
    def update():
        status_label.configure(text=message)

    window.after(0, update)

def extract_contacts(soup):
    emails = set()
    mobiles = set()
    landlines = set()
    other_phones = set()

    
    page_text = soup.get_text(" ", strip=True)
    emails.update(email_pattern.findall(page_text))

    
    for link in soup.select('a[href^="mailto:"]'):
        email = link["href"].split(":", 1)[1]
        email = email.split("?", 1)[0].strip()

        if email_pattern.fullmatch(email):
            emails.add(email)

    
    phone_text = page_text

    
    for link in soup.select('a[href^="tel:"]'):
        phone_text += " " + link["href"].split(":", 1)[1]

    for match in phonenumbers.PhoneNumberMatcher(
        phone_text, "IN"
    ):
        number = match.number

        if not phonenumbers.is_valid_number(number):
            continue

        formatted = phonenumbers.format_number(
            number,
            phonenumbers.PhoneNumberFormat.INTERNATIONAL
        )

        number_type = phonenumbers.number_type(number)

        if number_type == phonenumbers.PhoneNumberType.MOBILE:
            mobiles.add(formatted)

        elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
            landlines.add(formatted)

        else:
            
            other_phones.add(formatted)

    return emails, mobiles, landlines, other_phones


def scrape_websites(urls):
    global is_running

    total = len(urls)
    contact_results.clear()
    found_emails.clear()

    try:
        for index, url in enumerate(urls, start=1):
            show_status(
                f"Processing website {index}/{total}"
            )
            show_result(f"\nWebsite {index}: {url}")

            website_emails = set()
            website_mobiles = set()
            website_landlines = set()
            website_other_phones = set()

            try:
                headers = {"User-Agent": "Mozilla/5.0"}

                
                response = requests.get(
                    url, timeout=15, headers=headers
                )
                response.raise_for_status()

                home_soup = BeautifulSoup(
                    response.text, "html.parser"
                )

               
                pages_to_scan = [url]
                visited_pages = {url}
                home_domain = urlparse(url).netloc

                
                keywords = (
                    "contact", "about", "support", "company"
                )

                for link in home_soup.find_all(
                    "a", href=True
                ):
                    href = link["href"].strip()
                    text = link.get_text(" ", strip=True)
                    searchable = (href + " " + text).lower()

                    if not any(
                        word in searchable for word in keywords
                    ):
                        continue

                    page_url = urljoin(url, href)
                    parsed_page = urlparse(page_url)

                    
                    if parsed_page.scheme not in (
                        "http", "https"
                    ):
                        continue

                    if parsed_page.netloc != home_domain:
                        continue

                    if page_url not in visited_pages:
                        visited_pages.add(page_url)
                        pages_to_scan.append(page_url)

                    
                    if len(pages_to_scan) >= 5:
                        break

                
                for page_url in pages_to_scan:
                    try:
                        if page_url == url:
                            page_soup = home_soup
                        else:
                            page_response = requests.get(
                                page_url,
                                timeout=15,
                                headers=headers
                            )
                            page_response.raise_for_status()

                            page_soup = BeautifulSoup(
                                page_response.text,
                                "html.parser"
                            )

                        emails, mobiles, landlines, other = (
                            extract_contacts(page_soup)
                        )

                        website_emails.update(emails)
                        website_mobiles.update(mobiles)
                        website_landlines.update(landlines)
                        website_other_phones.update(other)

                    except requests.RequestException as error:
                        show_result(
                            f"Contact page error: "
                            f"{page_url} - {error}"
                        )
                        continue

                
                found_emails.update(website_emails)

                
                record = {
                    "website": url,
                    "emails": sorted(website_emails),
                    "mobiles": sorted(website_mobiles),
                    "landlines": sorted(website_landlines),
                    "other_phones": sorted(website_other_phones)
                }

                contact_results.append(record)

                show_result(
                    f"Emails: {len(website_emails)}\n"
                    f"Mobile numbers: {len(website_mobiles)}\n"
                    f"Landline numbers: {len(website_landlines)}"
                )

                if not (
                    website_emails
                    or website_mobiles
                    or website_landlines
                    or website_other_phones
                ):
                    show_result(
                        "No public contact details found."
                    )

            except requests.RequestException as error:
                show_result(
                    f"Website error: {url} - {error}"
                )
                continue

            except Exception as error:
                show_result(
                    f"Processing error for {url}: {error}"
                )
                continue

            
            progress = index / total
            window.after(
                0,
                lambda p=progress: progress_bar.set(p)
            )

        show_result("\n--- Scraping completed ---")
        show_status(
            f"Finished! Processed {len(contact_results)} "
            f"websites; found {len(found_emails)} unique emails."
        )

        window.after(
            0,
            lambda: save_button.configure(state="normal")
        )

    finally:
        is_running = False
        window.after(
            0,
            lambda: start_button.configure(state="normal")
        )




def start_scraping():
    global is_running

    if is_running:
        return

    urls = url_box.get("1.0", "end").strip().splitlines()
    urls = [url.strip() for url in urls if url.strip()]

    if not urls:
        show_status("Please enter website URLs.")
        return

    valid_urls = []

    for url in urls:
        url = url.strip().strip('"').strip("'").strip(",")

        if not url:
            continue

        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        parsed = urlparse(url)

        if (
            parsed.scheme in ("http", "https")
            and parsed.hostname
            and "." in parsed.hostname
            and " " not in parsed.hostname
        ):
            valid_urls.append(url)
        else:
            show_result(f"Invalid URL skipped: {url}")

    if not valid_urls:
        show_status("No valid website URLs found.")
        return

    is_running = True
    start_button.configure(state="disabled")
    save_button.configure(state="disabled")

    progress_bar.set(0)
    results_box.delete("1.0", "end")
    found_emails.clear()
    contact_results.clear()

    results_box.insert(
        "end",
        f"Starting scan of {len(valid_urls)} websites...\n"
    )

    threading.Thread(
        target=scrape_websites,
        args=(valid_urls,),
        daemon=True
    ).start()

def save_results():
    if not contact_results:
        messagebox.showwarning(
            "No Results",
            "Please scrape some websites first."
        )
        return

    file_path = filedialog.asksaveasfilename(
        title="Save Company Contact Results",
        defaultextension=".xlsx",
        initialfile="Company Contact Data.xlsx",
        filetypes=[("Excel Workbook", "*.xlsx")]
    )

    if not file_path:
        return

    try:
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Company Contacts"

        sheet.append([
            "Sr. No.",
            "Company Website",
            "Email Addresses",
            "Mobile Numbers",
            "Landline Numbers",
            "Other Phone Numbers"
        ])

        for number, record in enumerate(
            contact_results, start=1
        ):
            sheet.append([
                number,
                record["website"],
                "; ".join(record["emails"]) or "Not found",
                "; ".join(record["mobiles"]) or "Not found",
                "; ".join(record["landlines"]) or "Not found",
                "; ".join(record["other_phones"]) or "Not found"
            ])

        
        sheet.freeze_panes = "A2"
        sheet.auto_filter.ref = sheet.dimensions

        widths = {
            "A": 10,
            "B": 35,
            "C": 40,
            "D": 25,
            "E": 25,
            "F": 25
        }

        for column, width in widths.items():
            sheet.column_dimensions[column].width = width

        workbook.save(file_path)

        status_label.configure(
            text=(
                f"Saved results for "
                f"{len(contact_results)} websites."
            )
        )

        messagebox.showinfo(
            "Success",
            "Company contact data saved successfully!"
        )

    except Exception as error:
        status_label.configure(
            text=f"Save failed: {error}"
        )
        messagebox.showerror(
            "Save Error",
            str(error)
        )




start_button = ctk.CTkButton(
    left_frame,
    text="Start Scraping",
    width=220,
    height=40,
    command=start_scraping
)
start_button.pack(pady=8)

save_button = ctk.CTkButton(
    left_frame,
    text="Save Results",
    width=220,
    height=40,
    fg_color="#18865B",
    hover_color="#116642",
    command=save_results,
    state="disabled"
)
save_button.pack(pady=(3, 12))

window.mainloop()



