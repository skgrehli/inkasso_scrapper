from selenium import webdriver
import csv


if __name__ == '__main__':
    
    # Taking Control of the browser ....
    browser = None
    try:
        browser = webdriver.Chrome()
    except Exception as error:
        print(error)

    if browser is None:
        print("Selenium not opened")
        sys.exit()
    with open("output.csv", "wb+") as out_file :
        writer = csv.writer(out_file)
        writer.writerow(['Name' ,'Street', 'PLZ', 'Ort', 'Email', 'www', 'Telefon', 'Fax'])
        url = "https://www.inkasso.de/mitglieder/liste"
        browser.get(url)
        url_link = []
        for element in browser.find_elements_by_css_selector('div.field-content.more-link a'):
            url_link.append(element.get_attribute('href'))

        for product_url in url_link:
            browser.get(product_url)
            try:
                name = browser.find_element_by_css_selector('h1.field-name-title-field').text.strip().replace('\n', '').encode('ascii', 'ignore').decode('ascii')
            except Exception as e:
                name = ''
            try:
                street = browser.find_element_by_css_selector('.street-block .thoroughfare').text.strip().replace('\n', '').encode('ascii', 'ignore').decode('ascii')
            except Exception as e:
                street = ''
            try:
                plz = browser.find_element_by_css_selector('span.postal-code').text.strip().replace('\n', '').encode('ascii', 'ignore').decode('ascii')
            except Exception as e:
                plz = ''
            try:
                ort = browser.find_element_by_css_selector('span.locality').text.strip().replace('\n', '').encode('ascii', 'ignore').decode('ascii')
            except Exception as e:
                ort = ''

            try:
                telefon = browser.find_element_by_css_selector('div.field-name-field-member-phone div.even').text.strip().replace('\n', '').encode('ascii', 'ignore').decode('ascii')
            except Exception as e:
                telefon = ''
            try:
                fax = browser.find_element_by_css_selector('div.field-name-field-member-fax div.even').text.strip().replace('\n', '').encode('ascii', 'ignore').decode('ascii')
            except Exception as e:
                fax = ''
            try:
                email = browser.find_element_by_css_selector('div.field-name-field-member-email div.even span').text.strip().replace('\n', '').encode('ascii', 'ignore').decode('ascii')
            except Exception as e:
                email = ''
            try:
                www = browser.find_element_by_css_selector('div.field-name-field-member-homepage div.even a').text.strip().replace('\n', '')
            except Exception as e:
                www = ''


            try:
                writer.writerow([name,street,plz,ort,email,www,telefon,fax])
            except Exception as e:
                print(e)