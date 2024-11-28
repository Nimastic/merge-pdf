from PyPDF2 import PdfMerger

# List of PDF files with full paths
pdf_files = [
    r"C:/Users/jerie/Downloads/To Compile/Lecture 0.pdf",
    r"C:/Users/jerie/Downloads/To Compile/Lecture 1.pdf",
    r"C:/Users/jerie/Downloads/To Compile/Lecture 2.pdf",
    r"C:/Users/jerie/Downloads/To Compile/Lecture 3.pdf",
    r"C:/Users/jerie/Downloads/To Compile/Lecture 4.pdf",
    r"C:/Users/jerie/Downloads/To Compile/Lecture 5.pdf",
    r"C:/Users/jerie/Downloads/To Compile/Lecture 6.pdf",
    r"C:/Users/jerie/Downloads/To Compile/Lecture 7.pdf",
    r"C:/Users/jerie/Downloads/To Compile/Lecture 8.pdf",
    r"C:/Users/jerie/Downloads/To Compile/Lecture 9.pdf",
    r"C:/Users/jerie/Downloads/To Compile/Lecture 10.pdf",
    r"C:/Users/jerie/Downloads/To Compile/Lecture 11.pdf",
    r"C:/Users/jerie/Downloads/To Compile/Lecture 12.pdf"
]

# Create a PdfMerger object
merger = PdfMerger()

# Append each PDF in sequence
for pdf in pdf_files:
    merger.append(pdf)

# Save the merged PDF
output_file = r"C:/Users/jerie/Downloads/To Compile/Merged_Lectures.pdf"
merger.write(output_file)
merger.close()

print(f"Merged PDF saved as {output_file}")
