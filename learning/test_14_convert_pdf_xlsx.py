import tabula

pdfPath = '/Users/anupmanekar/DevWorkspace/ephemeris/slae_2000.pdf'
outputPath = '/Users/anupmanekar/DevWorkspace/ephemeris/slae_2000.xlsx'
dfs = tabula.read_pdf(pdfPath, pages=[2,3])
print(dfs)
tabula.convert_into(pdfPath, outputPath, output_format="csv", pages=[2,3])