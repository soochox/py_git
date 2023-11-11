import PyPDF2
import csv

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def save_text_to_csv(text, csv_file_path):
    with open(csv_file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Text"])  # 헤더 추가 (옵션)
        writer.writerow([text])

if __name__ == "__main__":
    # PDF 파일 경로 설정 (raw string 사용)
    pdf_path = r"C:\Users\PC\Desktop\coding\python_git\buja_under700_thema.pdf"  # 실제 PDF 파일 경로로 변경하세요.

    # 텍스트 추출
    extracted_text = extract_text_from_pdf(pdf_path)

    # CSV 파일로 저장
    csv_file_path = r"C:\Users\PC\Desktop\coding\python_git\output.csv"  # 저장할 CSV 파일 경로 (raw string 사용)
    save_text_to_csv(extracted_text, csv_file_path)

    print("텍스트를 CSV 파일로 저장했습니다.")

    # 이 코드에서는 csv.writer를 사용하여 텍스트를 CSV 파일에 작성합니다.
    # 헤더가 필요하다면 writer.writerow(["Text"])와 같이 헤더를 추가할 수 있습니다.
    # newline=""은 CSV 파일에 빈 줄이 추가되지 않도록 하는 옵션입니다.
    # 코드를 실행하면 output.csv에 텍스트가 저장됩니다.