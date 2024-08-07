from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches
import schedule
import aspose.words as aw




class DollarQuote:

    def __init__(self):
        
        self.chrome_options = Options()

        self.arguments = ['--lang=pt-BR', '--window-size=800,800', '--incognito']

        for argument in self.arguments:
            self.chrome_options.add_argument(argument)

        self.chrome_options.add_experimental_option("prefs", {
            'download.directory_upgrade': True,
            'download.prompt_for_download': False,
            "profile.default_content_setting_values.notifications": 2, 
            "profile.default_content_setting_values.automatic_downloads": 1,
        })

        self.driver = webdriver.Chrome(options=self.chrome_options)

        self.date = datetime.now().strftime("%d/%m/%Y")

        self.file_name = f'{self.date.replace("/","-")}.png'
    
    
    def get_dollar_quote(self):
        self.driver.get("https://www.google.com/search?q=dolar")
        sleep(5)
        self.cotacao_dolar = self.driver.find_element(By.CLASS_NAME,'DFlfde.SwHCTb').text.replace(',','.')
        return self.cotacao_dolar
        
        
    def save_screenshot(self):
        sleep(2)
        self.driver.save_screenshot(self.file_name)
        sleep(1)
        self.driver.close()
        self.driver.quit()
        
        


class DocxToPdfConverter:
    
    def __init__(self, texts, image_path, docx_filename, pdf_filename):
        self.texts = texts
        self.image_path = image_path
        self.docx_filename = docx_filename
        self.pdf_filename = pdf_filename

    def write_docx(self,doc,texts):
        
        for k,text in self.texts.items():
            if k == 'title':
                paragraph = doc.add_paragraph()
                run = paragraph.add_run(text)
                run.bold = True
                run.font.size = Pt(20)
                paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
                
            elif k == 'paragraph3':
                doc.add_paragraph(text)
                paragraph = doc.add_paragraph()
                run = paragraph.add_run()
                run.add_picture(image_path, width=Inches(4.0))
                paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
                
                
            else:
                doc.add_paragraph(text)
        doc.save(self.docx_filename)
        
                          

    def create_docx(self):
        
        doc = Document()
        
        self.write_docx(doc,self.texts)
        
    def convert_docx_to_pdf(self,docx_path,name_pdf):
        
        doc = aw.Document(docx_path)
        
        doc.save(name_pdf)
        

    def create_and_convert(self):
        
        self.create_docx()
        

        self.convert_docx_to_pdf(self.docx_filename,self.pdf_filename)


bot =  DollarQuote()

dollar_quote = bot.get_dollar_quote()

bot.save_screenshot()

texts = {
    'title': f'Cotação Atual do Dólar – {dollar_quote} ({bot.date})',
    'paragraph1':f'O dólar está no valor de {dollar_quote}, na data {bot.date}.',
    'paragraph2':'Valor cotado no site https://www.google.com/search?q=dolar',
    'paragraph3':'Print da cotação atual',
    'paragraph4':'Cotação feita por – Rafael Ribeiro'
    }

image_path = bot.file_name

docx_filename = bot.file_name.replace('.png','.docx')

pdf_filename = bot.file_name.replace('.png','.pdf')

converter = DocxToPdfConverter(texts, image_path, docx_filename, pdf_filename)

converter.create_and_convert()
