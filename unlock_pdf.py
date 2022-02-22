import sys

import pikepdf

# Run as: python3 unlock_pdf.py input.pdf [password]
pdf = pikepdf.open(sys.argv[1], sys.argv[2])
pdf.save(sys.argv[1] + "output.pdf")
