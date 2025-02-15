import re

def load_sample_text(filename):
    with open(filename, 'r') as file:
        return file.read()
    
#Regex function to filter needed elements
# 1. Extracting Email Addresses
def extract_Emails(Emails):
    Emails_pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    return re.findall(Emails_pattern, Emails)

# 2. Extracting URLs
def extract_urls(text):
    url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    return re.findall(url_pattern, text)

# 3. Extracting Phone Numbers (various formats)
def extract_phone_numbers(text):
    phone_pattern = r'(\(?\d{3}\)?[\s.-]?)?\d{3}[\s.-]?\d{4}'
    return re.findall(phone_pattern, text)

# 4. Extracting Credit Card Numbers
def extract_credit_cards(text):
    credit_card_pattern = r'(\d{4}[-\s]?){3}\d{4}'
    return re.findall(credit_card_pattern, text)

# 5. Extracting HTML Tags
def extract_html_tags(text):
    html_tag_pattern = r'<[^>]+>'
    return re.findall(html_tag_pattern, text)

# 6. Extracting Hashtags
def extract_hashtags(text):
    hashtag_pattern =r'#\w+'
    return re.findall(hashtag_pattern, text)

# 7. Extracting Currency Amounts
def extract_currency_amounts(text):
    currency_pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
    return re.findall(currency_pattern, text)

# 8. Extracting Time in 12-hour or 24-hour format
def extract_times(text):
    time_pattern =  r'\b(?:[01][0-9]|2[0-3]):[0-5][0-9]\b|(?:0?[1-9]|1[0-2]):[0-5][0-9] ?(?:AM|PM)\b'
    return re.findall(time_pattern, text)

# Main function to load the text and run the extractions
def main():
    main_sample = load_sample_text('main_sample.txt')

    if not main_sample:
        print("Error: The file could not be found.")
        return
    
    print("Extracted Emails:", extract_Emails(main_sample))
    print("Extracted URLs:", extract_urls(main_sample))
    print("Extracted Phone Numbers:", extract_phone_numbers(main_sample))
    print("Extracted Credit Card Numbers:", extract_credit_cards(main_sample))
    print("Extracted HTML Tags:", extract_html_tags(main_sample))
    print("Extracted Hashtags:", extract_hashtags(main_sample))
    print("Extracted Currency Amounts:", extract_currency_amounts(main_sample))
    print("Extracted Times:", extract_times(main_sample))
  

if __name__ == '__main__':
    main()