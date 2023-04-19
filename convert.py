import os
import subprocess

url = input("Enter the URL: ")
output_format = input("Enter the output format (docx, pdf, or epub): ")

# Define the input and output file names
input_file = "input.html"
output_file = f"output.{output_format}"

# Use the subprocess module to call pandoc to convert the URL content to the desired format
subprocess.run(f"pandoc {url} -o {input_file}", shell=True)
subprocess.run(f"pandoc {input_file} -o {output_file}", shell=True)

# Remove the temporary input file
os.remove(input_file)

print(f"Conversion complete! The output file '{output_file}' has been created.")
