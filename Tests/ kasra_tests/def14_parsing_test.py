from sec_parsers import Filing, download_sec_filing

#def14a document from edgar
# html = download_sec_filing('https://www.sec.gov/Archives/edgar/data/320193/000130817924000010/laapl2024_def14a.htm')

#10k document from edgar
# html = download_sec_filing('https://www.sec.gov/Archives/edgar/data/1318605/000162828024002390/tsla-20231231.htm')

#10k document from drive
# html = download_sec_filing('https://drive.google.com/uc?export=download&id=1DGLewUcTAvDM_VsHyo-kzNywlNhqkt6t')

#def14a document from drive
html = download_sec_filing('https://drive.google.com/uc?export=download&id=1y7VffXl5XrpolGd1OvCn_SkLkSOAtv0d')

filing = Filing(html)
filing.parse() # parses filing
filing.visualizeXml() # opens filing in webbrowser with highlighted section headers

