import PyPDF2
import pandas as pd

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def save_text_to_excel(text, excel_path):
    df = pd.DataFrame({"Text": [text]})
    df.to_csv(excel_path, index=False)
    # df.to_excel(excel_path, index=False)

if __name__ == "__main__":
    # PDF 파일 경로 설정 (raw string 사용)
    pdf_path = r"C:\Users\PC\Desktop\coding\python_git\buja_under700_thema.pdf"  # 실제 PDF 파일 경로로 변경하세요.

    # 텍스트 추출
    extracted_text = extract_text_from_pdf(pdf_path)

    # 엑셀로 저장
    excel_path = r"C:\Users\PC\Desktop\coding\python_git\output.csv"  # 저장할 엑셀 파일 경로 (raw string 사용)
    save_text_to_excel(extracted_text, excel_path)

    print("텍스트를 엑셀로 저장했습니다.")
